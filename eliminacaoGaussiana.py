from substituicoesRetroativas import substituicaoRetroativa
A = [[1, -3, 2],
     [-2, 8, -1],
     [4, -6, 5]]

b = [11, -15, 29]

def eliminacaoGauss(A, b):
    n = len(A)
    for k in range (0, n-1):
        for i in range(k+1, n):
            m = - A[i][k]/A[k][k]
            for j in range(k+1, n):
                A[i][j] = m * A[k][j] + A[i][j]
            b[i] = m * b[k] + b[i]
            A[i][k] = 0
    resultado = substituicaoRetroativa(A, b) 
    return resultado

print("Resultado: ")
print(eliminacaoGauss(A, b))


