#!environment/bin/python3
"""Script to give individual tests import context"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../sudoku')))

import sudoku
