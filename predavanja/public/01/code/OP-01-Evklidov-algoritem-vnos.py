A = int(input("Vpiši A:"))
B = int(input("Vpiši B:"))
while A != B:
    if A > B:
        A = A - B
    else:
        B = B - A
print("Največji skupni delitelj števil", A, "in", B, "je: ", A)