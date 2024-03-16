#! /usr/bin/env python3
"""
This module calculates the cost of a title.
"""


class calc_cost:
    """ This class contains logic for calculating costs"""
    @staticmethod
    def calculate_cost(title: str) -> float:
        """ Method calculates cost based on length"""
        return (len(title))
