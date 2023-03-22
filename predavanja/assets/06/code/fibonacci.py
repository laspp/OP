"""Fibonaccijevo zaporedje
Zaporedje, v katerem je vsak člen vsota prejšnjih dveh:
Fn = F_n-2 + F_n-1
"""

# Koliko členov izpišemo
n = 100

# Začetne vrednosti za prva dva člena
# V splošnem začnemo z 0, 1
# Fibonacci je začel z 1, 2
F_2prej = 1  # dve števili nazaj od trenutnega
F_1prej = 2  # eno število nazaj od trenutnega

for i in range(n):
    print(F_2prej)
    Fn = F_2prej + F_1prej
    F_2prej = F_1prej
    F_1prej = Fn
    
    