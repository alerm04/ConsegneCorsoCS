import socket
import time
 
TARGET_IP  = "192.168.56.101"  
TARGET_PORT = 22               
NUM_PACKETS = 10               
DELAY       = 0.5              
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
for i in range(1, NUM_PACKETS + 1):
    messaggio = f"pacchetto #{i}".encode()
    sock.sendto(messaggio, (TARGET_IP, TARGET_PORT))
    print(f"Inviato pacchetto {i} a {TARGET_IP}:{TARGET_PORT}")
    time.sleep(DELAY)
 
sock.close()
print("Fine invio.")