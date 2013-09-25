# -*- coding: utf-8 -*-

"""
checkerboard problem
"""

def cover(board, lab=1, top=0, left=0, side=None):
    print "paras:", lab, top, left, side
    if side is None:
        side = len(board)
    s = side // 2
    offsets = (0, -1), (side-1, 0)
    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            print "out", dy_outer, dy_inner
            print "in", dx_outer, dx_inner
            if not board[top+dy_outer][left+dx_outer]:
                print "a", top+dy_outer, left+dx_outer
                print "b", top+s+dy_inner, left+s+dx_inner
                print "xx", top+s+dy_inner, left+s+dx_inner, lab
                board[top+s+dy_inner][left+s+dx_inner] = lab
                print board
    print "==>"
    for row in board:
        print "%2i  "*8 %tuple(row)

    lab += 1
    if s > 1:
        for dy in [0, s]:
            for dx in [0, s]:
                print "dy,dx", dy, dx
                lab = cover(board, lab, top+dy, left+dx, s)

    return lab



def ins_sort_rec(seq, i):
    if i == 0:
        return
    ins_sort_rec(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    return


def sel_sort_rec(seq, i):
    if i == 0:
        return
    max_j = i
    for j in xrange(i):
        if seq[j] > seq[max_j]:
            max_j = j
    seq[i], seq[max_j] = seq[max_j], seq[i]
    sel_sort_rec(seq, i-1)


def sel_sort(seq):
    for i in xrange(len(seq)-1, 0, -1):
        max_j = i
        for j in xrange(i):
            if seq[j] > seq[max_j]:
                max_j = j
        seq[i], seq[max_j] = seq[max_j], seq[i]


def max_perm_rec(seq, peop=None):
    """p81 maximum permutation problem"""
    if peop is None:
        peop = set(range(len(seq)))
    if len(peop) == 1:
        return
    t = 0
    for p in peop - set(seq):
        if seq[p]:
            seq[p] = None
            t = 1
    if t:
        max_prem(seq, peop)


def max_perm(seq, peop=None):
    """p81 maximum permutation problem"""
    if peop is None:
        peop = set(range(len(seq)))
    if len(peop) == 1:
        return
    t = 1
    while t:
        t = 0
        for p in peop - set(seq):
            if seq[p]:
                seq[p] = None
                t = 1

def max_perm_book(M):
    n = len(M)
    A = set(range(n))
    count = [0] * n
    for i in M:
        count[i] += 1
    Q = [i for i in A if count[i] == 0]
    while Q:
        i = Q.pop()
        A.remove(i)
        j = M[i]
        count[j] -= 1
        if count[j] == 0:
            Q.append(j)
    return A

def test_max_perm():
    seq = [2, 2, 0, 5, 3, 5, 7, 4]
    # seq = [2, ]
    # max_prem_rec(seq)
    # max_perm(seq)
    print max_perm_book(seq)
    print seq


def counting_sort(A, key=lambda x: x):
    from collections import defaultdict
    B, C = [], defaultdict(list)
    for x in A:
        C[key(x)].append(x)
    print C
    for k in range(min(C), max(C)+1):
        print k, C[k]
        B.extend(C[k])
    return B

def test_counting_sort():
    A = [2,3,1,5,7,2]
    print counting_sort(A)


def celeb(G):
    """celebrity problem """
    n = len(G)
    u, v = 0, 1
    for c in range(2, n+1):
        if G[u][v]:
            u = c
        else:
            v = c
    if u == n:
        c = v
    else:
        c = u
    for v in range(n):
        if c == v:
            continue
        if G[c][v]:
            break
        if not G[v][c]:
            break
    else:
        return c
    return None


def test_celeb():
    from random import randrange
    n = 100
    G = [[randrange(2) for i in range(n)] for i in range(n)]
    c = randrange(n)
    for i in range(n):
        G[i][c] = True
        G[c][i] = False
    print celeb(G)


def naive_topsort(G, S=None):
    """图排序"""
    if S is None:
        S = set(G)
    if len(S) == 1:
        return list(S)
    v = S.pop()
    seq = naive_topsort(G, S)
    min_i = 0
    for i, u in enumerate(seq):
        if v in G[u]:
            min_i = i + 1
    seq.insert(min_i, v)
    return seq


def test_naive_topsort():
    G = {"a": ("b", "f"),
         "b": ('c', 'd', 'f'),
         "c": ('d',),
         "d": ('e', 'f'),
         "e": ('f',),
         "f": (),
         }
    print naive_topsort(G)


def fibrec(n):
    if n < 2:
        return n
    return fibrec(n-1) + fibrec(n-2)


def fibtailrec(n, acc1, acc2):
    if n == 0:
        return acc1
    return fibtailrec(n - 1, acc2, acc1 + acc2)


def test_fibrec():
    print fibrec(7)
    print fibtailrec(7, 0, 1)

if __name__ == "__main__":
    # test_max_perm()
    # test_counting_sort()
    # test_celeb()
    # test_naive_topsort()
    test_fibrec()
