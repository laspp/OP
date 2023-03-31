# Fibonaccijevo zaporedje

n = int(input('Vnesi n: '))

Fn_2 = 1
Fn_1 = 2
for i in range(n):
    print(Fn_2)
    Fn = Fn_2 + Fn_1
    Fn_2 = Fn_1
    Fn_1 = Fn
    
    