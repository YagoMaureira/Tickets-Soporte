import socket
import json


def create_client_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = input("Ingrese el host: ")
    port = int(input("Ingrese el puerto al que desea conectarse: "))

    client_socket.connect((host, port))
    print(f"socket conectado al host {host} en el puerto {port}")
    return client_socket


def create_ticket():
    print("Ingrese los datos del ticket".center(40, "*"))
    ticket_title = input("Ingrese el titulo: ")
    ticket_author = input("Ingrese el autor: ")
    ticket_description = input("Ingrese la descripcion: ")

    ticket = {"title": ticket_title, "author": ticket_author, "description": ticket_description}
    ticket_json = json.dumps(ticket)
    print(type(ticket_json))
    return ticket_json
