#!/usr/bin/env python3

with open('input.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]

sequences = ['X', 'M', 'A', 'S']
directions = ['right', 'down', 'left', 'up', 'right-up', 'right-down', 'left-up', 'left-down']
nb_xmas = 0

M_SIZE = len(grid) - 1 # assuming is a square matrix

def is_out_of_range(x, y, direction):
    print(f"checking out of range for {x}, {y} -> {direction}")
    if direction == 'right' and y + len(sequences) - 1 > M_SIZE:
        return True
    if direction == 'left' and y - len(sequences) + 1 < 0:
        return True
    if direction == 'up' and x - len(sequences) + 1 < 0:
        return True
    if direction == 'down' and x + len(sequences) - 1 > M_SIZE:
        return True
    if direction == 'right-up' and (y + len(sequences) - 1 > M_SIZE or x - len(sequences) + 1 < 0):
        return True
    if direction == 'right-down' and (y + len(sequences) - 1 > M_SIZE or x + len(sequences) - 1 > M_SIZE):
        return True
    if direction == 'left-up' and (y - len(sequences) + 1 < 0 or x - len(sequences) + 1 < 0):
        return True
    if direction == 'left-down' and (y - len(sequences) + 1 < 0 or x + len(sequences) - 1 > M_SIZE):
        return True
    return False

def is_valid_sequence(x, y, direction):
    for i, char in enumerate(sequences):
        print (f"testing sequence char: {char} at {x}, {y} -> index {i} - {direction}")
        if direction == 'right':
            if i == len(sequences) - 1 and grid[x][y + i] == char:
                return True
            elif is_out_of_range(x, y, direction):
                return False
            elif grid[x][y + i] == char:
                continue
            else:
                return False
        if direction == 'left':
            if i == len(sequences) - 1 and grid[x][y - i] == char:
                return True
            elif is_out_of_range(x, y, direction):
                return False
            elif grid[x][y - i] == char:
                continue
            else:
                return False
        if direction == 'up':
            if i == len(sequences) - 1 and grid[x - i][y] == char:
                return True
            elif is_out_of_range(x, y, direction):
                return False
            elif grid[x - i][y] == char:
                continue
            else:
                return False
        if direction == 'down':
            if i == len(sequences) - 1 and grid[x + i][y] == char:
                return True
            elif is_out_of_range(x, y, direction):
                return False
            elif grid[x + i][y] == char:
                continue
            else:   
                return False
        if direction == 'right-up':
            if i == len(sequences) - 1 and grid[x - i][y + i] == char:
                return True
            elif is_out_of_range(x, y, direction):
                return False
            elif grid[x - i][y + i] == char:
                continue
            else:
                return False
        if direction == 'right-down':
            if i == len(sequences) - 1 and grid[x + i][y + i] == char:
                return True
            elif is_out_of_range(x, y, direction):
                return False
            elif grid[x + i][y + i] == char:
                continue
            else:
                return False
        if direction == 'left-up':
            if i == len(sequences) - 1 and grid[x - i][y - i] == char:
                return True
            elif is_out_of_range(x, y, direction):
                return False
            elif grid[x - i][y - i] == char:
                continue
            else:
                return False
        if direction == 'left-down':
            if i == len(sequences) - 1 and grid[x + i][y - i] == char:
                return True
            elif is_out_of_range(x, y, direction):
                return False
            elif grid[x + i][y - i] == char:
                continue
            else:
                return False

def main():
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for direction in directions:
                if is_valid_sequence(i, j, direction):
                    counter += 1
                    print(f"Found sequence new nb: {counter}")

    print(f"Total: {counter}")

if __name__ == '__main__':
    main()