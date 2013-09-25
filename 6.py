# -*- coding: utf-8-*-

class Node:
    lft = None
    rgt = None
    def __init__(self, key, val):
        self.key = key
        self.val = val

def insert(node, key, val):
    if node is None:
        return Node(key, val)
    if node.key == key:
        node.val = val
    elif key > node.key:
        node.rgt = insert(node.rgt, key, val)
    else:
        node.lft = insert(node.lft, key, val)
    return node

def search(node, key):
    if node is None:
        raise KeyError
    if node.key == key:
        return node.val
    if key > node.key:
        return search(node.rgt, key)
    else:
        return search(node.lft, key)


class Tree():
    root = None
    def __setitem__(self, key, val):
        self.root = insert(self.root, key, val)
    def __getitem__(self, key):
        return search(self.root, key)
    def __contains__(self, key):
        try:
            search(self.root, key)
        except KeyError:
            return False
        return True


def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi


def select(seq, k):
    lo, pi, hi = partition(seq)
    print lo, pi, hi
    m = len(lo)
    if m == k:
        return pi
    if m < k:
        return select(hi, k-m-1)
    if m > k:
        return select(lo, k)


def test_select():
    """ 选取seq的第k个最小元素"""
    seq = [7,1,2,5,3]
    print select(seq, 3)


def quicksort(seq):
    if len(seq) <= 1:
        return seq
    lo, pi, hi = partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi)


def test_quicksort():
    seq = [2,1,7,5,3,8]
    print quicksort(seq)


def naive_closest_pair(seq):
    n = len(seq)
    x = seq[0]
    y = seq[1]
    c = abs(x-y)
    for i in xrange(n):
        for j in xrange(i+1, n):
            if abs(seq[i]-seq[j]) < c:
                x = seq[i]
                y = seq[j]
                c = abs(x-y)
    return x, y


def closest_pair(seq, start, end):
    mid = (end-start) // 2
    n = end - start + 1
    if n == 2:
        return tuple(seq), abs(seq[0]-seq[1])
    if n < 2:
        return None
    lft = closest_pair(seq, start, mid)
    rgt = closest_pair(seq, mid+1, end)
    mc = 0
    mt = None
    if lft:
        mt, mc = lft
    if rgt and rgt[1] < mc:
        mt, mc = rgt
    mt, mc = closest_merge(seq, start, mid, end, mt, mc)
    return mt, mc


def closest_merge(seq, start, mid, end, mt, mc):
    l = seq[start:mid+1]
    l.append(10000)
    r = seq[mid+1:end+1]
    r.append(10000)
    i, j, k = 0, 0, start
    while k < end:
        # if i >= mid - start + 1:
        #     seq[k] = seq[j]
        #     k += 1
        #     continue
        # if j >= end - mid:
        #     seq[k] = seq[i]
        #     k += 1
        #     continue
        if l[i] <= r[j]:
            seq[k] = l[i]
            if abs(l[i]-r[j]) < mc:
                mt = tuple([l[i], r[j]])
                mc = abs(l[i]-r[j])
            i += 1
        else:
            seq[k] = r[j]
            if abs(l[i]-r[j]) < mc:
                mt = tuple([l[i], r[j]])
                mc = abs(l[i]-r[j])
            j += 1
        k += 1
    return mt, mc


def test_closest_pair():
    seq = [2, 11, 100, 50, 4]
    # print naive_closest_pair(seq)
    start = 0
    end = len(seq) - 1
    print closest_pair(seq, start, end)


def merge_sort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = merge_sort(lft)
    if len(rgt) > 1:
        rgt = merge_sort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] > rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


def test_merge_sort():
    seq = [2,5,7,1,3,8]
    print merge_sort(seq)


def repetitions(A, n):
    i = 0
    for i in xrange(n):
        A[A[i]%n] += n
    print A
    for i in xrange(n):
        frq = A[i] // n
        ele = i
        print ele, frq

def count_sort(seq):
    n = len(seq)
    k = max(seq)
    B = [0] * (k+1)
    for i in xrange(n):
        B[seq[i]] += 1
    print "B", B
    j = 0
    for i in xrange(1, k+1):
        if B[i] > 0:
            seq[j] = i
            j += 1
    return seq


def test_count_sort():
    seq = [1, 5, 2, 10, 3, 7, 6, 8, 8]
    print count_sort(seq)


if __name__ == "__main__":
    #test_select()
    #test_quicksort()
    #test_closest_pair()
    #test_merge_sort()
    #repetitions([0,2,2,3,4], 5)
    test_count_sort()
