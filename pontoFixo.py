def neverNegative(i):
    if i < 0:
        return i*(-1)
    else:
        return i
#função padrão
def f(x):
    return x**3 - 9*x + 3
#função "fi" de f(x)
def fi(x):
    return x**3/9 + 1/3


def iterar():
    precisao1 = 0.0005
    precisao2 = 0.0005
    x0 = 0.5
    if neverNegative(f(x0)) < precisao1:
        return x0
    k = 1
    while True:
        x1 = fi(x0)
        if neverNegative(f(x1)) < precisao1 or neverNegative(x1 - x0) < precisao2:
            return x1
        x0 = x1
        k = k + 1

print(iterar())

