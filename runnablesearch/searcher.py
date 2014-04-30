#!/usr/bin/env python
# coding=utf-8

import ast
import _ast

def has_main(filepath):
    with open(filepath, 'r') as f:
        source = f.read()

    tree = ast.parse(source)

    first_level_ifs = (n for n in ast.walk(tree) if isinstance(n, _ast.If))

    strs_in_ifs = [n.s for _if in first_level_ifs
                   for n in ast.walk(_if)
                   if isinstance(n, _ast.Str)]

    return '__main__' in strs_in_ifs
