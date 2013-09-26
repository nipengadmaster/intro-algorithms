# -*- coding: utf-8 -*-

import numpy as np

INF = float('inf')

def young_insert(array, x):
    """
    将x插入young矩阵array中
    """
    n, m = array.shape
    b = array < INF
    n_lst = b.sum()
    i = n_lst // m
    j = n_lst % m
    array[i][j] = x
    while 1:
        up = array[i-1][j] if i > 0 else -INF
        lft = array[i][j-1] if j > 0 else -INF
        if up > x and up > lft:
            array[i-1][j] = x
            array[i][j] = up
            i = i - 1
        elif j > 0 and lft > x and lft > up:
            array[i][j-1] = x
            array[i][j] = lft
            j = j - 1
        else:
            break


def young_tab(lst, n, m):
    """将lst做成n*m的young矩阵"""
    array = np.array([INF] * (n*m))
    array.resize(n, m)
    for x in lst:
        young_insert(array, x)
    return array


def test_young_insert():
    x = 2
    n, m = 5, 6
    lst = [1, 3, 5, 7, 8, 11,
           4, 6, 9, 14, 15, 19,
           10, 21, 23, 33, 56, 57,
           34, 37, 45, 55,]
    n_lst = len(lst)
    array = np.array(lst + [INF,] * (n*m-n_lst))
    array.resize(5, 6)
    young_insert(array, x)
    print array

def test_young_tab():
    lst = [9, 16, 3, 2, 4, 8, 5, 14, 12,]
    array = young_tab(lst, 4, 4)
    print array

if __name__ == "__main__":
    test_young_insert()
    test_young_tab()
