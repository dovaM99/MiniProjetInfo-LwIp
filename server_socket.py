#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:09:25 2024

@author: dorvaldecelestinmobendza
"""
# script serveur

import socket
import select
import time

def server():
    host = '127.0.0.1'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Serveur démarré, en écoute sur {host}:{port}")

    # Liste des sockets pour select
    sockets_list = [server_socket]
    clients = {}  # Dictionnaire pour suivre les adresses clients

    # Dictionnaire pour suivre les derniers temps d'activité des clients
    last_active = {}

    while True:
        # Utilisation de select avec un timeout pour vérifier l'activité
        read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list, 10)

        if not read_sockets:  # Aucune activité dans les 10 dernières secondes
            for client_socket in list(clients):
                # Vérifie l'heure de la dernière activité
                if time.time() - last_active.get(client_socket, 0) > 10:
                    print(f"Temps d'inactivité dépassé pour {clients[client_socket]}")
                    sockets_list.remove(client_socket)
                    del clients[client_socket]
                    client_socket.close()

        for notified_socket in read_sockets:
            if notified_socket == server_socket:
                # Nouvelle connexion
                client_socket, client_address = server_socket.accept()
                sockets_list.append(client_socket)
                clients[client_socket] = client_address
                last_active[client_socket] = time.time()
                print(f"Connexion acceptée de {client_address}")
            else:
                # Recevoir des messages des clients
                message = notified_socket.recv(1024)
                if not message:
                    print(f"Fermé la connexion de {clients[notified_socket]}")
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    notified_socket.close()
                    continue

                last_active[notified_socket] = time.time()
                client_id = "Client 1" if clients[notified_socket] == clients[sockets_list[1]] else "Client 2"
                print(f"Reçu de {client_id}: {message.decode()}")
                response_message = f"Bonjour {client_id}, j'ai bien reçu votre message: {message.decode()}"
                notified_socket.send(response_message.encode())

        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            del clients[notified_socket]
            notified_socket.close()

if __name__ == "__main__":
    server()

