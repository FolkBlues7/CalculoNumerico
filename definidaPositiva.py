#essa função retorna se uma matriz é definida positiva, ou não. Funciona apenas para matrizes quadradas.
#exmeplo de matriz definida positiva
A = [[1, 2, 3],
     [5, 5, 2],
    [10, 5, 2]]
#exemplo de matriz não definida positiva
B = [[1, 2, 3],
     [5, -5, 2],
    [10, 5, -2]]

def verficarDefinidaPositiva(A):
    linha = len(A)
    determinante = 1 #sempre que for fazer um produtório, inicie a variável inicial com 1
    for i in range(linha):
        determinante *= A[i][i]
        if determinante <= 0:
            return False
    return True    

x = verficarDefinidaPositiva(A)
print(x)   
x = verficarDefinidaPositiva(B)
print(x)    
