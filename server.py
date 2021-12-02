import socket
from server_functions import *
import json


server_socket = create_server_socket()


while True:

    conn, addr = server_socket.accept()
    print(f"Conexión establecida {conn} | {addr}")

    while True:
        option = conn.recv(1024)
        print(f"\n opcion recibida de cliente: {option.decode()}")

        if option.decode() == "-i" or option.decode() == "--insertar":
            ticket = conn.recv(1024).decode()
            ticket_dict = json.loads(ticket)
            insert_ticket(ticket_dict)
            print("Ticket insertado!")

        if option.decode() == "-l" or option.decode() == "--listar":
            json_ticket_list = list_tickets()
            conn.send(json_ticket_list.encode())
            print("\n Se ha enviado el listado de tickets al cliente")

        if option.decode() == "-e" or option.decode() == "--editar":
            id_ticket = conn.recv(1024).decode()
            ticket_json = get_ticket_by_id(id_ticket)
            ticket_json = json.dumps(ticket_json)
            print(type(ticket_json), ticket_json)
            conn.send(ticket_json.encode())
            edited_ticket = conn.recv(1024).decode()
            edited_ticket = json.loads(edited_ticket)
            edit_ticket(edited_ticket, id_ticket)

        if option.decode() == "-q" or option.decode() == "--quit":
            print("Cerrando conexion con cliente")
            conn.close()
            print("Cerrando socket server..")
            server_socket.close()
            break
    break



