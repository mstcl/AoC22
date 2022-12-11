#!/usr/bin/env python
"""Day 8"""

import numpy as np
import tool


def main():
    data = [line.strip("\n") for line in tool.read_return_data(9)]
    guide = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}

    def run_sim(knots: list):
        visited = set()
        for line in data:
            direction, num_steps = tuple(line.split(" "))
            for i in range(int(num_steps)):
                knots[0] = [
                    knots[0][0] + guide[direction][0],
                    knots[0][1] + guide[direction][1],
                ]
                for idx, _ in enumerate(knots[:-1]):
                    if not check_neighbours(knots[idx + 1], knots[idx]):
                        t_change = get_update(knots[idx + 1], knots[idx])
                        knots[idx + 1] = [
                            t_change[0] + knots[idx + 1][0],
                            t_change[1] + knots[idx + 1][1],
                        ]
                    else:
                        break
                visited.add(tuple(knots[-1]))
        return visited

    print(
        "Part 1:",
        len(run_sim([[0, 0] for i in range(2)])),
    )
    print(
        "Part 2:",
        len(run_sim([[0, 0] for i in range(10)])),
    )


def get_update(t_pos, h_pos):
    x, y = tuple(t_pos)
    cross = [
        (2 + x, y), (x, 2 + y),
        (-2 + x, y), (x, -2 + y),
    ]
    diag = [
        (1 + x, 2 + y), (2 + x, 1 + y), (2 + x, 2 + y), (2 + x, -1 + y),
        (1 + x, -2 + y), (2 + x, -2 + y), (-2 + x, -1 + y), (-1 + x, -2 + y),
        (-2 + x, -2 + y), (-2 + x, 1 + y), (-1 + x, 2 + y), (-2 + x, 2 + y),
    ]
    diff = list(np.sign([h_pos[0] - x, h_pos[1] - y]))
    return diff * (tuple(h_pos) in cross) + diff * (tuple(h_pos) in diag)


def check_neighbours(t_pos, h_pos):
    x, y = tuple(t_pos)
    neighbours = [
        (0 + x, 1 + y), (0 + x, 0 + y), (0 + x, -1 + y),
        (1 + x, 1 + y), (1 + x, 0 + y), (1 + x, -1 + y),
        (-1 + x, 1 + y), (-1 + x, 0 + y), (-1 + x, -1 + y),
    ]
    return tuple(h_pos) in neighbours


if __name__ == "__main__":
    main()
