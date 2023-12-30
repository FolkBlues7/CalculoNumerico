#x³ - 9x + 3 DEFINA A FUNÇÃO AQUI!
def f(x):
    return x**3 - (9*x) + 3

def neverNegative(i):
    if i < 0:
        return i*(-1)
    else:
        return i

def calcularX(a, b):
    return (a*f(b)-b*f(a))/(f(b)-f(a))

a = 0
b = 1
precisao1 = 0.0005
precisao2 = 0.0005

def iterar(a,b):
    while True:
        x = calcularX(a, b)
        if b-a < precisao1:
            return (a*b)/2
        if neverNegative(f(x)) < precisao1:
            return x
        if f(a)*f(x) < 0:
            b = x
        if f(b)*f(x) < 0:
            a = x

resultado = iterar(a,b)
print(resultado)
