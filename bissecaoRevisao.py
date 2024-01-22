def f(x):
    return x**3 - 9*x + 3

#intervalos
a = 0
b = 1
precision = 0.003
pontoMedio = 0
while (b-a >= precision):
    if b - a < precision:
        pontoMedio = (a+b)/2
        break
    if b - a >= precision:
        pontoMedio = (a+b)/2
    if f(a) * f(pontoMedio) < 0:
        b = pontoMedio
    if f(pontoMedio) * f(b) < 0:
        a = pontoMedio
    pontoMedio = (a+b)/2
 
print("O resultado é: " + str(pontoMedio))
    