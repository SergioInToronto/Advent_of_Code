import re

REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} # cid
HEIGHT_REGEX = re.compile("([0-9]+)(cm|in)")
HAIR_COLOUR_REGEX = re.compile("^#[0-9a-f]{6}$")
VALID_EYE_COLOURS = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
PASSPORT_ID_REGEX = re.compile("^[0-9]{9}$")

with open("day4.input") as f:
    passports = f.read().strip().split('\n\n')

valid_count = 0

for passport in passports:
    fields = dict(field.split(":") for field in passport.split())
    if REQUIRED_FIELDS.difference(fields.keys()):
        # print("Rejected on if REQUIRED_FIELDS.difference")
        continue
    if not 1920 <= int(fields['byr']) <= 2002:
        # print("Rejected on if not 1920")
        continue
    if not 2010 <= int(fields['iyr']) <= 2020:
        # print("Rejected on if not 2010")
        continue
    if not 2020 <= int(fields['eyr']) <= 2030:
        # print("Rejected on if not 2020")
        continue
    match = re.search(HEIGHT_REGEX, fields['hgt'])
    if not match:
        # print("Rejected on if not match")
        continue
    height_scale, height_units = match.groups()
    if height_units == 'cm' and not 150 <= int(height_scale) <= 193:
        # print("Rejected on if height_units ==")
        continue
    if height_units == 'in' and not 59 <= int(height_scale) <= 76:
        # print("Rejected on if height_units ==")
        continue
    if not re.search(HAIR_COLOUR_REGEX, fields['hcl']):
        # print("Rejected on if not re")
        continue
    if not fields['ecl'] in VALID_EYE_COLOURS:
        # print("Rejected on if not fields")
        continue
    if not re.search(PASSPORT_ID_REGEX, fields['pid']):
        # print("Rejected on pid")
        continue
    valid_count += 1

print(valid_count)