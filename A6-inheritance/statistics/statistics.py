#! /usr/bin/env python3
"""
This module contains logic to process input and call appropriate methods.
"""

from data_set import DataSet


class Statistics:
    """ Class to get input and output statistics. """

    @staticmethod
    def read_input() -> list[int]:
        """ Method to read and process input. """
        return list(map(int, input().split()))

    @staticmethod
    def print_output(output: str) -> None:
        """ Method to print the output. """
        print(output)

    @staticmethod
    def solve(data_set: DataSet) -> str:
        """ Method to format output """
        return f"Case {data_set.case_number}: {
            data_set.get_min()} {data_set.get_max()} {
                data_set.get_range()}"

    @staticmethod
    def process_data(input_data: list[int], case_number: int) -> str:
        """ Method to process single line of data. """
        sample = input_data[1:]
        # Create a list of data w/out first element
        data_set: DataSet = DataSet(sample)
        data_set.case_number = case_number
        return Statistics.solve(data_set)

    @staticmethod
    def process_input() -> None:
        """ Method to process input until EOF. """
        case_number = 1
        try:
            while True:
                input_data = Statistics.read_input()
                output = Statistics.process_data(input_data, case_number)
                Statistics.print_output(output)
                case_number += 1
        except EOFError:
            pass


if __name__ == "__main__":
    Statistics.process_input()
