import sys
from client_functions import create_client_socket


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

        if option == "-i" or "--insertar":
            # Funcion de insertar
            print("Funcion de insertar")
        elif option == "-l" or "--listar":
            # Funcion de listar
            print("Funcion de listar")
        elif option == "-e" or "--editar":
            # Funcion de editar
            print("Funcion de editar")
        elif option == "-q" or "--quit":
            sys.exit(0)
        else:
            print("Opción invalida, pruebe de nuevo..")
