#! /usr/bin/env python3
"""
This module contains logic to get input and validate it.
"""
from calc_cost import calc_cost


class titlecost:
    """ This class contains logic to recieve and validate input"""
    def __init__(self) -> None:
        """ No initialization required """
        pass

    @staticmethod
    def validate_title(title: str) -> str:
        """ Method checks alphabetic chars, between 1-30 chars."""
        if not title.isalpha() or not (1 <= len(title) <= 30):
            raise ValueError("only alphabetic chars. Between 1-30 chars")
        return title

    @staticmethod
    def validate_max_cost(max_cost: str) -> float:
        """ Method checks max_cost is float between 0-100."""
        try:
            max_cost_float = float(max_cost)
        except ValueError:
            raise ValueError("only floats")
        if not (0 <= max_cost_float <= 100):
            raise ValueError("only between 0 and 100")
        return max_cost_float

    def solve(self) -> None:
        """ Method solves problem by getting input
        and calling appropriate methods"""
        title, max_cost_str = input().split(" ", 1)
        title = self.validate_title(title)
        max_cost = self.validate_max_cost(max_cost_str)
        actual_cost = calc_cost.calculate_cost(title)
        print(min(actual_cost, max_cost))


if __name__ == "__main__":
    solved = titlecost()
    solved.solve()
