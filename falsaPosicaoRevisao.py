def f(x):
    return x**3 - 9*x + 3

def neverNegative(i):
    if i < 0:
        return i*(-1)
    else:
        return i

a = 0
b = 1

x = (a*f(b) - b*f(a))/(f(b) - f(a))

precision1 = 0.005
precision2 = 0.005

if b-a < precision1:
    x = (b+a)/2
else:
    if neverNegative(f(a)) < precision2:
        x = a
    else:
        if neverNegative(f(b)) < precision2:
            x = b
        else:
            cont = 1
            while True:
                x = (a*f(b) - b*f(a))/(f(b) - f(a))
                if neverNegative(f(x)) < precision2:
                    break
                if f(a) * f(x) < 0:
                    b = x
                else:
                    a = x #44444444444
                if b - a < precision1:
                    x = (b+a)/2
                    break
                cont = cont + 1
                
                


print(str(x))


