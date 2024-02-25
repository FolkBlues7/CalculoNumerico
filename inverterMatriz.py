"""
Essa função recebe uma matriz a inverte com base no número de linhas e colunas que a mesma apresenta.
Exemplo de matriz que ela recebe:
A = [[1, 2, 3],
     [5, 6, 2],
    [10, 5, 1]]
Então a função vai criar uma outra matriz com linhas e colunas invertidas e vai preencher os valores e retorna-los
como uma outra matriz.
"""

#recebe uma matriz e a inverte
def inverterMatriz(A):
    #pega o número de objeto da coleção, ou seja, as linhas.
    linhas = len(A)
    #pega o número de objetos da primeira lista da coleção, ou seja, as colunas
    colunas = len(A[0])
    #inverte a matriz
    matriz_invertida = [[A[j][i] for j in range(linhas)] for i in range(colunas)]
    #retorna a matriz invertida
    return matriz_invertida