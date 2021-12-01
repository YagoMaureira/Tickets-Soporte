import sys
import json
from client_functions import create_client_socket, create_ticket


if __name__ == '__main__':
    client_socket = create_client_socket()
    while True:

        sys.stdout.flush()
        sys.stdin.flush()
        print("""
        ***** Menu *****
        -i / --insertar -> Para insertar nuevo ticket
        -l / --listar -> Para listar tickets
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
            json_ticket_list = client_socket.recv(1024).decode('utf-8')
            json_ticket_list = json.loads(json_ticket_list)
            print("\n Listado de Tickets".center(40, '*'))
            print(json_ticket_list)
            print(type(json_ticket_list))
            for ticket in json_ticket_list:
                print(ticket)

        elif option in ["-e", "--editar"]:
            # Funcion de editar
            print("Funcion de editar")

        elif option in ["-q", "--quit"]:
            break

        else:
            print("Opción invalida, pruebe de nuevo..")
    client_socket.close()
