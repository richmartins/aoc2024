#!/usr/bin/env python3

def get_reports(file_name):
    with open(file_name, 'r') as file:
        reports = [line.strip() for line in file.readlines()]
    return reports

def compute_report_levels(reports):
    sum = 0
    for report in reports:
        levels = [int(level) for level in report.split(' ')]
        safe = True

        # 1 if increasing 0 if deacreasing
        direction = 0 if levels[0] > levels[1] else 1

        for i in enumerate(levels):
            if i == len(levels) - 1:
                break

            if levels[i] == levels[i+1] or abs(levels[i] - levels[i+1]) > 3:
                safe = False
                break

            if (direction == 1 and levels[i] > levels[i+1]) or (direction == 0 and levels[i] < levels[i+1]):
                safe = False
                break

        if safe:
            sum += 1

    print(sum)
        


def main():
    reports = get_reports('input.txt')
    reports2 = get_reports('input_part1.txt')
    compute_report_levels(reports2)

if __name__ == '__main__':
    main()