#!/usr/bin/env python
"""Day 6"""

import tool


def main():
    data = tool.read_return_data(6)[0]
    def find_marker(target: int):
        seen = []
        last_idx = 0
        for idx, ch in enumerate(data):
            if len(seen) == target:
                if len(set(seen)) == len(seen):
                    last_idx = idx
                    break
                seen = seen[1:]
            seen.append(ch)
        return last_idx
    print("Part 1:", find_marker(4))
    print("Part 2:", find_marker(14))

if __name__ == "__main__":
    main()
