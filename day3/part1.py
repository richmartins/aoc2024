#!/usr/bin/env python3
import re

def get_input(filename):
    with open(filename) as file:
        data = file.readlines()
    return data

def parse_input(data):
    regex = r"mul\((\d{1,3})\,(\d{1,3})\)"
    
    line_sum = 0
    for line in data: # there is only one line ?
        sum = 0
        for match in re.finditer(regex, line):
            sum += int(match.group(1)) * int(match.group(2))
        line_sum += sum
    print(f"line_sum: {line_sum}")

def main():
    # print("example input")
    # data = get_input("example_input.txt")
    # parse_input(data)

    print("real input")
    data = get_input("input1.txt")
    parse_input(data)


if __name__ == "__main__":
    main()