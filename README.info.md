## Base de Datos

En este proyecto se utilizó una base de datos relacional, MySQL para ser más específico. La elección de esta DB es 
porque es una de las más utilizadas por la comunidad del desarrollo, y además cuenta con gran cantidad de documentación
para facilitar el aprendizaje y en la corrección de errores 

## SQL Alchemy (ORM)

Para persistir los objetos de python en la base de datos se optó por SQL Alchemy, el cual permite abstraer el código de 
la base de datos. SQLAlchemy utiliza un conjunto de sentencias y tipos de datos para asegurarse de que sus sentencias 
SQL sean creadas en forma adecuada y eficiente para cada base de datos sin necesidad de tener que pensar en eso.

## JSON (JavaScript Object Notation)

JSON es un formato de texto sencillo para el intercambio de datos. Se trata de un subconjunto de la notación literal de 
objetos de JavaScript, aunque, debido a su amplia adopción como alternativa a XML, se considera un formato 
independiente del lenguaje. La mayoría de datos intercambiados entre el cliente y servidor se encuentran en este 
formato debido a la sencillez que se presenta tanto para la interpretación como para su manipulación para el su envio y
recepción.

## multiprocessing (Paquete Python)

Se utilizó este Paquete para el paralelismo basado en procesos. Para lanzar un proceso paralelo a la hora de exportar
tickets en formato CSV comprimido se utilizó el objeto Process de este paquete.

## threading (Paquete Python)

Este paquete se utiliza para el paralelismo basado en hilos. Para lanzar un hilo por cada cliente que se va conectando
se utiliza el objeto **Thread**.



