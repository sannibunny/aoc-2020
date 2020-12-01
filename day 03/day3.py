from typing import List, Tuple

# VERTICAL = '|'
# HORIZONTAL = '-'
# INTERSECT = 'X'

import sys

FIRST = '.'
INTERSECT = 'X'
TURN = '+'

UP = 'U'
DOWN = 'D'
RIGHT = 'R'
LEFT = 'L'

GRID_SIZE = 20000

CENTRAL_PORT = (0, 0)


def part1(filename):
    with open(filename, 'r') as file:
        # grid = create_grid(GRID_SIZE)
        occupied = {}
        for line in file:
            instructions = line.split(',')
            current_point = CENTRAL_PORT
            for instruction in instructions:
                instruction = instruction.strip()
                direction = instruction[0]
                distance = int(instruction[1:])
                occupied, current_point = draw_on_grid(occupied, direction, distance, current_point)

        dists = []
        min_elem = sys.maxsize
        min_key = None
        for key in occupied.keys():
            if occupied[key][0] == INTERSECT and key != CENTRAL_PORT:
                m_d = abs(key[0] - CENTRAL_PORT[0]) + abs(key[1] - CENTRAL_PORT[1])
                dists.append(m_d)
                if m_d < min_elem:
                    min_key = key

        # min_key is the coordinate i want to get to, i need to find a path to it

        print(min_key)
        return min(dists)


def draw_on_grid(grid, direction, distance, current_point):
    x, y = current_point

    if direction == UP:
        current_point = x, y + distance
        for i in range(distance):
            temp_y = y + i
            if grid.get((x, temp_y)) is None:
                grid[(x, temp_y)] = FIRST
            else:
                grid[(x, temp_y)] = INTERSECT

            if i == distance - 1:
                grid[(x, temp_y)] = grid[(x, temp_y)] + TURN

    elif direction == DOWN:
        current_point = x, y - distance
        for i in range(distance):
            temp_y = y - i
            if grid.get((x, temp_y)) is None:
                grid[(x, temp_y)] = FIRST
            else:
                grid[(x, temp_y)] = INTERSECT

            if i == distance - 1:
                grid[(x, temp_y)] = grid[(x, temp_y)] + TURN

    elif direction == LEFT:
        current_point = x - distance, y
        for i in range(distance):
            temp_x = x - i
            if grid.get((temp_x, y)) is None:
                grid[(temp_x, y)] = FIRST
            else:
                grid[(temp_x, y)] = INTERSECT

            if i == distance - 1:
                grid[(temp_x, y)] = grid[(temp_x, y)] + TURN

    elif direction == RIGHT:
        current_point = x + distance, y
        for i in range(distance):
            temp_x = x + i
            if grid.get((temp_x, y)) is None:
                grid[(temp_x, y)] = FIRST
            else:
                grid[(temp_x, y)] = INTERSECT

            if i == distance - 1:
                grid[(temp_x, y)] = grid[(temp_x, y)] + TURN

    return grid, current_point


if __name__ == "__main__":
    print(part1("input_test.txt"))
