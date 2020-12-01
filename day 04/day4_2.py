def part1(left, right):
    count = 0
    for password in range(left, right):
        listed = list(str(password))
        if listed[0] <= listed[1] <= listed[2] <= listed[3] <= listed[4] <= listed[5]:
            counts = {}
            for i in listed:
                counts[i] = counts.get(i, 0) + 1

            for num in counts.keys():
                # print(password, counts, "here")
                if counts[num] == 2:
                    count += 1
                    break

    return count

if __name__ == "__main__":
    print(part1(112233, 112234))
    print(part1(231832, 767346))