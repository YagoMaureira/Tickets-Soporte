from server_functions import *
import json
from threading import Thread
import sys
from multiprocessing import Lock


server_socket = create_server_socket()


def th_server(conn, addr, lock):
    while True:
        option = conn.recv(1024)
        print(f"\n opcion recibida de cliente: {option.decode()}")

        if option.decode() == "-i" or option.decode() == "--insertar":
            server_history(addr[0], option.decode())
            insert_ticket(conn, lock)

        if option.decode() == "-l" or option.decode() == "--listar":
            server_history(addr[0], option.decode())
            list_tickets(conn)

        if option.decode() == "-f" or option.decode() == "--filtrar":
            server_history(addr[0], option.decode())
            filter_ticket(conn)

        if option.decode() == "-e" or option.decode() == "--editar":
            server_history(addr[0], option.decode())

            edit_ticket(conn)

        if option.decode() == "-x" or option.decode() == "--exportar":
            server_history(addr[0], option.decode())
            export_option = conn.recv(1024).decode()
            if export_option == "-a":
                list_tickets(conn)
            if export_option == "-b":
                filter_ticket(conn)
            else:
                print("Opcion incorrecta")

        if option.decode() == "-q" or option.decode() == "--quit":
            server_history(addr[0], option.decode())
            print(f"El cliente {addr[0]} se ha desconectado")
            break


try:
    while True:
        lock = Lock()
        conn, addr = server_socket.accept()

        print(f"\nConexión establecida - Cliente {addr[0]} | {addr[1]}")
        server_history(addr[0], "Conexion iniciada")
        th = Thread(target=th_server, args=(conn, addr, lock,)).start()
except KeyboardInterrupt:
    server_socket.close()
    print("\nSocket de servidor cerrado")
    sys.exit(0)
