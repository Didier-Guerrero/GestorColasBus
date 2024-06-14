from azure.servicebus import ServiceBusClient

# Parámetros de conexión(Cambiar al connection string que desee)
CONNECTION_STR = '********************************************************************************************'
QUEUE_NAME = 'incidents'

def receive_messages(receiver):
    received_msgs = receiver.receive_messages(max_message_count=10, max_wait_time=5)
    for msg in received_msgs:
        print("Mensaje recibido: ", str(msg))
        receiver.complete_message(msg)

# Crear cliente del Service Bus
servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

# Recibir mensajes
with servicebus_client:
    receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME)
    with receiver:
        receive_messages(receiver)
