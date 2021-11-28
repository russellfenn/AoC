"""
Day 04 - Using Pydantic

Since this is essentially a data validation problem, let's see if using Pydantic makes it easier.

This mostly works - the test cases given (and tested in test_d04.py) either pass or fail as expected,
but the accepted answer of 188 valid passports that I determined through the hand-built validators differs 
from the 178 calculated with Pydantic.

I think this is caused by the faulty @validator('hgt'), which fails to init properly.

```plain
{'eyr': '2029', 'byr': '1942', 'cid': '232', 'iyr': '2016', 'hgt': '193cm', 'hcl': '#733820', 'pid': '175cm', 'ecl': 'oth'}
2 validation errors for Passport
hgt
  __init__() takes exactly 3 positional arguments (2 given) (type=type_error)
pid
  string does not match regex "^[0-9]{9}$" (type=value_error.str.regex; pattern=^[0-9]{9}$)
```

"""

from pydantic import BaseModel, ValidationError, validator, conint, constr
# from pydantic.class_validators import validator
from typing import Dict, List, Literal, Optional
from d04 import parse_data
import re


hgt_rx = re.compile(r'([0-9]{2,3})(cm|in)')

class Passport(BaseModel):
    byr: conint(ge=1920, le=2002)
    iyr: conint(ge=201, le=2020)
    eyr: conint(ge=2020, le=2030)
    hgt: str
    hcl: constr(regex=r"^#[0-9a-f]{6}$")
    ecl: Literal['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    pid: constr(regex=r"^[0-9]{9}$")
    #cid: Optional[constr(regex=r"^[0-9]{9}$")]



    @validator('hgt')
    def height_validator(cls, v) -> str:
        try:
            re_match = hgt_rx.match(v)
            if re_match:
                height = int(re_match.group(1))
                unit = re_match.group(2)
                if unit == "cm":
                    if height <= 150 or height >= 193:
                        raise ValidationError("Height in cm must be 150<=height<=193")
                elif unit == "in":
                    if height <= 59 or height >= 76:
                        raise ValidationError("Height in in muat be 59<=height<=76")
                return v
        except:
            pass
        raise ValidationError("Must specify height in in or cm")


if __name__ == "__main__":
    with open('d04.input', 'r') as f:
        passports = parse_data([l.rstrip() for l in f.readlines()])
    
    # Check valid values using Pydantic
    valid_passports: List[Dict[str, bool]] = list()
    for suspect_passport in passports:
        try:
            p: Passport = Passport(**suspect_passport)
            valid_passports.append(p)
        except ValidationError as e:
            print(suspect_passport)
            print(e)
    print(f"[Pydantic] Found {len(valid_passports)} valid passports.")
