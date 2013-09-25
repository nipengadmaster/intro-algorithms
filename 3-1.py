#-*- coding: utf-8 -*-

"""
在计算机科学中，Bogo排序（bogo-sort）是个既不实用又原始的排序算法，其原理等同将一堆卡片抛起，落在桌上后检查卡片是否已整齐排列好，若非就再抛一次。其名字源自Quantum bogodynamics，又称bozo sort、blort sort或猴子排序（参见无限猴子定理）。
"""

from random import shuffle
from itertools import izip, tee


def in_order(my_list):
    """Check if my_list is ordered"""
    it1, it2 = tee(my_list)
    it2.next()
    return all(a<=b for a,b in izip(it1, it2))


def bogo_sort(my_list):
    """Bogo-sorts my_list in place."""
    while not in_order(my_list):
        print "shuffle"
        shuffle(my_list)


def gnome_sort(seq):
    """Gnome sort """
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i-1], seq[i] = seq[i], seq[i-1]
            i -= 1
    return seq


def merge_sort(seq):
    """合并排序 """
    mid = len(seq) // 2
    lft = seq[:mid]
    rgt = seq[mid:]
    if len(lft) > 1:
        lft = merge_sort(lft)
    if len(rgt) > 1:
        rgt = merge_sort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


if __name__ == "__main__":
    seq = [2,4,1,5,3]
    # bogo_sort(seq)
    # print gnome_sort(seq)
    result = merge_sort(seq)
    print result
