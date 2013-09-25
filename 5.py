# -*- coding: utf-8 -*-

def iter_dfs(G, s):
    S, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        Q.extend(G[u])
        yield u


def traverse(G, s, qtype=set):
    S, Q = set(), qtype()
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        for v in G[u]:
            Q.add(v)
        yield u

class stack(list):
    add = list.append

def test_dfs():
    a, b, c, d, e, f, g, h = range(8)
    G = [
        (b, c, d, e,f),
        (c, e),
        (d,),
        (e,),
        (f,),
        (c,g,h),
        (f,h),
        (f,g),
        ]
    r = iter_dfs(G, 0)
    print list(r)
    r = traverse(G, 0, stack)
    print list(r)

if __name__ == "__main__":
    test_dfs()
