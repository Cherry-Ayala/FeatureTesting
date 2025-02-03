def p(a, b):
    if b == 0:
        print("Error: División por cero")
        return None
    else:
        return a / b
    

def f(n):
    if n < 0:
        print("Error: Número negativo")
        return None
    else:
        r = 1
        for i in range(1, n + 1):
            r *= i
        return r

