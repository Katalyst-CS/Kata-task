import pika
import pika.credentials

def __connect__():
    # credentials = pika.credentials.PlainCredentials('user', 'password')
    parameters = pika.ConnectionParameters(host='localhost' ,port=5000)
    return pika.BlockingConnection(parameters)

connection = __connect__()
channel = connection.channel()
channel.basic_qos(prefetch_count=1)