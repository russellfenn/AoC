from d02 import validate_password, parse_password_entry, validate_position_rule

def test_example():
    assert validate_password(1, 3, "a", "abcde") == True
    assert validate_password(1, 3, "b", "cdefg") == False
    assert validate_password(2, 9, "c", "ccccccccc") == True


def test_parsed_password():
    pp = parse_password_entry("1-3 a: abcde")
    assert pp[0] == 1
    assert pp[1] == 3
    assert pp[2] == 'a'
    assert pp[3] == 'abcde'
    assert validate_password(pp[0], pp[1], pp[2], pp[3])


def test_parsed_as_tuple():
    pp = parse_password_entry("1-3 a: abcde")
    assert validate_password(*pp)


rules_list = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

def test_count_rules():
    rules = [parse_password_entry(e) for e in rules_list]
    valids = [validate_password(*r) for r in rules]
    assert valids == [True, False, True]


def test_position_rule():
    assert validate_position_rule(1, 3, "a", "abcde") == True
    assert validate_position_rule(1, 3, "b", "cdefg") == False
    assert validate_position_rule(2, 9, "c", "ccccccccc") == False

def test_position_rules_list():
    rules = [parse_password_entry(e) for e in rules_list]
    valids = [validate_position_rule(*r) for r in rules]
    assert valids == [True, False, False]