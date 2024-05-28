#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:15:57 2024

@author: dorvaldecelestinmobendza
"""

# client2 

import socket

def client():
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Client 2 connecté au serveur.")
        s.sendall(b'Hello, server! from Client 2')
        data = s.recv(1024)
        print(f"Client 2 reçu: {data.decode()}")

if __name__ == "__main__":
    client()
