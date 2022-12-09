#!/usr/bin/env python
"""Day 7"""

import numpy as np
import tool


def main():
    data = [line.strip("\n") for line in tool.read_return_data(7)]
    tree = {}
    size = {"/": 0}
    parent, path = "/", "/"
    level = []
    for idx, line in enumerate(data):
        if line[:4] == "$ cd":
            if line[5:7] == "..":
                level.pop()
                parent = level[-1]
            else:
                parent = line[5:]
                level.append(parent)
                path = "-".join(level)
                if path not in tree:
                    tree[path], size[path] = [], 0
                if len(level) > 1:
                    tree[path] += ["-".join(level[:i]) for i, _ in enumerate(level)][1:]
        elif line[:4] == "$ ls":
            sub_idx = int(idx) + 1
            while sub_idx < len(data):
                info = data[sub_idx].split(" ")
                if info[0] == "$":
                    break
                if info[0] == "dir":
                    pass
                else:
                    size[path] += int(info[0])
                sub_idx += 1
    for child, parent in tree.items():
        for member in parent:
            size[member] += size[child] * (child != "/")
    total_size = 0
    for member in size.values():
        total_size += member * (member <= 100000)
    delete_size, min_dir = 30000000 - (70000000 - size["/"]), 999999999999
    for dir_size in size.values():
        if min_dir > dir_size >= delete_size:
            min_dir = dir_size
    print("Part 1:", total_size)
    print("Part 2:", min_dir)


if __name__ == "__main__":
    main()
