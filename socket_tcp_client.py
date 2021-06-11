#!/usr/bin/env python3

import socket

print("Hello","World")

HOST = '192.168.10.12'
PORT = 888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    outdata = input('Plz input message: ')
    print('send: '+outdata)
    s.send(outdata.encode())

    indata = s.recv(1024)
    if len(indata) == 0:
        s.close()
        print('Server close connection')
        break

    print('recv: '+indata.decode())
