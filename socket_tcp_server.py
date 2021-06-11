#!/usr/bin/env python3

import socket

HOST = '192.168.10.12'
PORT = 888

print("Hello","World")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('connected by '+str(addr))

    while True:
        indata = conn.recv(1024)
        if len(indata) == 0:
            conn.close()
            print('client close connection')
            break

        print('recv: '+indata.decode())

        outdata = 'echo '+indata.decode()

        conn.send(outdata.encode())
