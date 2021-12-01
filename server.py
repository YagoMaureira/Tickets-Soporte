import socket
from server_functions import create_server_socket, insert_ticket, list_tickets
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

        if option.decode() == "-q" or option.decode() == "--quit":
            print("Cerrando conexion con cliente")
            conn.close()
            print("Cerrando socket server..")
            server_socket.close()
            break
    break



