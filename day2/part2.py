#!/usr/bin/env python3

def get_reports(file_name):
    with open(file_name, 'r') as file:
        reports = [line.strip() for line in file.readlines()]
    return reports

def is_safe(levels):
    direction = 0 if levels[0] > levels[1] else 1
    for i in range(len(levels) - 1):
        if levels[i] == levels[i+1] or abs(levels[i] - levels[i+1]) > 3:
            return False
        if (direction == 1 and levels[i] > levels[i+1]) or (direction == 0 and levels[i] < levels[i+1]):
            return False
    return True

def check_report(levels):

    if is_safe(levels):
        return True

    for i in range(len(levels)):
        if is_safe(levels[:i] + levels[i+1:]):
            return True

    return False


def compute_report_levels(reports):
    sum = 0
    for report in reports:
        levels = [int(level) for level in report.split(' ')]
        safe = check_report(levels)
        if safe:
            sum += 1
    return sum


def main():
    reports_little = get_reports('input_little.txt')
    reports_big = get_reports('input_big.txt')
    print("Nb reports safe for little input {}, out of {}".format(
        compute_report_levels(reports_little), len(reports_little)))
    print("Nb reports safe for big input {}, out of {}".format(
        compute_report_levels(reports_big), len(reports_big)))


if __name__ == '__main__':
    main()
