from infrastructure.mq.connection import channel

def declare_durable(queue):
    channel.queue_declare(queue, durable=True)
    