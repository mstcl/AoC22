#!/usr/bin/env python
"""Day 12"""

import numpy as np
import json
import tool


def main():
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
                elif right_element < left_element:
                    return False
                else:
                    continue
            if isinstance(left_element, int):
                left_element = [left_element]
            if isinstance(right_element, int):
                right_element = [right_element]
            answ = is_in_order(left_element, right_element)
            if answ is None:
                continue
            return answ

    data = list(filter(None, [line.strip("\n") for line in tool.read_return_data(13)]))
    tally = 0
    for idx, item in enumerate(data[::2]):
        left, right = json.loads(item), json.loads(data[1::2][idx])
        if is_in_order(left, right):
            tally += idx + 1

    print("Part 1:", tally)
    print("Part 2:")


if __name__ == "__main__":
    main()
