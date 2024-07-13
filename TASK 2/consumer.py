from confluent_kafka import Consumer, KafkaException
import json

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['my-topic'])

output_file = 'kafka_data.json'

consumer.close()


try:
    with open(output_file, 'w') as f:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    continue
                else:
                    raise KafkaException(msg.error())
            record = json.loads(msg.value().decode('utf-8'))
            json.dump(record, f)
            f.write('\n')
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
