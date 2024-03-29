import numpy
import math 

def iniciarValores():
    while True:
        print("Digite o extremo A do intervalo: ")
        a = float(input())
        print("Digite o extremo B do intervalo: ")
        b = float(input())
        print("Digite a precisão da busca, por exemplo, no formato (0.001): ")
        e = float(input())
        if f(a) * f(b) < 0:
            return a, b, e
        else:
            print("Não existe raíz no intervalo dado!")
 
def calcularNumIteracoes(extremoA, extremoB, precisao):
    k = (numpy.log(extremoB - extremoA) - numpy.log(precisao))/numpy.log(2)
    k = math.ceil(k) #arredonda para o teto
    print("Será preciso de " + str(k) + " iterações para encontrar a raíz.")
    return k #retorna a quantidade de iterações

#x³-9x+3 intervalo [0,1] e precisão = 0.001
def f(x):
    return  x**3 - 9 * x + 3

def iterar(extremoA, extremoB, precisao, iteracoes):
    pMedio = 0
    for contador in range(iteracoes+1):
        print("Iteração: " + str(contador))
        if extremoB - extremoA < precisao:
            print("Precisão alcançada, retornando ponto médio do intervalo: " + str((extremoB+extremoA)/2))
            return (extremoB+extremoA)/2
        else:
            pMedio = (extremoB+extremoA)/2
            if f(extremoA)*f(pMedio) < 0:
                extremoB = pMedio
            if f(pMedio)*f(extremoB) < 0:
                extremoA = pMedio
    print("Zero da função não encontrado.")

A, B, E = iniciarValores()
K = calcularNumIteracoes(A, B ,E)
resultado = iterar(A, B , E, K)