#!/usr/bin/env python3

def read_file(file_name):
    cord1 = []
    cord2 = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.split('   ')
            cord1.append(int(line[0]))
            cord2.append(int(line[1].strip()))
    return [cord1, cord2]

def compute_occurence(list):
    occures = {}
    for key in list:
        if key in occures:
            occures[key] += 1
        else:
            occures[key] = 1
    return occures

def compute_similarity_score(file_name):
    lists = read_file(file_name)

    occures = compute_occurence(lists[1])

    sum = 0

    for i in lists[0]:
        sum += i * occures.get(i, 0)
    return sum

def main():
    print(compute_similarity_score('input_chal2.txt'))

if __name__ == '__main__':
    main()