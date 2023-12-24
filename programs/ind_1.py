#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def f(*args):
    if args:
        sum = 0
        test_positive = False

        for item in args:
            if float(item) > 0 or test_positive == True:
                if test_positive == False:
                    test_positive = True
                    sum -= float(item)

                sum += float(item)

        #Eсли нет положительных аргументов, то функция возвращает None
        if test_positive == False:
            return None
        
        else:
            return sum
    else:
        return None


if __name__ == "__main__":
    print(f(-1, -2, -3))
    print(f())
    print(f(-1, -2, 3))
    print(f(-1,-2, 3, 4, 5, 6, 7))
    print(f(1, 2, 3))
