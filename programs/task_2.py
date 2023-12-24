#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def garmonic_mean(*args):
    if args:
        values = [float(arg) for arg in args]

        count = len(values)
        denominator = 0

        for item in values:
            denominator += 1/item

        return count/denominator
    else:
        return None


if __name__ == "__main__":
    print(garmonic_mean(1))
    print(garmonic_mean(1,2,3))
    print(garmonic_mean(1,2,3,4,5,6,7,8,9,10))
    print(garmonic_mean())