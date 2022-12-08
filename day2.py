#!/usr/bin/env python
"""Day 2"""

import tool


def main():
    data = ["".join(line.strip("\n").split(" ")) for line in tool.read_return_data(2)]
    win = {"A": "Y", "B": "Z", "C": "X"}
    draw = {"A": "X", "B": "Y", "C": "Z"}
    loss = {"A": "Z", "B": "X", "C": "Y"}
    shape_score = {"X": 1, "Y": 2, "Z": 3}

    def calculate(data: list) -> int:
        score = 0
        for line in data:
            score += 6 * (line[1] == win[line[0]]) + 3 * (line[1] == draw[line[0]])
            score += shape_score[line[1]]
        return score

    print("Part 1:", calculate(data))
    for idx, line in enumerate(data):
        selection = (
            loss[line[0]] * (line[1] == "X")
            + draw[line[0]] * (line[1] == "Y")
            + win[line[0]] * (line[1] == "Z")
        )
        data[idx] = f"{line[0]}{selection}"
    print("Part 2:", calculate(data))


if __name__ == "__main__":
    main()
