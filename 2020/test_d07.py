from d07 import count_contents, create_bag_tree, deep_find, parse_rule, find_inner_bag_2, Node, BagContent
import pytest
from typing import Dict


example_rules_1 = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags.",
]

example_rules_2 = [
    "shiny gold bags contain 2 dark red bags.",
    "dark red bags contain 2 dark orange bags.",
    "dark orange bags contain 2 dark yellow bags.",
    "dark yellow bags contain 2 dark green bags.",
    "dark green bags contain 2 dark blue bags.",
    "dark blue bags contain 2 dark violet bags.",
    "dark violet bags contain no other bags.",
]

@pytest.fixture
def rules_1():
    return {color: contents for color, contents in [parse_rule(r) for r in example_rules_1]}


@pytest.fixture
def rules_2():
    return {color: contents for color, contents in [parse_rule(r) for r in example_rules_2]}


def test_part1_one_level_search(rules_1):
    result = find_inner_bag_2(rules_1, 'shiny gold')
    assert result == set(['bright white', 'muted yellow'])


def test_part1_recursive_search(rules_1):
    result = deep_find(rules_1, 'shiny gold')
    assert result == {'bright white', 'dark orange', 'light red', 'muted yellow'}


def test_part2_bag_counts(rules_1, rules_2):
    tree_1: Dict[str, Node] = create_bag_tree(rules_1)
    assert count_contents(tree_1['faded blue']) == 1
    assert count_contents(tree_1['dotted black']) == 1
    assert count_contents(tree_1['vibrant plum']) == 12
    assert count_contents(tree_1['dark olive']) == 8
    assert count_contents(tree_1['shiny gold']) - 1 == 32  # -1 so we don't count the outer shiny gold bag

    tree_2: Dict[str, Node] = create_bag_tree(rules_2)
    assert count_contents(tree_2['shiny gold']) -1  == 126  # -1 so we don't count the outer shiny gold bag
