import re


BAG_RULE_REGEX = re.compile("^([a-z ]+) bags contain (.*?).$")
BAG_CONTENT_REGEX = re.compile("([0-9]+) ([a-z ]+) bags?")
# [('2', 'striped magenta'), ('2', 'dark coral'), ('1', 'bright orange'), ('4', 'plaid blue')]


input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')

bag_rules = {}
for row in raw:
    bag_colour, allowed_content = re.search(BAG_RULE_REGEX, row).groups()
    bag_rules[bag_colour] = allowed_content


def _list_holders(bag_colour):
    result = set()
    holders = [x for x in bag_rules if bag_colour in bag_rules[x]]
    result.update(holders)
    for x in holders:
        res = _list_holders(x)
        result.update(res)
    return result


def _count_bags(bag_colour):
    total = 0
    for (count, nested_bag_colour) in re.findall(BAG_CONTENT_REGEX, bag_rules[bag_colour]):
        # print(f"{bag_colour} Contains: {count} {nested_bag_colour} bag(s)")
        total += (int(count) * _count_bags(nested_bag_colour)) + int(count)
    return total


print(len(_list_holders("shiny gold")))
# import pdb; pdb.set_trace()
print(_count_bags("shiny gold"))