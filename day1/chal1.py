#!/usr/bin/env python3

def read_file(file_name):
    cord1 = []
    cord2 = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.split('   ')
            cord1.append(int(line[0]))
            cord2.append(int(line[1].strip()))
    cord1.sort()
    cord2.sort()
    return [cord1, cord2]

def get_cord(file_name):
    lists = read_file(file_name)
    sum = 0
    for x1, x2 in zip(lists[0], lists[1]):
        if x1 > x2:
            sum += x1 - x2
        elif x1 < x2:
            sum += x2 - x1
        else:
            pass

    return sum

def main():
    print(get_cord('input1.txt'))
    print(get_cord('input2.txt'))

if __name__ == '__main__':
    main()