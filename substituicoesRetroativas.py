#uma lista de listas, uma matríz
A = [[3, 1, 0],
      [0, 3, 4],
      [0, 0, 7/9]]
#um vetor
b = [4, 3, 0]     

#cria uma lista de mesma dimensões de A com valores zero
def substituicaoRetroativa(A, b):
   n = len(A)
   x = n * [0]
   for i in range(n-1, -1, -1):
      S = 0 #sempre que for fazer um somatório, inicie a variável!
      for j in range(i+1, n):
         S = S + A[i][j] * x[j]
      x[i] = (b[i] - S)/A[i][i]

substituicaoRetroativa(A, b)

