#!/usr/bin/env python
"""Import tool"""

def read_return_data(day: int) -> list:
    with open(f"day{day}-input", "r", encoding="utf-8") as file:
        return "$".join(file.readlines()).strip("\n").split("$")

def read_return_data_2(day:int):
    with open(f"day{day}-input", "r", encoding="utf-8") as file:
        return file.read()
