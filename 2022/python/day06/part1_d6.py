def find_marker(input, marker_length):
    for i in range(len(input) - marker_length):
        if len(set(input[i:i + marker_length])) == marker_length:
            return i + marker_length