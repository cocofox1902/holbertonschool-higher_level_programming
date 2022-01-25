#!/usr/bin/python3
"""Module to supplies one function
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function to return a nex matrix divided

        Args:
            m_a(list): list of integer of float
            m_b(list): list of integer of float
    """
    return (np.matmul(m_a, m_b))
