def get_reports(input):
    reports = []
    for line in input[:-1].split('\n'):
        reports.append([int(num) for num in line.split()])
    return reports

def is_report_safe(report):
        safe = True
        # first two data points of report
        if abs(report[0] - report[1]) > 3:
            safe = False
            return safe
        increasing = report[0] < report[1]

        # rest of report
        for index in range(1, len(report)):
            if (increasing and report[index - 1] >= report[index]):
                safe = False
                break
        
            if (not increasing and report[index - 1] <= report[index]):
                safe = False
                break
        
            if abs(report[index] - report[index - 1]) > 3:
                safe = False
                break
        
        return safe

def with_dampener(report):
    variations = []
    for i in range(len(report)):
        before = []
        after = []
        if i > 0:
            before = report[:i]
        if i < len(report) - 1:
            after = report[i+1:]
        variations.append(before + after)
    return variations
        

def part1(input):
    reports = get_reports(input)

    safe_reports = 0
    for report in reports:
        if is_report_safe(report):
            safe_reports += 1

    return safe_reports

def part2(input):
    reports = get_reports(input)

    safe_reports = 0
    for report in reports:
        if is_report_safe(report):
            safe_reports += 1
        else:
            variations = with_dampener(report)
            for variation in variations:
                if is_report_safe(variation):
                    safe_reports += 1
                    break

    return safe_reports
