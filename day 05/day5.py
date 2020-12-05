from typing import List


def part1(filename) -> List[int]:
    max_seat = 0
    seat_list = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            row = line[:7]
            col = line[7:]
            start = 0
            end = 127
            for char in row:
                if char == 'F':
                    if abs(end - start) <= 1:
                        end = start
                        continue

                    end = start + round((end - start) / 2) - 1
                else:
                    if abs(end - start) <= 1:
                        start = end

                    start = start + round((end - start) / 2)

            first = 0
            last = 7
            for char in col:
                if char == 'L':
                    if abs(last - first) <= 1:
                        last = first
                        continue

                    last = first + round((last - first) / 2) - 1
                else:
                    if abs(last - first) <= 1:
                        first = last
                        continue

                    first = first + round((last - first) / 2)

            seat_id = end * 8 + last
            max_seat = max(seat_id, max_seat)
            seat_list.append(seat_id)

    # return max_seat
    return seat_list


def part2(filename):
    seat_list = part1(filename)
    for i in range(0, len(seat_list)):
        current = seat_list[i]
        for j in range(i + 1, len(seat_list)):
            if abs(current - seat_list[j]) == 2:
                seat_id = min(current, seat_list[j]) + 1
                if seat_id not in seat_list:
                    return seat_id

    return 0


if __name__ == "__main__":
    print(part2("input.txt"))
