#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 23:38:14 2025

@author: liaochunyang
"""

class Matrix:
    
     
    def __iter__(self):
        return MatrixIterator(self)
    
    
class MatrixIterator:
    pass