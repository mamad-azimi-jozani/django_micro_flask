import socket
import time



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        s.connect(('db', 3306))
        s.close()
        break
    except socket.error as ex:
        time.sleep(0.1)