import socket
from models import Ticket
from datetime import date
from db_config import sessionobj
from sqlalchemy.exc import SQLAlchemyError
import json


def create_server_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    port = int(input("Ingrese el numero de puerto: "))
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("\n[*]Socket iniciado exitosamente!!")

    return server_socket


def insert_ticket(conn, lock):
    ticket = conn.recv(1024).decode()
    ticket_dict = json.loads(ticket)
    with lock:
        ticket = Ticket(title=ticket_dict['title'], author=ticket_dict['author'],
                        description=ticket_dict['description'], status="pendiente", date=date.today())
        sessionobj.add(ticket)
        try:
            sessionobj.commit()
            print("\nTicket creado!")
            conn.send("\nTicket creado!".encode())
        except SQLAlchemyError as e:
            sessionobj.rollback()
            print(e)
            conn.send("\nError al crear ticket".encode())


def list_tickets(conn):
    ticket_list = []
    tickets = sessionobj.query(Ticket).all()
    sessionobj.commit()
    for ob in tickets:
        ticket_list.append(ob.to_json())

    json_tickets = json.dumps(ticket_list)
    conn.send(json_tickets.encode())
    print("\nSe ha enviado el listado de tickets al cliente")


def get_ticket_by_id(id_ticket):
    ticket = sessionobj.query(Ticket).get(int(id_ticket))
    return ticket.to_json()


def edit_ticket(conn):
    id_ticket = conn.recv(1024).decode()
    ticket_json = get_ticket_by_id(id_ticket)  # Obtenemos en JSON el ticket obtenido en base a su ID
    ticket_json = json.dumps(ticket_json)
    print(type(ticket_json), ticket_json)
    conn.send(ticket_json.encode())  # Enviamos en JSON el ticket para que el cliente lo edite

    edited_ticket = conn.recv(1024).decode()  # Recibimos del cliente el ticket editado
    edited_ticket = json.loads(edited_ticket)

    ticket = sessionobj.query(Ticket).get(int(id_ticket))  # Se trae el ticket de DB y se le coloca los valores editados
    ticket.title = edited_ticket['title']
    ticket.description = edited_ticket['description']
    ticket.status = edited_ticket['status']
    sessionobj.add(ticket)
    try:
        sessionobj.commit()
        print("\nTicket actualizado!")
    except SQLAlchemyError as e:
        print(e)
        print("\nError al editar ticket")
        sessionobj.rollback()


def filter_ticket(conn):
    filter_values_dict = conn.recv(1024).decode()
    filter_values_dict = json.loads(filter_values_dict)

    filtered_ticket_list = []

    tickets = sessionobj.query(Ticket).filter()
    for k, v in filter_values_dict.items():
        if k == "author":
            print(f"autor: {type(v)}| {v}")
            tickets = tickets.filter(Ticket.author == v)
        if k == "status":
            print(f"estado: {type(v)}| {v}")
            tickets = tickets.filter(Ticket.status == v)
        if k == "date":
            print(f"fecha: {type(v)}| {v}")
            tickets = tickets.filter(Ticket.date == v)

    for ob in tickets:
        filtered_ticket_list.append(ob.to_json())
    filtered_ticket_list = json.dumps(filtered_ticket_list)

    conn.send(filtered_ticket_list.encode())


def server_history(client_ip, option):
    history_file = open("server_history.log", "a")
    history_file.write(f"IP Cliente: {client_ip} | Fecha: {date.today()} | Operacion: {option}\n")
    history_file.close()
