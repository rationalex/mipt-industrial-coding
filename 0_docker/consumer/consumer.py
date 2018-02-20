import pika

from pymongo import MongoClient

DB_NAME = 'task1'

client = MongoClient(host='mongo')

client.drop_database('MONGO_DB')
db = client[DB_NAME]
db.drop_collection('messages')

rmq_conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = rmq_conn.channel()
channel.queue_declare(queue='task1')

def callback(ch, method, properties, body):
  print("Message received: {}".format(body.decode()))
  db.messages.save({
          'message': body.decode()
          })


channel.basic_consume(callback,
                      queue='task1',
                      no_ack=True)

print('Waiting for messages...')

try:
  channel.start_consuming() 
except KeyboardInterrupt:
  channel.stop_consuming()

client.close()
