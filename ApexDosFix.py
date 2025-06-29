import socket
import threading
import time

TARGET_IP = '127.0.0.1'
TARGET_PORT = 8080
NUM_THREADS = 50
DURATION = 99999999999999999999999999999999999999999999999999

def send_packets():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET_IP, TARGET_PORT))
        end_time = time.time() + DURATION
        count = 0
        while time.time() < end_time:
            s.sendall(b"Test packet\n")
            count += 1
        s.close()
        print(f"Packets sent: {count}")
    except Exception as e:
        print(f"Błąd: {e}")

threads = []

for _ in range(NUM_THREADS):
    t = threading.Thread(target=send_packets)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Ended")
