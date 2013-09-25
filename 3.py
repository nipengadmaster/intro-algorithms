# -*- coding: utf-8 -*-


def compute_power(x, n):
    if n == 1:
        return x
    a = n // 2
    b = n % 2
    half = compute_power(x, a)
    c = x if b else 1
    return half * half * c


def test_compute_power():
    x = 7
    n = 5
    print compute_power(x, n)

if __name__ == "__main__":
    test_compute_power()
