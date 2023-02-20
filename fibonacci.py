def teste1():
    if fibonacci(0) == [0] and fibonacci(-1) == []:
        print("Teste OK")
    else:
        print("Teste Falhou")



def fibonacci(n):
    res = []
    if n < 0:
        return res
    elif n==0:
        res.append(n)
        return res 
    else:
        res=[0,1]
        while (len(res)<n+1):
            res.append(res[-1]+res[-2])
        return res
