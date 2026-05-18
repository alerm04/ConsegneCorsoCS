def lunghezza_parole(A):
    B = []
    for parola in A:
        B.append(len(parola))
    return B

n = int(input("Quante parole vuoi inserire? "))
A = []
for i in range(n):
    parola = input(f"Inserisci la parola {i+1}: ")
    A.append(parola)

B = lunghezza_parole(A)
print("Lista lunghezze:", B)