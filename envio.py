import logging
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from datetime import datetime

# Parámetros de conexión(Cambiar al connection string que desee)
CONNECTION_STR = '********************************************************************************************'
QUEUE_NAME = 'incidents'

# Configuración de logging
logging.basicConfig(level=logging.INFO)

def send_incident_message(sender, incident_id, incident_description, severity, timestamp):
    try:
        # Crear el contenido del mensaje con la información del incidente
        message_content = (
            f"Incidente ID: {incident_id}\n"
            f"Descripción: {incident_description}\n"
            f"Severidad: {severity}\n"
            f"Timestamp: {timestamp}"
        )
        message = ServiceBusMessage(message_content)

        # Enviar el mensaje a la cola
        sender.send_messages(message)
        logging.info(f"Mensaje de incidente {incident_id} enviado exitosamente.")
    except Exception as e:
        logging.error(f"Error al enviar el mensaje de incidente {incident_id}: {str(e)}")

# Crear cliente del Service Bus
servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

# Ejemplo de datos de un incidente
incident_id = 12345
incident_description = "Falla en el servidor principal que causa interrupción del servicio."
severity = "Alta"
timestamp = datetime.now().isoformat()

# Enviar mensaje de incidente
with servicebus_client:
    sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
    with sender:
        send_incident_message(sender, incident_id, incident_description, severity, timestamp)
