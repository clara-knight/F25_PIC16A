#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 23:38:14 2025

@author: liaochunyang
"""


class Matrix:

    def __init__(self, elements=[0], shape=(1, 1)):
        if not len(elements) == shape[0] * shape[1]:
            raise InvalidMatrixError("Invalid shape")
        self.elements = elements
        self.shape = shape

    def __iter__(self):
        pass

    def reshape(self, elements, shape):
        # eg [1,2,3,4,5,6], (2,3) ->  [[1,2,3], [4,5,6]]
        for i in shape[0]:
            print(i)


class MatrixIterator:
    pass


class InvalidMatrixError(Exception):

    def __init__(self, error_message):
        self.message = error_message

    def __str__(self):
        return self.message

