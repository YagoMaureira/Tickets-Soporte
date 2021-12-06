import socket
from server_functions import *
import json


server_socket = create_server_socket()


while True:

    conn, addr = server_socket.accept()
    print(f"Conexión establecida - Cliente {addr[0]} | {addr[1]}")
    server_history(addr[0], "Conexion iniciada")

    while True:
        option = conn.recv(1024)
        print(f"\n opcion recibida de cliente: {option.decode()}")

        if option.decode() == "-i" or option.decode() == "--insertar":
            server_history(addr[0], option)
            insert_ticket(conn)

        if option.decode() == "-l" or option.decode() == "--listar":
            server_history(addr[0], option)
            list_tickets(conn)

        if option.decode() == "-f" or option.decode() == "--filtrar":
            server_history(addr[0], option)
            filter_ticket(conn)

        if option.decode() == "-e" or option.decode() == "--editar":
            server_history(addr[0], option)
            id_ticket = conn.recv(1024).decode()
            ticket_json = get_ticket_by_id(id_ticket)
            ticket_json = json.dumps(ticket_json)
            print(type(ticket_json), ticket_json)
            conn.send(ticket_json.encode())

            edit_ticket(conn, id_ticket)

        if option.decode() == "-x" or option.decode() == "--exportar":
            export_option = conn.recv(1024).decode()
            if export_option == "-a":
                list_tickets(conn)
            if export_option == "-b":
                filter_ticket(conn)
            else:
                print("Opcion incorrecta")

        if option.decode() == "-q" or option.decode() == "--quit":
            server_history(addr[0], option)
            print("Cerrando conexion con cliente")
            conn.close()
            print("Cerrando socket server..")
            server_socket.close()
            break
    break
