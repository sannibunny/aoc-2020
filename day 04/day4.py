def part1(left, right):
    count = 0
    for password in range(left, right):
        adjacent = False
        increasing = True
        listed = list(str(password))
        counts = {}

        for i, num in enumerate(listed):
            if i < len(listed) - 1 and num > listed[i + 1]:
                increasing = False
                break

            counts[num] = counts.get(num, 0) + 1

        if increasing:
            for key in counts.keys():
                if counts[key] == 2:
                    print(password)
                    count += 1

    return count

if __name__ == "__main__":
    # print(part1(111122, 111123))
    print(part1(231832, 767346))