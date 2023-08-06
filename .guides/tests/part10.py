#!/usr/local/bin/python3
"""
Assess part 10, before submission (transpose and rotate)

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 31, 2018
"""
import verifier
import sys


def check_func10(file):
    """
    Checks that the test cases are correct
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    func = 'rotate'
    opts = {'right':True}
    result = verifier.grade_docstring(file,0)
    if not result[0]:
        result = verifier.grade_func(file,'transpose',{},0)
    if not result[0]:
        result = verifier.grade_func(file,func,{},0)
    if not result[0]:
        result = verifier.grade_func(file,func,opts,0)
    if not result[0]:
        print("The 'transpose' and 'rotate' operations look correct.")
    return result[0]


if __name__ == '__main__':
    sys.exit(check_func10('plugins.py'))
