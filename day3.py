#!/usr/bin/env python
"""Day 3"""

import tool


def main():
    def ord_char(char: str) -> int:
        return ord(char)

    def calc_score(vals):
        score = 0
        for num in vals:
            score += (num - 38) * (num <= 90) + (num - 96) * (num > 90)
        return score

    data = [
        list(map(ord_char, list(line.strip("\n")))) for line in tool.read_return_data(3)
    ]
    overlaps = []
    for line in data:
        size = len(line)
        s1 = set(line[:size//2])
        s2 = set(line[size//2:])
        overlaps.append(list(s1.intersection(s2))[0])
    print("Part 1:", calc_score(overlaps))
    overlaps = []
    for idx in range(0, len(data), 3):
        s1 = set(data[idx])
        s2 = set(data[idx + 1])
        s3 = set(data[idx + 2])
        overlaps.append(list(s1.intersection(s2.intersection(s3)))[0])
    print("Part 2:", calc_score(overlaps))


if __name__ == "__main__":
    main()
