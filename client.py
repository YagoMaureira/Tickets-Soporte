import sys
import json
from client_functions import *


if __name__ == '__main__':
    client_socket = create_client_socket()
    while True:

        sys.stdout.flush()
        sys.stdin.flush()
        print("""
        ***** Menu *****
        -i / --insertar -> Para insertar nuevo ticket
        -l / --listar -> Para listar todos los tickets
        -f / --filtrar -> Para obtener lista filtrada de tickets
        -e / --editar -> Para editar ticket
        -q / --quit -> Para cerrar programa 
        
        """)
        option = input("Ingrese su opcion: ")
        client_socket.send(option.encode())
        if option in ["-i", "--insertar"]:
            print("Funcion de insertar")
            ticket_json = create_ticket()
            client_socket.send(ticket_json.encode())

        elif option in ["-l", "--listar"]:
            json_ticket_list = client_socket.recv(2048).decode('utf-8')
            json_ticket_list = json.loads(json_ticket_list)
            print("\n Listado de Tickets".center(40, '*'))
            print(json_ticket_list)
            print(type(json_ticket_list))
            for ticket in json_ticket_list:
                print(ticket)

        elif option in ["-f", "--filtrar"]:
            filter_values_dict = filter_ticket_list()
            client_socket.send(filter_values_dict.encode())

            filtered_tickets = client_socket.recv(1024).decode()
            filtered_tickets = json.loads(filtered_tickets)
            print("Lista de tickets filtrados".center(40, '*'))
            print(filtered_tickets)

        elif option in ["-e", "--editar"]:
            print("\n Funcion de editar ticket")
            id_ticket = input("Ingrese el id del ticket que quiere editar: ")
            client_socket.send(id_ticket.encode())
            ticket_to_edit = client_socket.recv(1024).decode()
            ticket_to_edit = json.loads(ticket_to_edit)
            print(ticket_to_edit)
            print(type(ticket_to_edit))
            edited_ticket = edit_ticket(ticket_to_edit)
            print(type(edited_ticket), edited_ticket)
            client_socket.send(edited_ticket.encode())

        elif option in ["-q", "--quit"]:
            break

        else:
            print("Opción invalida, pruebe de nuevo..")
    client_socket.close()
