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
        -x / --exportar -> Para exportar una lista completa o filtrada
        -q / --quit -> Para cerrar programa 
        
        """)
        option = input("Ingrese su opcion: ")
        client_socket.send(option.encode())
        if option in ["-i", "--insertar"]:
            create_ticket(client_socket)

        elif option in ["-l", "--listar"]:
            list_tickets(client_socket)

        elif option in ["-f", "--filtrar"]:
            filter_values_dict = filter_ticket_list()
            client_socket.send(filter_values_dict.encode())

            filtered_tickets = client_socket.recv(1024).decode()
            filtered_tickets = json.loads(filtered_tickets)
            print("\n**** Lista de tickets filtrados ****")
            for ticket in filtered_tickets:
                print(f"\n{ticket}")

        elif option in ["-e", "--editar"]:
            print("\n Funcion de editar ticket")
            id_ticket = input("Ingrese el id del ticket que quiere editar: ")
            client_socket.send(id_ticket.encode())
            ticket_to_edit = client_socket.recv(1024).decode()
            ticket_to_edit = json.loads(ticket_to_edit)
            print("\nEl siguiente Ticket va ser editado\n", ticket_to_edit)
            edited_ticket = edit_ticket(ticket_to_edit)
            print("\nTicket editado\n", edited_ticket)
            client_socket.send(edited_ticket.encode())

        elif option in ["-x", "--exportar"]:
            export_tickets(client_socket)

        elif option in ["-q", "--quit"]:
            client_socket.close()
            break

        else:
            print("Opción invalida, pruebe de nuevo..")
