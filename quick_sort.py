# -*- coding: utf-8 -*-

def quick_sort(lst, p, r):
    """ 快速排序"""
    if p < r:
        q = partition(lst, p, r)
        quick_sort(lst, p, q-1)
        quick_sort(lst, q+1, r)


def partition(lst, p, r):
    """切分lst"""
    x = lst[r]
    i = p - 1
    for j in xrange(p, r):
        if lst[j] < x:
            i += 1
            if i != j:
                lst[j], lst[i] = lst[i], lst[j]
    q = i + 1
    lst[q], lst[r] = lst[r], lst[q]
    return q


def test_partition():
    lst = [2, 8, 7, 1, 3, 5, 6, 4]
    lst = [2, 1]
    p , r = 0, len(lst)-1
    q = partition(lst, p, r)
    print q, lst


def test_quick_sort():
    lst = [2, 8, 7, 1, 3, 5, 6, 4]
    quick_sort(lst, 0, len(lst)-1)
    print lst


if __name__ == "__main__":
    test_partition()
    test_quick_sort()
