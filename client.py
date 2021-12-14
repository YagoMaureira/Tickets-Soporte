import sys
from client_functions import *
from multiprocessing import Process


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
        -q / --quit -> Para finalizar conexion con servidor 
        """)
        option = input("\nIngrese su opcion: ")
        client_socket.send(option.encode())
        if option in ["-i", "--insertar"]:
            create_ticket(client_socket)

        elif option in ["-l", "--listar"]:
            list_tickets(client_socket)

        elif option in ["-f", "--filtrar"]:
            filter_values_dict = filter_values_menu()
            filter_ticket_list(client_socket, filter_values_dict)

        elif option in ["-e", "--editar"]:
            edit_ticket(client_socket)

        elif option in ["-x", "--exportar"]:
            filter_values_dict = {}
            print("\n- Para exportar toda la lista de tickets ingrese -a")
            print("- Para exportar una lista filtrada ingrese -b")
            opt = input("\nIngrese la opcion: ")
            if opt == "-b":
                filter_values_dict = filter_values_menu()

            client_socket.send(opt.encode())

            export_process = Process(target=export_tickets, args=(client_socket, opt, filter_values_dict))
            export_process.start()
            export_process.join()

        elif option in ["-q", "--quit"]:
            client_socket.close()
            break

        else:
            print("Opción invalida, pruebe de nuevo..")
