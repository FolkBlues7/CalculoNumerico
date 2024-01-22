#defina a função f(x) aqui:
def f(x):
    return x**3 - 9*x +3
#defina a derivadaa f'(x) aqui:
def fI(x):
    return 3*x**2 - 9
#essa é a função FI padrão
def fi(x0):
    x1 = x0 - (f(x0)/fI(x0))
    return x1
#serve para garantir valores positivos, funciona como o móduo |X|
def neverNegative(i):
    if i < 0:
        return i*(-1)
    else:
        return i
#inicialização de intervalo e precisão
x0 = 0.5
precision1 = 0.004
precision2 = 0.004
resultado = 0
#iterações do método de Newton
if neverNegative(f(x0)) < precision1:
    resultado = x0
else:
    contador = 1
    while True:
        x1 = fi(x0)
        if neverNegative(f(x1)) < precision1 or neverNegative(x1 - x0) < precision2:
            resultado = x1
            break
        x0 = x1
        contador = contador + 1

print(resultado)

