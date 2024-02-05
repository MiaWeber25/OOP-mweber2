#! /usr/bin/env python3

def sort(a: int, b: int) -> bool:
    return a < b  # if a < b return TRUE


def solve() -> None:
    # Read input and assign to a,b
    line = input()
    a_str, b_str = line.split()
    a = int(a_str)
    b = int(b_str)
    if sort(a, b):  # a is the smaller number
        print(a, b)
    else:
        print(b, a)  # b is the smaller number


if __name__ == "__main__":
    solve()
