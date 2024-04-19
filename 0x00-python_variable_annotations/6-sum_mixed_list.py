#!/usr/bin/env python3

""" Complex types - mixed list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  returns sum as a float.
    Args:
        List[Union[int, float]]: the list of float

    Returns:
        string: their sum as a float
    """
    return float(sum(mxd_lst))
