import time
import redis
from threading import Thread


client = redis.StrictRedis()

CHANNEL = 'slk_test'
pubsub = client.pubsub()
pubsub.subscribe(CHANNEL)

def publish_msg():
    """每3s发布一条内容"""
    message = [
        'slk 1',
        'slk 2',
        'slk 3',
        'slk 4'
    ]
    for msg in message:
        client.publish(CHANNEL, msg)
        time.sleep(3)


def subscribe_msg():
    for msg in pubsub.listen():
        if msg['type'] == 'message':
            print('receive:',msg)


def main():
    t1 = Thread(target=publish_msg)
    t2 = Thread(target=subscribe_msg)

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()