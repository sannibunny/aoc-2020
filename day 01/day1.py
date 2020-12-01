
def part1(filename):
    with open(filename, 'r') as file:
        nums = []
        for line in file:
            nums.append(int(line))

        for i in range(0, len(nums)):
            a = nums[i]
            for j in range(i, len(nums)):
                b = nums[j]
                if a + b == 2020:
                    return a * b

    return 0


def part2(filename):
    with open(filename, 'r') as file:
        nums = []
        for line in file:
            nums.append(int(line))

        for i in range(0, len(nums)):
            a = nums[i]
            for j in range(i, len(nums)):
                b = nums[j]
                for k in range(j, len(nums)):
                    c = nums[k]
                    if a + b + c == 2020:
                        return a * b * c

    return 0


if __name__ == "__main__":

    print(part1("input.txt"))
    print(part2("input.txt"))
