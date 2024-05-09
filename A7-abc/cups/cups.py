"""
Main class to call appropriate methods and satisfy Kattis requirements.
"""
from typing import TextIO
from cup_stacking import CupStacking


def main() -> None:
    import sys
    input_stream: TextIO = sys.stdin
    solver: CupStacking = CupStacking(input_stream)
    solver.read_input()
    solver.solve()
    solver.print_answer()


if __name__ == "__main__":  # pragma: no cover
    main()
