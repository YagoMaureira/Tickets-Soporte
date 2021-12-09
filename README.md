# Tickets-Soporte

Sistema de tickets de soporte hecho en Python

# Ayuda y uso básico de la aplicación

### Servidor

En primera instancia se debe lanzar el servidor, cuyo nombre es **server.py**.
Para ejecutar el mismo se debe escribir en terminal lo siguiente: `python3 server.py`.
Realizado este paso, se va pedir en que puerto va atender el servidor, con lo cual se debe ingresar el numero de puerto
deseado. Con todos estos pasos hechos, el servidor ya quedara funcionando y escuchando las conexiones de los clientes.
Cuando se desee cerrar el servidor, hay que pulsar Ctrl+C, con esto se finalizara el servidor.

### Cliente

Cuando el servidor esté ejecutandose y escuchando conexiones, para que un cliente pueda conectarse, en terminal debe
tipear lo siguiente: `python3 client.py`. Una vez hecho esto, se solicitará que ingrese el host y luego el puerto al
servidor que se desea conectar (En este punto se se debe ingresar el mismo numero de puerto que se ingresó cuando se 
inició el servidor). Al realizar lo anterior, se mostrará en terminal el menú en donde se indican los comandos para la 
interacción con el servidor, los cuales son los siguientes:

`-i / --insertar` -> Para insertar un nuevo ticket

`-l / --listar` -> Para listar todos los tickets

`-f / --filtrar` -> Para obtener una lista filtrada de tickets por autor, fecha o estado

`-e / --editar` -> Para editar un ticket en particular

`-x / --exportar` -> Para exportar una lista completa o filtrada por autor, fecha o estado

`-q / --quit` -> Para finalizar la conexion con el servidor


