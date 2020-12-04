from typing import Dict

MANDATORY = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
VALID = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}


def part1(filename):
    valid = 0
    new_passport = set()
    with open(filename, 'r') as file:
        for line in file:
            if line == "\n":
                if "cid" in new_passport:
                    new_passport.remove("cid")

                if new_passport == MANDATORY:
                    valid += 1

                new_passport = set()
            else:
                pairs = line.strip().split(" ")
                for pair in pairs:
                    key, _, _ = pair.partition(":")
                    key = key.strip()
                    new_passport.add(key)

    if "cid" in new_passport:
        new_passport.remove("cid")

    if new_passport == MANDATORY:
        valid += 1

    return valid


def part2(filename):
    passports = []
    valid = 0
    with open(filename, 'r') as file:
        passport = {}
        for line in file:
            if line == "\n":
                passports.append(passport)
                passport = {}
            else:
                pairs = line.strip().split(" ")
                for pair in pairs:
                    key, _, value = pair.partition(":")
                    passport[key.strip()] = value.strip()

    passports.append(passport)
    for passport in passports:
        print("----")
        if valid_passport(passport):
            valid += 1

    return valid


def valid_passport(passport: Dict[str, str]):
    print(passport)
    if not MANDATORY.issubset(passport.keys()):
        return False

    byr = int(passport["byr"])
    if not 1920 <= byr <= 2002:
        print("invalid byr:", byr)
        return False

    iyr = int(passport["iyr"])
    if not 2010 <= iyr <= 2020:
        print("invalid iyr:", iyr)
        return False

    eyr = int(passport["eyr"])
    if not 2020 <= eyr <= 2030:
        print("invalid eyr:", eyr)
        return False

    hgt = passport["hgt"]
    if hgt.endswith("cm"):
        hgt = int(hgt[:-2])
        if not 150 <= hgt <= 193:
            print("invalid hgt (cm):", hgt)
            return False
    else:
        if not hgt.endswith("in"):
            print("invalid hgt", hgt)
            return False

        hgt = int(hgt[:-2])
        if not 59 <= hgt <= 76:
            print("invalid hgt (in):", hgt)
            return False

    hcl = passport["hcl"]
    if not hcl.startswith("#") or len(hcl) != 7:
        print("invalid hcl:", hcl)
        return False

    for char in hcl[1:]:
        if not (char.isdigit() or char in "abcdef"):
            print("invalid hcl:", hcl)
            return False

    ecl = passport["ecl"]
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        print("invalid ecl:", ecl)
        return False

    pid = passport["pid"]
    if len(pid) != 9:
        print("invalid pid:", pid)
        return False

    for char in pid:
        if not char.isdigit():
            print("invalid pid:", pid)
            return False

    return True


if __name__ == "__main__":
    print(part2("input.txt"))
