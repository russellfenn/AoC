"""
Day 04
Data Validation

The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

from types import FunctionType
from typing import List, Dict
import re

required_fields: List = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']



def parse_data(data: List[str]) -> List[Dict[str, str]]:
    passports: List[Dict[str,str]] = list()
    d: Dict[str,str] = dict()
    for line in data:
        if len(line) == 0:  # empty
            passports.append(d)
            d = dict()
        else:
            for element in line.split(' '):
                key, value = element.split(':')
                d[key] = value
    if d:  # include the last record!
        passports.append(d)
    return passports


def check_required_fields(passport: Dict[str, str]) -> Dict[str, bool]:
    """Return a dict of key values and if the exist or not in the given dict"""
    return {key: key in passport for key in required_fields}


# To validate _values_, let's make a validation rule for each data type.
# Each validator will accept a string, then convert to int if required.
# Returns True or False
# Later, I think it would be better to use Pydantic.

def validate_byr(byr: str) -> bool:
    """Birth Year"""
    try:
        birth_year = int(byr)
        return birth_year >= 1920 and birth_year <= 2002
    except:
        return False


def validate_iyr(iyr: str) -> bool:
    """Issue Year"""
    try:
        issue_year = int(iyr)
        return issue_year >= 2010 and issue_year <= 2020
    except:
        return False

def validate_eyr(eyr: str) -> bool:
    """Expiration Year"""
    try:
        expire_year = int(eyr)
        return expire_year >= 2020 and expire_year <= 2030
    except:
        return False


hgt_rx = re.compile(r'([0-9]{2,3})(cm|in)')


def validate_hgt(hgt: str) -> bool:
    """Height"""
    try:
        re_match = hgt_rx.match(hgt)
        if re_match:
            height = int(re_match.group(1))
            unit = re_match.group(2)
            if unit == "cm":
                return height >= 150 and height <= 193
            elif unit == "in":
                return height >= 59 and height <= 76
            else:
                return False
    except:
        return False
    return False


hcl_rx = re.compile(r'^#[0-9a-f]{6}$')


def validate_hcl(hcl: str) -> bool:
    """Hair Color"""
    return hcl_rx.match(hcl) is not None


def validate_ecl(ecl: str) -> bool:
    """Eye Color"""
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


pid_rx = re.compile(r'^[0-9]{9}$')


def validate_pid(pid: str) -> bool:
    """Passport ID"""
    return pid_rx.match(pid) is not None

field_validators: Dict[str, FunctionType] = {
    "byr": validate_byr,
    "iyr": validate_iyr,
    "eyr": validate_eyr,
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": validate_ecl,
    "pid": validate_pid,
}

def check_values(passport: Dict[str, str]) -> Dict[str, bool]:
    #try:
        return {key: validator(passport[key]) for key, validator in field_validators.items()}
    #except:
    #    return {}


def validate_passport(passport: Dict[str, str]) -> Dict[str, bool]:
    """All required fields present, and have valid values"""
    return all(check_required_fields(passport).values()) \
           and all(check_values(passport).values())

if __name__ == "__main__":
    with open('d04.input', 'r') as f:
        passports = parse_data([l.rstrip() for l in f.readlines()])
    
    valid_keys: List[Dict[str, bool]] = [check_required_fields(p) for p in passports]
    valids: List[bool] = [all(vk.values()) for vk in valid_keys]
    print(f"[Required Fields] Found {sum(valids)} valid passports.")

    # Check valid values
    valid_passports: List[Dict[str, bool]] = [validate_passport(p) for p in passports]
    print(f"[Values] Found {sum(valid_passports)} valid passports.")