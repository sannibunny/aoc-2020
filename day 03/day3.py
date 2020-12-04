
TREE = "#"

def part1(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            grid.append(line.strip())

    count = 1
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        count *= slopes(grid, right, down)

    return count


def slopes(grid, right, down):
    loop = len(grid[0])
    row = 0
    col = 0
    count = 0
    while row < len(grid):
        if grid[row][col % loop] == TREE:
            count += 1

        row += down
        col += right

    return count


if __name__ == "__main__":
    print(part1("input.txt"))
