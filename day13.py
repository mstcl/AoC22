#!/usr/bin/env python
"""Day 13"""

import json
import tool


def is_in_order(lefty, righty):
    for idx in range(max(len(lefty), len(righty))):
        if idx > len(lefty) - 1:
            return True
        if idx > len(righty) - 1:
            return False
        left_element, right_element = lefty[idx], righty[idx]
        if isinstance(left_element, int) and isinstance(right_element, int):
            if left_element < right_element:
                return True
            if right_element < left_element:
                return False
            continue
        if isinstance(left_element, int):
            left_element = [left_element]
        if isinstance(right_element, int):
            right_element = [right_element]
        answ = is_in_order(left_element, right_element)
        if answ is None:
            continue
        return answ


def main():
    data = list(filter(None, [line.strip("\n") for line in tool.read_return_data(13)]))
    tally = 0
    for idx, item in enumerate(data[::2]):
        left, right = json.loads(item), json.loads(data[1::2][idx])
        tally += (idx + 1) * (is_in_order(left, right) is True)
    print("Part 1:", tally)
    print("Part 2:", check_list([[2]], data) * (check_list([[6]], data) + 1))


def check_list(compared, data):
    rank = 0
    for _, item in enumerate(data):
        left, right = json.loads(item), compared
        rank += is_in_order(left, right) is True
    return rank + 1


if __name__ == "__main__":
    main()
