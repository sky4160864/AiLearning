#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:Administrator
@file:py_test.py
@time:2020/06/06
"""
import numpy as np


def test01():
    arr01 = np.array([1, 2, 3])
    arr02 = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr01)
    print(arr02)
    print(arr01 - arr02)
    arr01_tile = np.tile(arr01, (2, 1))
    print(arr01_tile)
    print(arr01_tile - arr02)
    print("==============")
    print(arr01 + arr02)
    print(arr01_tile + arr02)
