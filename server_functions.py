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


def insert_ticket(conn):
    ticket = conn.recv(1024).decode()
    ticket_dict = json.loads(ticket)

    ticket = Ticket(title=ticket_dict['title'], author=ticket_dict['author'], description=ticket_dict['description'],
                    status="pendiente", date=date.today())
    sessionobj.add(ticket)
    sessionobj.commit()
    print("\n Ticket insertado!")


def list_tickets(conn):
    ticket_list = []
    tickets = sessionobj.query(Ticket).all()
    print("Enviando listado de tickets al cliente")
    sessionobj.commit()
    for ob in tickets:
        ticket_list.append(ob.to_json())

    print(ticket_list)
    json_tickets = json.dumps(ticket_list)

    conn.send(json_tickets.encode())
    print("\n Se ha enviado el listado de tickets al cliente")


def get_ticket_by_id(id_ticket):
    ticket = sessionobj.query(Ticket).get(int(id_ticket))
    return ticket.to_json()


def edit_ticket(conn, id_ticket):
    edited_ticket = conn.recv(1024).decode()
    edited_ticket = json.loads(edited_ticket)

    ticket = sessionobj.query(Ticket).get(int(id_ticket))
    ticket.title = edited_ticket['title']
    ticket.description = edited_ticket['description']
    ticket.status = edited_ticket['status']
    sessionobj.add(ticket)
    sessionobj.commit()
    print("\nTicket actualizado!")
    return ticket


def filter_ticket(conn):
    filter_values_dict = conn.recv(1024).decode()
    filter_values_dict = json.loads(filter_values_dict)

    print(filter_values_dict)
    print(f"\n\n {filter_values_dict.items()}")
    filtered_ticket_list = []

    tickets = Ticket
    for k, v in filter_values_dict.items():
        if k == "author":
            print(f"autor: {type(v)}| {v}")
            tickets = sessionobj.query(Ticket).filter(Ticket.author == v)
        if k == "status":
            print(f"estado: {type(v)}| {v}")
            tickets = sessionobj.query(Ticket).filter(Ticket.status == v)
        if k == "date":
            print(f"fecha: {type(v)}| {v}")
            tickets = sessionobj.query(Ticket).filter(Ticket.date == v)

    print(type(tickets), tickets)
    print("-------------")
    for ob in tickets:
        print(type(ob), ob)
        filtered_ticket_list.append(ob.to_json())
    filtered_ticket_list = json.dumps(filtered_ticket_list)

    conn.send(filtered_ticket_list.encode())


def server_history(client_ip, option):
    history_file = open("server_history.log", "a")
    history_file.write(f"IP Cliente: {client_ip} | Fecha: {date.today()} | Operacion: {option}\n")
    history_file.close()
