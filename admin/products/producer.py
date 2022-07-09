import pika

params = pika.URLParameters('amqps://shagynym:LgU9act_-y8ktIqDNxB9XDex9Nm04O3a@jackal.rmq.cloudamqp.com/shagynym')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
  channel.basic_publish(exchange='', routing_key='admin', body='hello')