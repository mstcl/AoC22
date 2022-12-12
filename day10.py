#!/usr/bin/env python
"""Day 10"""

import numpy as np
import tool


def main():
    data = [line.strip("\n") for line in tool.read_return_data(10)]
    reg_X = 1
    cycle = 1
    signal_strength = []
    current_pixel = 0
    current_row = ["" for _ in range(40)]
    all_rows = []

    def get_sprite():
        return [reg_X - 1, reg_X, reg_X + 1]

    def check_and_store():
        if cycle in [(val * 40 + 20) for val in range(6)]:
            signal_strength.append(reg_X * cycle)

    def check_restore(pixel, row):
        if pixel in [(val * 40) for val in range(7)]:
            all_rows.append("".join(row))
            return 0, ["" for _ in range(40)]
        return pixel, row

    def do_tasks(row, cyc, pix):
        row[pix] = "█" * (pix in get_sprite()) + " " * (pix not in get_sprite())
        cyc += 1
        pix += 1
        pix, row = check_restore(pix, row)
        return row, cyc, pix

    for line in data:
        instruction = line.split(" ")
        if instruction[0] == "noop":
            current_row, cycle, current_pixel = do_tasks(
                current_row, cycle, current_pixel
            )
            check_and_store()
            continue
        current_row, cycle, current_pixel = do_tasks(current_row, cycle, current_pixel)
        check_and_store()
        current_row, cycle, current_pixel = do_tasks(current_row, cycle, current_pixel)
        reg_X += int(instruction[1])
        check_and_store()
    print("Part 1:", np.sum(signal_strength))
    print("Part 2:")
    for line in all_rows:
        print("".join(line))


if __name__ == "__main__":
    main()
