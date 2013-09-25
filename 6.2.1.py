# -*- coding: utf-8 -*-

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def max_heapify(lst, i, n_lst):
    l = left(i)
    r = right(i)
    print i, l, r
    if l <= n_lst and lst[l] > lst[i]:
        largest = l
    else:
        largest = i
    if r <= n_lst and lst[r] > lst[largest]:
        largest = r
    if largest != i:
        print "old", lst
        lst[largest], lst[i] = lst[i], lst[largest]
        print "new", lst
        max_heapify(lst, largest, n_lst)


def max_heapify_iter(lst, i, n_lst):
    while i <= n_lst:
        l = left(i)
        r = right(i)
        print i, l, r
        if l > n_lst:
            break
        if l <= n_lst and lst[l] > lst[i]:
            largest = l
        else:
            largest = i
        if r <= n_lst and lst[r] > lst[largest]:
            largest = r
        if largest != i:
            print "old", lst
            lst[largest], lst[i] = lst[i], lst[largest]
            print "new", lst
            i = largest
    return


def test_max_heapify():
    lst = [0, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    # max_heapify(lst, 2)
    max_heapify_iter(lst, 2)
    print lst


def build_max_heap(A):
    heap_size = len(A) - 1
    for i in xrange((len(A)-1) // 2, 0, -1):
        print i
        max_heapify(A, i, heap_size)


def test_build_max_heap():
    lst = [0, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    build_max_heap(lst)
    print lst


def heapsort(A):
    """ 堆排序 """
    build_max_heap(A)
    for i in xrange(len(A) - 1, 1, -1):
        print "heapsort:", i
        A[1], A[i] = A[i], A[1]
        max_heapify(A, 1, i-1)
    pass


def test_heapsort():
    lst = [0, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heapsort(lst)
    print lst

if __name__ == "__main__":
    # test_max_heapify()
    # test_build_max_heap()
    test_heapsort()
