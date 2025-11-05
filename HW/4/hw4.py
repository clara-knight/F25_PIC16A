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
        self.reshape()

    def __iter__(self):
        return MatrixIterator(self)

    def reshape(self):
        m = [
            self.elements[i : i + self.shape[1]]
            for i in range(0, len(self.elements), self.shape[1])
        ]
        self.elements = m


class MatrixIterator:
    def __init__(self, Matrix):
        self.shape = Matrix.shape
        self.elements = Matrix.elements
        self.i = 0
        self.j = -1

    def __next__(self):
        self.j += 1

        if self.j >= self.shape[1]:
            self.j = 0
            self.i += 1

        if self.i >= self.shape[0]:
            raise StopIteration

        return self.elements[self.i][self.j]


class InvalidMatrixError(Exception):
    def __init__(self, error_message):
        self.message = error_message

    def __str__(self):
        return f"Error: {self.message}."


class SquareMatrix(Matrix):
    def __init__(self, elements, shape):
        if shape[0] != shape[1]:
            raise InvalidMatrixError(
                "Square matrix should have the same number of rows and columns"
            )
        super().__init__(elements, shape)

    def Trace(self):
        self.trace = 1
        for i in self.shape[0]:
            self.trace *= self.elements[i][i]
