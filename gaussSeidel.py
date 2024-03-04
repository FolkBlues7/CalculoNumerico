from normaVetores import norma

def seidel(A, b, epsilon, iterMax=50):
    n = len(A)
    x = n * [0]

    for i in range(n):
        for j in range(n):
            if i != j:
                A[i][j] = A[i][j] / A[i][i]
        b[i] = b[i] / A[i][i]

    for k in range(iterMax):
        v = x[:]  # Copia o vetor x atual para v
        for i in range(n):
            S = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x[i] = b[i] - S
        d = norma(x, v)
        if d <= epsilon:
            return x

    print("Número máximo de iterações alcançado")
    return x

A = [[5, 1, 1],
     [3, 4, 1],
     [3, 3, 6]]
b = [5, 6, 0]
eps = 0.05
x = seidel(A, b, eps)
print(x)
