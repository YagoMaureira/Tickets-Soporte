import socket
import json
import csv
import zipfile


def create_client_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = input("Ingrese el host: ")
    port = int(input("Ingrese el puerto al que desea conectarse: "))

    client_socket.connect((host, port))
    print(f"\nsocket conectado al host {host} en el puerto {port}")
    return client_socket


def create_ticket(client_socket):
    print("\n**** Ingrese los datos del ticket ****")
    ticket_title = input("Ingrese el titulo: ")
    ticket_author = input("Ingrese el autor: ")
    ticket_description = input("Ingrese la descripcion: ")

    ticket = {"title": ticket_title, "author": ticket_author, "description": ticket_description}
    ticket_json = json.dumps(ticket)
    client_socket.send(ticket_json.encode())
    server_response = client_socket.recv(1024).decode()
    print(server_response)


def list_tickets(client_socket):
    json_ticket_list = client_socket.recv(4096).decode('utf-8')
    json_ticket_list = json.loads(json_ticket_list)
    print("\n**** Listado de Tickets ****")
    for ticket in json_ticket_list:
        print(f"\n {ticket}")


def edit_ticket(client_socket):
    print("\n Funcion de editar ticket")
    id_ticket = input("Ingrese el id del ticket que quiere editar: ")
    client_socket.send(id_ticket.encode())
    ticket_to_edit = client_socket.recv(1024).decode()
    ticket_to_edit = json.loads(ticket_to_edit)
    print("\nEl siguiente Ticket va ser editado\n", ticket_to_edit)

    print("\n**** Menu de edicion ****")
    edit_title = input("\nDesea editar el titulo del ticket? s/n -> ")
    if edit_title == "s":
        title = input("Ingrese el titulo: ")
        ticket_to_edit['title'] = title

    edit_author = input("\nDesea editar el autor del ticket? s/n -> ")
    if edit_author == "s":
        author = input("Ingrese el autor: ")
        ticket_to_edit['author'] = author

    edit_status = input("\nDesea editar el estado del ticket? s/n -> ")
    if edit_status == "s":
        status = input("Ingrese el estado: ")
        ticket_to_edit['status'] = status

    edit_description = input("\nDesea editar la descripcion del ticket? s/n -> ")
    if edit_description == "s":
        description = input("Ingrese la descripcion: ")
        ticket_to_edit['description'] = description

    print("\nTicket editado\n", ticket_to_edit)
    ticket_edited = json.dumps(ticket_to_edit)
    client_socket.send(ticket_edited.encode())


def filter_ticket_list(client_socket, filter_values_dict):
    filter_values_dict = json.dumps(filter_values_dict)

    client_socket.send(filter_values_dict.encode())

    filtered_tickets = client_socket.recv(2048).decode()
    filtered_tickets = json.loads(filtered_tickets)
    print("\n**** Lista de tickets filtrados ****")
    for ticket in filtered_tickets:
        print(f"\n{ticket}")
    return filtered_tickets


def filter_values_menu():
    filter_values_dict = {}
    author_filter = input("\nDesea filtrar por autor? s/n -> ")
    if author_filter == "s":
        author = input("Ingrese el autor: ")
        filter_values_dict['author'] = author

    status_filter = input("\nDesea filtrar por estado? s/n -> ")
    if status_filter == "s":
        status = input("Ingrese el estado: ")
        filter_values_dict['status'] = status

    date_filter = input("\nDesea filtrar por fecha? s/n -> ")
    if date_filter == "s":
        date = input("Ingrese la fecha en formato yyyy-mm-dd: ")
        filter_values_dict['date'] = date
    return filter_values_dict


def export_tickets(conn, opt, filter_values_dict):

    if opt == "-a":
        ticket_list = conn.recv(4096).decode('utf-8')

    if opt == "-b":
        filter_values_dict = json.dumps(filter_values_dict)
        conn.send(filter_values_dict.encode())
        ticket_list = conn.recv(2048).decode()

    json_ticket_list = json.loads(ticket_list)

    with open("tickets.csv", "w", encoding='utf-8', newline="") as file:
        fc = csv.DictWriter(file, fieldnames=json_ticket_list[0].keys(),)
        fc.writeheader()
        fc.writerows(json_ticket_list)

    ticket_zip = zipfile.ZipFile('tickets.zip', 'w')
    ticket_zip.write('tickets.csv', compress_type=zipfile.ZIP_DEFLATED)
    ticket_zip.close()
