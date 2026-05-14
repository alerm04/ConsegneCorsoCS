import math

print("=== Calcolatore Geometrico ===\n")

valore = float(input("Inserisci il valore iniziale: "))
figure_rimanenti = ["Quadrato", "Cerchio", "Rettangolo"]

for turno in range(3):
    print(f"\n--- Turno {turno + 1} ---")
    print(f"Valore corrente: {valore}")
    
    for i, figura in enumerate(figure_rimanenti):
        print(f"  {i + 1}. {figura}")
    
    scelta = int(input("Scegli una figura (numero): ")) - 1
    figura_scelta = figure_rimanenti.pop(scelta)

    if figura_scelta == "Quadrato":
        perimetro = valore * 4
        area = valore ** 2
        print(f"Quadrato → lato={valore}, perimetro={round(perimetro,2)}, area={round(area,2)}")

    elif figura_scelta == "Cerchio":
        perimetro = 2 * math.pi * valore
        area = math.pi * valore ** 2
        print(f"Cerchio → raggio={valore}, perimetro={round(perimetro,2)}, area={round(area,2)}")

    elif figura_scelta == "Rettangolo":
        altezza = valore / 2
        perimetro = valore * 2 + altezza * 2
        area = valore * altezza
        print(f"Rettangolo → base={valore}, altezza={altezza}, perimetro={round(perimetro,2)}, area={round(area,2)}")

    valore = area

print("\n=== Fine ===")