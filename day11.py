#!/usr/bin/env python
"""Day 11"""

import numpy as np
import tool


def monk_mul(x, num, im, is_part_1):
    return (x * num) // im if is_part_1 else (x * num) % im


def monk_plus(x, num, im, is_part_1):
    return (x + num) // im if is_part_1 else (x + num) % im


def monk_test(x, num):
    return x % num == 0


def main():
    def boom(turns: int, im: int, is_part_1: bool):
        data = [line.strip("\n") for line in tool.read_return_data(11)]
        items = [val.split(" ")[4:] for i, val in enumerate(data[1::7])]
        for i, line in enumerate(items):
            items[i] = list(map(int, [val.strip(",") for val in line]))
        db = dict(enumerate(items))
        instructions = {
            0: (0, 5, 11, 2, 3), 1: (0, 11, 5, 4, 0),
            2: (1, 2, 19, 5, 6), 3: (1, 5, 13, 2, 6),
            4: (0, -1, 7, 0, 3), 5: (1, 4, 17, 7, 1),
            6: (1, 6, 2, 7, 5), 7: (1, 7, 3, 4, 1),
        }
        scores = [0, 0, 0, 0, 0, 0, 0, 0]
        for _ in range(turns):
            for monk_id in range(8):
                for item in db[monk_id]:
                    scores[monk_id] += 1
                    info = instructions[monk_id]
                    new = monk_mul(
                        item, info[1] * (info[1] != -1) + item * (info[1] == -1),
                        im, is_part_1,
                    ) * (info[0] == 0) + monk_plus(item, info[1], im, is_part_1) * (info[0] == 1)
                    if monk_test(new, info[2]):
                        db[info[3]].append(new)
                    else:
                        db[info[4]].append(new)
                db[monk_id] = []
        return np.prod(sorted(scores)[6:])

    print("Part 1:", boom(20, 3, True))
    print("Part 2:", boom(10000, 9699690, False))


if __name__ == "__main__":
    main()
