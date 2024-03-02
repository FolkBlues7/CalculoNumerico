
def norma(v, x):
    n = len(v)
    maxnum = 0
    maxden = 0
    for i in range(0, n):
        num = abs(v[i] - x[i])
        if num > maxnum:
            maxnum = num
        den = abs(v[i])
        if den > maxden:
            maxden = den
    return maxnum/maxden