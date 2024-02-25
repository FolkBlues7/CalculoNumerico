"""
Depende da função inverterMatriz presente no arquivo inverterMatriz.py.
A função verificarSimetria recebe uma matriz e retorna True se ela for simétria ou False, se não.
Exemplo de matriz que ela recebe:
A = [[1, 2, 3],
     [5, 6, 2],
    [10, 5, 1]]
"""

from inverterMatriz import inverterMatriz

#Recebe uma matriz e retorna se ela é simétrica ou não. Leva em conta que a matriz está corretamente definida.
def verificarSimetria(A): 
    #pega o número de objeto da coleção, ou seja, as linhas.
    linhas = len(A)
    #pega o número de objetos da primeira lista da coleção, ou seja, as colunas
    colunas = len(A[0])
    if linhas != colunas:
        print("Erro! As linhas e colunas são diferentes, ou seja, não é uma matriz quadrada. Logo, não pode ser simétrica.")
    #inverte a matriz
    matrizInvertida = inverterMatriz(A)
    for i in range(linhas):
        for j in range(colunas):
            if A[i][j] != matrizInvertida[i][j]:
                return False
    #se mesmo após verificar tudo não detectar nenhuma diferençaa, então ela certamente é simétrica.
    return True

#matriz não simétrica
A = [[1, 2, 3],
     [5, 6, 2],
    [10, 5, 1]]
a = verificarSimetria(A)
print(a)

#matriz simétrica 
B = [[4, 12, -16],
     [12, 37, -43],
     [-16, -43, 98]]
a = verificarSimetria(B)
print(a)

