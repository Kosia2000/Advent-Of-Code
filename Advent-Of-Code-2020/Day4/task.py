filename = 'text.txt'


def open_file():
    lines = []
    with open(filename, "r") as file:
        for line in file.readlines():
            lines.append(line.strip())
    return lines


def make_pass():
    lines = open_file()
    pass_list = []
    passport = {}
    for line in lines:
        if line:
            words = line.split()
            for word in words:
                keys, values = word.split(':')
                passport[keys] = values
        else:
            pass_list.append(passport)
            passport = {}
    return pass_list


def check_fields(passport):
    valid = True
    for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if field not in passport:
            valid = False
            print(passport.keys(), len(passport.keys()))
    return valid


def _check_byr(passport):
    valid = True
    if 'byr' not in passport:
        valid = False
    elif not 1920 <= int(passport['byr']) <= 2002:
        valid = False
    return valid


def _check_iyr(passport):
    valid = True
    if 'iyr' not in passport:
        valid = False
    elif not 2010 <= int(passport['iyr']) <= 2020:
        valid = False
    return valid


def _check_eyr(passport):
    valid = True
    if 'eyr' not in passport:
        valid = False
    elif not 2020 <= int(passport['eyr']) <= 2030:
        valid = False
    return valid


def _check_hgt(passport):
    valid = True
    if 'hgt' not in passport:
        valid = False

    elif passport['hgt'].endswith('cm'):
        new = passport['hgt'].split('cm')
        if not 150 <= int(new[0]) <= 193:
            valid = False

    elif passport['hgt'].endswith('in'):
        new = passport['hgt'].split('in')
        if not 59 <= int(new[0]) <= 76:
            valid = False
    return valid


def _check_hcl(passport):
    valid = True
    if 'hcl' not in passport:
        valid = False
    elif len(passport['hcl']) != 7:
        valid = False
    return valid


def _check_ecl(passport):
    eye_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    valid = True
    if 'ecl' not in passport:
        valid = False
    elif passport['ecl'] not in eye_color:
        valid = False
    return valid


def _check_pid(passport):
    valid = True
    if 'pid' not in passport:
        valid = False
    elif len(passport['pid']) != 9:
        valid = False
    return valid


def validate(passport):
    valid = True

    if not _check_byr(passport):
        valid = False

    if not _check_iyr(passport):
        valid = False

    if not _check_eyr(passport):
        valid = False

    if not _check_hgt(passport):
        valid = False

    if not _check_hcl(passport):
        valid = False

    if not _check_ecl(passport):
        valid = False

    if not _check_pid(passport):
        valid = False

    return valid


def count_correct():
    count = 0
    count_fields = 0

    pass_list = make_pass()
    for passport in pass_list:
        if validate(passport):
            count += 1
        if check_fields(passport):
            count_fields += 1
    print("Valid passports part 1: {}".format(count_fields))
    print("Valid passports part 2: {}".format(count))


count_correct()
