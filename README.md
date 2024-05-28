# Serveur et Clients TCP avec Timeout

Ce projet contient une implémentation simple d'un serveur et de deux clients qui communiquent via TCP. Le serveur ferme automatiquement la connexion avec un client si aucune activité n'est détectée pendant 10 secondes.

## Fonctionnalités

- Serveur TCP qui écoute les connexions entrantes.
- Deux clients (Client 1 et Client 2) qui peuvent envoyer des messages au serveur.
- Le serveur ferme les connexions après 10 secondes d'inactivité.

## Serveur

Le serveur est implémenté en Python et utilise les sockets avec un mécanisme de timeout pour gérer l'inactivité.

 - Écoute sur localhost et un port spécifique.
 - Accepte une connexion.
 - Lit les données envoyées par le client et les renvoie (comportement d'écho).

```python
# Code du serveur ici
import socket
import select
import time

def server():
    host = '127.0.0.1'
    port = 12345
    ...
```

Le serveur utilise maintenant select pour gérer plusieurs connexions de manière non bloquante.

## Les clients 

Les clients fonctionnent comme suit : 

```python

def client():
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Client 1 connecté au serveur.")
        s.sendall(b'Hello, server! from Client 1')
        data = s.recv(1024)
        print(f"Client 1 reçu: {data.decode()}")
```
Chaque client se connecte au serveur et envoie un message identifié. Le serveur écoute tous les clients connectés et répond à chacun d'eux individuellement, en indiquant explicitement à quel client il parle. 
Vous pouvez lancer le serveur d'abord, puis ouvrir deux terminaux distincts pour chaque client pour voir le système en action.
