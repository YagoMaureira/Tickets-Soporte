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


def edit_ticket(ticket_to_edit: dict):
    print("\n Menu de edicion ".center(40, '*'))
    edit_title = input("Desea editar el titulo del ticket? s/n -> ")
    if edit_title == "s":
        title = input("Ingrese el titulo: ")
        ticket_to_edit['title'] = title

    edit_author = input("Desea editar el autor del ticket? s/n -> ")
    if edit_author == "s":
        author = input("Ingrese el autor: ")
        ticket_to_edit['author'] = author

    edit_status = input("Desea editar el estado del ticket? s/n ->")
    if edit_status == "s":
        status = input("Ingrese el estado: ")
        ticket_to_edit['status'] = status

    edit_description = input("Desea editar la descripcion del ticket? s/n ->")
    if edit_description == "s":
        description = input("Ingrese la descripcion: ")
        ticket_to_edit['description'] = description

    return json.dumps(ticket_to_edit)
