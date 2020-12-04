JUMP = 4
ONE = 1
TWO = 2
REPLACE = 3


def day2(filename):
    with open(filename, 'r') as file:
        valid = 0
        for line in file:
            beginning, _, word = line.partition(":")
            word = word.strip()
            policy, _, letter = beginning.partition(" ")
            letter = letter.strip()
            policy = policy.strip()
            start, _, end = policy.partition("-")
            found_first = False
            found_second = False
            if word[int(start) - 1] == letter:
                found_first = True

            end = int(end) - 1
            if end < len(word) and word[end] == letter:
                found_second = True

            if found_first != found_second:
                valid += 1

    return valid


if __name__ == "__main__":
    print(day2("input.txt"))
