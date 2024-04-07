#! /usr/bin/env python3
"""
This module contains logic to process input and call appropriate methods.
"""

from data_set import DataSet


class Statistics:
    """ Class to get input and output statistics. """

    @staticmethod
    def solve(data_set: DataSet) -> str:
        """ Method to format output """
        return f"Case {data_set.case_number}: {
            data_set.get_min()} {data_set.get_max()} {
                data_set.get_range()}"

    @staticmethod
    def process_input() -> None:
        """ Method to process input """
        case_number = 1
        try:
            while True:
                input_data: list[int] = list(map(int, input().split()))
                sample: list[int] = input_data[1:]
                # Create a list of data w/out first element
                data_set: DataSet = DataSet(sample)
                data_set.case_number = case_number
                print(Statistics.solve(data_set))
                case_number += 1
        except EOFError:
            pass


if __name__ == "__main__":
    Statistics.process_input()
