#!/usr/bin/env python
"""Day 5"""

import copy
import tool


def main():
    data = [line.strip("\n") for line in tool.read_return_data(5)]
    crates = []
    instructions = []
    for idx, line in enumerate(data):
        if line == "":
            instructions = [
                list(map(int, sl.split(" ")[1::2])) for sl in data[idx + 1 :]
            ]
            break
        crates.append(line)
    crates = crates[:-1][::-1]
    for idx, line in enumerate(crates):
        nl = line[1::2]
        crates[idx] = [nl[idx] for idx in range(0, len(nl), 2)]
    crates = list(map(list, zip(*crates)))
    crates = [[sl for sl in line if sl.strip()] for line in crates]
    print(
        "Part 1:",
        "".join([line[-1] for line in move_crates(True, copy.deepcopy(crates), instructions)]),
    )
    print(
        "Part 2:",
        "".join([line[-1] for line in move_crates(False, copy.deepcopy(crates), instructions)]),
    )


def move_crates(switch: bool, muh_crates: list, instructions: list):
    for line in instructions:
        if switch:
            moving = muh_crates[line[1] - 1][-line[0] :][::-1]
        else:
            moving = muh_crates[line[1] - 1][-line[0] :]
        muh_crates[line[2] - 1] += moving
        muh_crates[line[1] - 1] = muh_crates[line[1] - 1][: -line[0]]
    return muh_crates


if __name__ == "__main__":
    main()
