
# Uma lista de listas, uma matriz triangular inferior
A = [[2, 0, 0, 0],
      [3, 5, 0, 0],
      [1, -6, 8, 0],
      [-1, 4, -3, 9]]
b = [4, 1, 48, 6]

# Retorna o número de objetos em um container
def substituicoesSucessivas(A, b):
    n = len(A)
    x = n * [0]
    for i in range(n):
        S = 0
        for j in range(i):
            S += A[i][j] * x[j]
        x[i] = (b[i] - S) / A[i][i]
    print("Resultado: ")
    print(x)

substituicoesSucessivas(A, b)

