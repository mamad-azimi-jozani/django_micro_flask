import pika, sys, os, json
from main import ProductFlask, db


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    data = json.loads(body)
    print(data)
    if properties.content_type == 'product_created':
        product = ProductFlask(id=data['id'], title=data['title'], image=['image'])
        db.session.add(product)
        db.session.commit()
        print('product was created')

    if properties.content_type == 'product_updated':
        product = ProductFlask.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('product was updated')

    if properties.content_type == 'product_deleted':
        product = ProductFlask.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print('product was deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
