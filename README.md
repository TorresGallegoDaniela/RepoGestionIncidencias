# GestionIncidenciasTipoBug

Este repositorio contiene el código fuente para una aplicación de gestión de incidencias tipo bug.

## Descripción
GestionIncidenciasTipoBug es una funcion que te brinda la capacidad de reportar y gestionar incidencias y errores en tu código de manera efectiva y colaborativa. Esta funcion está diseñada para agilizar y optimizar el proceso de detección y seguimiento de bugs en los proyectos de software.

## Características

- Comunicación Asíncrona con Rabbit MQ: GestionIncidenciasTipoBug utiliza una comunicación asincrónica a través de Rabbit MQ, lo que permite un flujo constante y fluido de información entre los miembros del equipo. 

- Reporte Rápido y Preciso: La aplicación proporciona un proceso de reporte de bugs sencillo e intuitivo. 

- Seguimiento de Incidencias en Tiempo Real: GestionIncidenciasTipoBug ofrece una vista en tiempo real de todas las incidencias registradas. 

- Notificaciones Personalizadas: GestionIncidenciasTipoBug permite configurar notificaciones personalizadas para mantener a todos los miembros del equipo informados sobre las actualizaciones de incidencias importantes.

## Requisitos
Antes de ejecutar la aplicación, es importante asegurarte de que tengas instalados los siguientes componentes y bibliotecas en tu entorno de desarrollo:

- Python 3
### Bibliotecas de Python:
- pika: Permite interactuar con RabbitMQ.

```python
pip install pika
```

Para obtener más información sobre RabbitMQ y cómo usar la biblioteca `pika`, puedes consultar la documentación oficial y tutoriales:

- [RabbitMQ Documentation](https://www.rabbitmq.com/)
- [pika Documentation](https://pypi.org/project/pika/)

# Uso de la Función ReportBug

## Sintaxis

```python
from incidentsBug.bugReports import BugReports

# Crea una instancia de la clase `ReportBug`
bugReportsInstance = BugReports(idProyecto="ID_PROYECTO", area="AREA", título="TITULO")

# Establece las credenciales de RabbitMQ
bugReportsInstance.setRabbitmqCredentials(username="TU_USUARIO", password="TU_CONTRASEÑA", host="DIRECCIÓN_DEL_SERVIDOR", queue="NOMBRE_DE_LA_COLA")

# Reporta un bug
bugReportsInstance.bugReports()
```

### Ejemplo

```python
bugReportsInstance = BugReports(idProyecto="123456", area="desarrollo", título="Error en la función `foo()`")
bugReportsInstance.setRabbitmqCredentials(username="tu_usuario", password="tu_contraseña", host="dirección_del_servidor", queue="nombre_de_la_cola")
bugReportsInstance.bugReports()
```

### Excepciones
Si hay algún error al reportar el bug, la función `bugReports()` arrojará una excepción.