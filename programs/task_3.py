#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def concatenation(*args):
    if args:
        values = [str(arg) for arg in args]

        string = ""
        for item in values:
            string += item
            
        return string
    else:
        return None


if __name__ == "__main__":
    print(concatenation(1))
    print(concatenation(1,2,3))
    print(concatenation(1,2,3,4,5,6,7,8,9,10))
    print(concatenation())