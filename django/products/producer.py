import pika
import json
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
# channel = connection.channel()


def publish(method, body):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    properties = pika.BasicProperties(method)

    # channel.basic_publish(
    #     exchange='',
    #     routing_key='main',
    #     body=json.dumps(body),
    #     properties=properties
    # )

    try:
        channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
    except Exception as e1:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        channel = connection.channel()
        channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
