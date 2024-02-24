#uma lista de listas, uma matríz
A = [[5, -2, 6, 1],
      [0, 3, 7, -4],
      [0, 0, 4, 5],
      [0, 0, 0, 2]]
#um vetor
b = [1, -2, 28, 8]

#retorna o número de objetos em um container
n = len(A)

#cria uma lista de mesma dimensões de A com valores zero
x = n * [0]

for i in range(n-1, -1, -1):
   S = 0 #sempre que for fazer um somatório, inicie a variável!
   for j in range(i+1, n):
      S = S + A[i][j] * x[j]
   x[i] = (b[i] - S)/A[i][i]

print(x)