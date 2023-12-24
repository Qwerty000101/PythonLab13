#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def geometric_mean(*args):
    if args:
        values = [float(arg) for arg in args]

        product = 1
        for item in values:
            product *= item
            
        return product**(1/len(values))
    else:
        return None


if __name__ == "__main__":
    print(geometric_mean(1,2,3))
    print(geometric_mean())
    print(geometric_mean(1))
    print(geometric_mean(10,20,30))