def process_input(input: str):
    fa = []
    ea = []
    for i, char in enumerate(input):
        # disk file array, disk empty space array at start
        if i % 2 == 0:
            fa.append(int(char))
        else:
            ea.append(int(char))
    return fa, ea

def print_drive(fa, ea):
    df_len = len(fa)
    drive_string = ""
    for i in range(df_len):
        drive_string += str(i) * fa[i]
        if i < len(ea):
            drive_string += "." * ea[i]
    print(drive_string)

def print_drive_part_2(d):
    drive_string = ""
    for e in sorted(d, key=lambda x: x[1]):
        length, start_idx, file_num = e
        file_string = "." if file_num == -1 else str(file_num)
        drive_string +=  file_string * length
    print(drive_string)


def part1(input):
    fa, ea = process_input(input)
    print_drive(fa, ea)

    checksum = 0
    idx_fa_right = len(fa) - 1
    idx_fa_left = 0
    idx_ea = 0
    idx_checksum = 0
    empty_space_left = ea[0]
    file_remainer = fa[-1]

    state = 0 # 0: count left index word, 1: moving word

    # read last file, move to first available space or start from there and fill
    while idx_fa_left <= idx_fa_right:

        if state == 0:
            # add checksum from left file
            # if moved right
            limit = file_remainer if idx_fa_left == idx_fa_right else fa[idx_fa_left]
            for i in range(idx_checksum, idx_checksum + limit):
                checksum += idx_checksum * idx_fa_left
                idx_checksum += 1
            idx_fa_left += 1
            state = 1

        elif state == 1:
            # move right file - three cases: for lenghts of word to move and empty_space_left
            # case right file is equal length to empty_space left
            if file_remainer == empty_space_left:
                for i in range(idx_checksum, idx_checksum + file_remainer):
                    checksum += idx_checksum * idx_fa_right
                    idx_checksum += 1
                idx_fa_right -= 1
                file_remainer = fa[idx_fa_right]
                idx_ea += 1
                empty_space_left = ea[idx_ea]
                state = 0

            # case right file can fit with leftovers space
            elif file_remainer < empty_space_left:
                for i in range(idx_checksum, idx_checksum + file_remainer):
                    checksum += idx_checksum * idx_fa_right
                    idx_checksum += 1
                empty_space_left -= file_remainer
                idx_fa_right -= 1
                file_remainer = fa[idx_fa_right]
                state = 1

            # case right file longer than empty_space
            elif file_remainer > empty_space_left:
                for i in range(idx_checksum, idx_checksum + empty_space_left):
                    checksum += idx_checksum * idx_fa_right
                    idx_checksum += 1
                file_remainer -= empty_space_left
                idx_ea += 1
                empty_space_left = ea[idx_ea]
                state = 0

    return checksum


def part2(input):
    fa, ea = process_input(input)

    # create drive structure from file array (fa) and empty block array (ea)
    d = []
    start_idx = 0
    file_num = 0
    for i in range(len(fa)):
        d.append((fa[i], start_idx, file_num))
        start_idx += fa[i]
        file_num += 1
        if i < len(ea):
            d.append((ea[i], start_idx, -1))
            start_idx += ea[i]

    len_d = len(d)
    idx_f_right = len_d - 1

    earliest_usable_empty_idx = 1

    while idx_f_right > 0:
        f_len, f_start, file_num = d[idx_f_right]

        # keep track of first non-0 length empty block
        while d[earliest_usable_empty_idx][0] == 0:
            earliest_usable_empty_idx += 2
        idx_empty = earliest_usable_empty_idx

        while idx_empty < idx_f_right:
            e_len, e_start, _ = d[idx_empty] # old empty block data

            if f_len <= e_len:
                # update file
                d[idx_f_right] = (f_len, e_start, file_num)
                # update empty space the file moved to
                d[idx_empty] = (e_len - f_len, e_start + f_len, -1)
                # update empty space before old file position, if not last add empty space after it
                lb, sb, _ = d[idx_f_right - 1]   # empty block before d f
                d[idx_f_right - 1] = (lb + f_len, sb, -1)
                if idx_f_right + 1 < len_d: # if not last element
                    lb, sb, _ = d[idx_f_right - 1]    # empty block before d f
                    la, sa, _ = d[idx_f_right + 1]  # empty block after d f
                    d[idx_f_right - 1] = (lb + la, sb, -1)
                    d[idx_f_right + 1] = (0, sa, -1)
                break

            idx_empty += 2

        idx_f_right -= 2
    
    # calculate checksum
    checksum = 0
    for f in d[::2]:
        length, start_idx, f_num = f
        for i in range(length):
            checksum += (start_idx + i) * f_num

    return checksum
