#!/usr/bin/env python
"""Day 8"""

import numpy as np
import tool


def main():
    data = [list(map(int, list(line.strip("\n")))) for line in tool.read_return_data(8)]
    track, score, ct = {}, {}, 0

    def count_things(grid: list, is_transposed: bool):
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                a = (j + 0) * (is_transposed) + (i + 0) * (not is_transposed)
                b = (i + 0) * (is_transposed) + (j + 0) * (not is_transposed)
                c = 2 * (is_transposed) + 0 * (not is_transposed)
                d = 3 * (is_transposed) + 1 * (not is_transposed)
                track[(a, b)] = track.get((a, b), 0)
                score[(a, b)] = score.get((a, b), [0, 0, 0, 0])
                for idx, other in enumerate(grid[i + 0][: j + 0][::-1]):
                    if (other >= val) or (idx == len(grid[i][:j]) - 1):
                        track[(a, b)] += (other >= val)
                        score[(a, b)][c] = idx + 1
                        break
                for idx, other in enumerate(grid[i + 0][j + 1 :]):
                    if (other >= val) or (idx == len(grid[i][j + 1 :]) - 1):
                        track[(a, b)] += (other >= val)
                        score[(a, b)][d] = idx + 1
                        break

    count_things(data, False)
    count_things(np.array(data).T.tolist(), True)
    for val in track.values():
        ct += (val < 4)
    print("Part 1:", ct)
    print("Part 2:", np.max(np.array([np.prod(val) for val in score.values()])))


if __name__ == "__main__":
    main()
