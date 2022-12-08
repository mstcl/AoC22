#!/usr/bin/env python
"""Day 4"""

import tool


def main():
    data = [line.strip("\n").split(",") for line in tool.read_return_data(4)]
    ct = 0
    idx_to_ignore = []
    for idx, line in enumerate(data):
        bot_1, top_1 = tuple(map(int,line[0].split("-")))
        bot_2, top_2 = tuple(map(int,line[1].split("-")))
        if ((bot_1 <= bot_2) and (top_1 >= top_2)) or ((bot_2 <= bot_1) and (top_2 >= top_1)):
            ct += 1
            idx_to_ignore.append(idx)
            continue
    print("Part 1:", ct)
    ct2 = 0
    for idx, line in enumerate(data):
        if idx in idx_to_ignore:
            continue
        bot_1, top_1 = tuple(map(int,line[0].split("-")))
        bot_2, top_2 = tuple(map(int,line[1].split("-")))
        ct2 += 1 * ((top_2 >= bot_1 >= bot_2) or (top_1 >= bot_2 >= bot_1))
    print("Part 2:", ct+ct2)


if __name__ == "__main__":
    main()
