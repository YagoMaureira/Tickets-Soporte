import socket
from models import Ticket
from datetime import date
from db_config import sessionobj
import json


def create_server_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    port = int(input("Ingrese el numero de puerto: "))
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Socket iniciado exitosamente!!")

    return server_socket


def insert_ticket(dictionary):
    ticket = Ticket(title=dictionary['title'], author=dictionary['author'], description=dictionary['description'],
                    status="pendiente", date=date.today())
    sessionobj.add(ticket)
    sessionobj.commit()


def list_tickets():
    ticket_list = []
    tickets = sessionobj.query(Ticket).all()
    print("Enviando listado de tickets al cliente")
    sessionobj.commit()
    for ob in tickets:
        ticket_list.append(ob.to_json())
    json_tickets = json.dumps(ticket_list)
    return json_tickets
