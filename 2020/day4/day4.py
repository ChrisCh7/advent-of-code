import re

birth_year = 'byr'
issue_year = 'iyr'
expiration_year = 'eyr'
height = 'hgt'
hair_color = 'hcl'
eye_color = 'ecl'
passport_id = 'pid'
country_id = 'cid'


def is_valid_passport_part1(passport: dict):
    mandatory_passport_fields = [birth_year, issue_year, expiration_year, height, hair_color, eye_color, passport_id]
    for field in mandatory_passport_fields:
        if field not in passport:
            return False
    return True


def is_valid_passport_part2(passport: dict):
    mandatory_passport_fields = [birth_year, issue_year, expiration_year, height, hair_color, eye_color, passport_id]
    for field in mandatory_passport_fields:
        if field not in passport:
            return False
    return validate_fields(passport)


def validate_fields(passport: dict):
    if not validate_birth_year(passport[birth_year]):
        return False
    if not validate_issue_year(passport[issue_year]):
        return False
    if not validate_expiration_year(passport[expiration_year]):
        return False
    if not validate_height(passport[height]):
        return False
    if not validate_hair_color(passport[hair_color]):
        return False
    if not validate_eye_color(passport[eye_color]):
        return False
    if not validate_passport_id(passport[passport_id]):
        return False
    return True


def validate_birth_year(birth_year):
    birth_year = int(birth_year)
    if 1920 <= birth_year <= 2002:
        return True
    return False


def validate_issue_year(issue_year):
    issue_year = int(issue_year)
    if 2010 <= issue_year <= 2020:
        return True
    return False


def validate_expiration_year(expiration_year):
    expiration_year = int(expiration_year)
    if 2020 <= expiration_year <= 2030:
        return True
    return False


def validate_height(height: str):
    if height[-2:] == 'cm':
        nr = int(height[:height.index('cm')])
        if 150 <= nr <= 193:
            return True
    if height[-2:] == 'in':
        nr = int(height[:height.index('in')])
        if 59 <= nr <= 76:
            return True
    return False


def validate_hair_color(hair_color: str):
    if re.search('^#[0-9a-f]{6}$', hair_color) is not None:
        return True
    return False


def validate_eye_color(eye_color):
    if eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False


def validate_passport_id(passport_id: str):
    if re.search('^[0-9]{9}$', passport_id) is not None:
        return True
    return False


def main():
    with open('in.txt') as file:
        data = file.read()
    passports_info = data.split('\n\n')
    passports = []
    for passport_info in passports_info:
        passport_fields = passport_info.split()
        passports.append(passport_fields)

    for passport_index in range(len(passports)):
        current_passport = passports[passport_index]
        current_passport_dict = {field.split(':')[0]: field.split(':')[1] for field in current_passport}
        passports[passport_index] = current_passport_dict

    valid_passport_count_part1 = 0
    valid_passport_count_part2 = 0
    for passport in passports:
        if is_valid_passport_part1(passport):
            valid_passport_count_part1 += 1
        if is_valid_passport_part2(passport):
            valid_passport_count_part2 += 1

    print('Part1:', valid_passport_count_part1)
    print('Part2:', valid_passport_count_part2)


if __name__ == '__main__':
    main()
