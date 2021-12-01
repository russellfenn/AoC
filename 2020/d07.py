"""
Day 07 - Rules parsing?

Long list of rules that must be parsed.

Rule Format:

<color> bags contain <number> <color> bag(s)[, <color> bag(s)].

First task is to make a Regex that parses the rule line.

Parse the rules (594 of them!) into a Dict of 

  <bag color>: str
     Contents: List[Tuple[int, str]]

## Part 1

Finding all the bags that may contain a bag is done by
searching through every rule, and returning the color of
the bag containing the target color. But then we need to
search again for the bags that contain those bags, etc.

## Part 2

We build a tree, starting with our target bag (shiny gold)

 [(1) Shiny Gold]
 |
 |-> [(1) Dark Olive]  [(2) Vibrant Plum]
     |                 |
     |                 |-> [(5) Faded Blue]  [(6) Dotted Black]
     |
     |-> [(3) Faded Blue]  [(4) Dotted Black]

1 + 1*(3+4) + 2 + 2*(5+6)

"""

import re
from typing import Dict, List, Optional, Set, Tuple, NewType
from dataclasses import dataclass

outer_bag_rx = re.compile(r'^(?P<bag_color>[a-z ]+?)\sbags contain ')
inner_bag_rx = re.compile(r'\s*(?P<quant>[0-9]+)\s(?P<color>[a-z ]+?)\sbags?\.?')

def parse_rule(rule: str) -> Tuple[str, List[Tuple[int, str]]]:
    """ Returns (bag_color, [(quant, bag_color), (quant, bag_color)])
    """
    res = outer_bag_rx.match(rule)
    if res:
        outer_bag_color: str = res.group(1)
        contents: List[Tuple[int, str]] = list()
        for _ in rule[res.end():].split(','):
            res2 = inner_bag_rx.match(_)
            if res2:
                contents.append((int(res2.group(1)), res2.group(2)))
        return (outer_bag_color, contents)


def find_inner_bag(rules: Dict[str, Tuple], target_color: str) -> Set[str]:
    """Return a List of bag colors that may contain the target color"""
    result: Set[str] = set()
    for color, contents in rules.items():
        if target_color in [inner_color for quant, inner_color in contents]:
            result.update(color)
    return result


def find_inner_bag_2(rules: Dict[str, Tuple], target_color: str) -> Set[str]:
    return set([color for color, contents in rules.items() if target_color in [inner_color for quant, inner_color in contents]])


def deep_find(rules: Dict[str, Tuple], target_color: str) -> Set[str]:
    results: Set[str] = set()

    new_bags: Set[str] = find_inner_bag_2(rules, target_color)
    # print(f"Found new bags: {new_bags} that contain a '{target_color}' bag.")
    results.update(new_bags)
    for bag in new_bags:
        results.update(deep_find(rules, bag))
    return results


# Warning! Python hack
# Delay defining the Node type to avoid a circular reference
Node = NewType('Node', 'Node')

@dataclass
class BagContent:
    quant: int
    color: Node

@dataclass
class Node:
    color: str
    contents: List[BagContent]


def create_bag_tree(rules: Dict[str, List[Tuple[int, str]]]) -> Dict[str, Node]:
    """Load all the bags into a tree structure with quantities."""
    all_bags: Dict[str, Node] = dict()
    # Pass 1 just make the nodes
    # This allows us to add in any order
    for color in rules:
        all_bags[color] = Node(color=color, contents=[])
    # pass 2 adds bags to other bags
    for color, contents in rules.items():
        for bc in contents:
            all_bags[color].contents.append(BagContent(quant=bc[0], color=all_bags[bc[1]]))
    return all_bags


def count_contents(node: Node) -> int:
    """Recursive"""
    if len(node.contents) == 0:
        return 1  # count myself
    return 1 + sum([bg.quant * count_contents(bg.color) for bg in node.contents])


if __name__ == "__main__":
    with open('d07.input', 'r') as f:
        rules: Dict[str, List[Tuple[int, str]]]
        rules = {color: contents for color, contents in [parse_rule(r) for r in f.readlines()]}
    
    print(f"Parsed {len(rules)} rules.")
    shiny_gold: Set[str] = deep_find(rules, 'shiny gold')
    print(f"[Part 1] {len(shiny_gold)} bags may contain a shiny gold bag.")

    # Part 2 - load all bags into a big dictionary
    all_bags: Dict[str, Node] = create_bag_tree(rules)
    print(f"[Part 2] A shiny gold bag contains {count_contents(all_bags['shiny gold']) -1} bags!")
