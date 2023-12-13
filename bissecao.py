import numpy
import math 

print("Digite o extremo A do intervalo: ")
a = float(input())
print("Digite o extremo B do intervalo: ")
b = float(input())
print("Digite a precisão da busca, por exemplo, no formato (0.001): ")
e = float(input())
print(e)

def calcularNumIteracoes(extremoA, extremoB, precisao):
    k = (numpy.log(extremoB - extremoA) - numpy.log(precisao))/numpy.log(2)
    k = math.ceil(k) #arredonda para mais
    print("Será preciso de " + str(k) + " iterações para encontrar a raíz.")

calcularNumIteracoes(a, b, e)