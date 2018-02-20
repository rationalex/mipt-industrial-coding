import pika

rmq_conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = rmq_conn.channel()
channel.queue_declare(queue='task1')

message = input(">>> ")

channel.basic_publish(exchange='',
                      routing_key='task1',
                      body=message)

print("Sent message '{}'".format(message))

rmq_conn.close()