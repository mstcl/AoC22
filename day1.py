#!/usr/bin/env python
"""Day 1"""

import numpy as np
import tool


def main():
    data = np.sort(np.array([
                np.sum(list(map(int, line.split("\n"))))
                for line in "".join(tool.read_return_data(1)).split("\n\n")
            ]))
    print("Part 1:", np.max(data))
    print("Part 2:", np.sum(data[-3:]))

if __name__ == "__main__":
    main()
