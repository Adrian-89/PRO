from __future__ import annotations


class Fraction:
    def __init__(self, num: int, den: int):
        self.gcd_val = self._gcd(num, den)
        self.num = num // self.gcd_val
        self.den = den // self.gcd_val

    def __add__(self, other: Fraction):
        if isinstance(other, Fraction):
            result_num = self.num * other.den + self.den * other.num
            result_den = self.den * other.den
            return Fraction(result_num, result_den)

    def __sub__(self, other: Fraction):
        if isinstance(other, Fraction):
            result_num = self.num * other.den - self.den * other.num
            result_den = self.den * other.den
            return Fraction(result_num, result_den)

    def __mul__(self, other: Fraction):
        if isinstance(other, Fraction):
            result_num = self.num * other.num
            result_den = self.den * other.den
            return Fraction(result_num, result_den)

    def __truediv__(self, other: Fraction):
        if isinstance(other, Fraction):
            result_num = self.num * other.den
            result_den = self.den * other.num
            return Fraction(result_num, result_den)

    def __str__(self):
        return f"The fraction is:: {self.num}/{self.den}"

    @staticmethod
    def _gcd(a: int, b: int) -> int:
        '''Euclid's Algorithm'''
        while b > 0:
            a, b = b, a % b
        return a
