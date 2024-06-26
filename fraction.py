from __future__ import annotations


class Fraction:
    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den
        self

    def __add__(self, other: Fraction):
        if isinstance(other, Fraction):
            return self.den + Fraction.num

    def __sub__(self, other: Fraction):
        if isinstance(other, Fraction):
            return self.den - Fraction.num

    def __mul__(self, other: Fraction):
        if isinstance(other, Fraction):

    def __truediv__(self, other: Fraction):
        ...

    def __str__(self):
        ...

    @staticmethod
    def gcd(a: int, b: int) -> int:
        '''Euclid's Algorithm'''
        while b > 0:
            a, b = b, a % b
        return a
