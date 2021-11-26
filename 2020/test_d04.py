import d04
import pytest
from typing import Dict, List

mixed_sample_data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

@pytest.fixture
def sample_data():
    return mixed_sample_data.split('\n')

invalid_passport_data = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

@pytest.fixture
def invalid_passports():
    return invalid_passport_data.split('\n')


valid_passport_data = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

@pytest.fixture
def valid_passports():
    return valid_passport_data.split('\n')


def test_required_fields(sample_data):
    # Parse passports into a list
    passports: List[Dict[str, str]] = d04.parse_data(sample_data)

    valid_keys: List[Dict[str, bool]] = [d04.check_required_fields(p) for p in passports]
    assert len(valid_keys) == len(passports)

    # Now just get a summary of all the valid_keys
    valids: List[bool] = [all(vk.values()) for vk in valid_keys]
    assert valids == [True, False, True, False]


def test_field_validations():
    assert d04.validate_byr("1979") == True
    assert d04.validate_byr("1919") == False
    assert d04.validate_byr("3.14") == False
    assert d04.validate_byr(1980) == True

    assert d04.validate_hgt("120cm") == False
    assert d04.validate_hgt("180") == False
    assert d04.validate_hgt("180cm") == True
    assert d04.validate_hgt("5ft") == False


def test_valid_passport_list(valid_passports):
    passports: List[Dict[str, str]] = d04.parse_data(valid_passports)
    req_fields_d = [d04.check_required_fields(p) for p in passports]
    all_req_fields = [all(rf.values()) for rf in req_fields_d]
    assert all(all_req_fields) == True
    valid_fields_d = [d04.check_values(p) for p in passports]
    all_valid_fields = [all(vf.values()) for vf in valid_fields_d]
    assert all(all_valid_fields) == True


def test_invalid_passport_list(invalid_passports):
    passports: List[Dict[str, str]] = d04.parse_data(invalid_passports)
    valid_fields_d = [d04.check_values(p) for p in passports]
    all_valid_fields = [all(vf.values()) for vf in valid_fields_d]
    assert any(all_valid_fields) == False
