import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from example_package_szabgab.example import add_one

def test_one():
    print('add_one to 2 is 3')
    assert add_one(2) == 3

