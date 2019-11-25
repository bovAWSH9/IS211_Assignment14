#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211_Assignment14 - Recursion"""

def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 0
    elif len(s1) == 0:
        return -1
    elif len(s2) == 0:
        return 1

    if s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])
