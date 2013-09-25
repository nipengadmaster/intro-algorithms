#-*- coding: utf-8 -*-

def check(a, b):
    """判断两个字符串a,b是不是通过颠倒"""
    a_dict = get_dict(a)
    b_dict = get_dict(b)
    return a_dict == b_dict


def get_dict(a):
    """把字符串a做成dict，value为频次"""
    result = {}
    for sa in a:
        if sa == " ":
            continue
        if sa not in result:
            result[sa] = 1
        else:
            result[sa] += 1
    return result


if __name__ == "__main__":
    a = "bad credit"
    b = "cred bad it"
    print check(a, b)
    print get_dict(a)
    print get_dict(b)
