def fib(n):
    """Izpiše prvih n Fibonaccijevih števil"""
    
    # Začetne vrednosti za prva dva člena
    # V splošnem začnemo z 0, 1
    # Fibonacci je začel z 1, 2
    a = 1  # dve števili nazaj od trenutnega
    b = 2  # eno število nazaj od trenutnega

    for i in range(n):
        print(a)
        (a, b) = (b, a + b)

# Glavni program
n = 100
fib(n)
