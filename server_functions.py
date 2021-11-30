import socket

def create_server_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    port = int(input("Ingrese el numero de puerto: "))
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Socket iniciado exitosamente!!")

    return server_socket
