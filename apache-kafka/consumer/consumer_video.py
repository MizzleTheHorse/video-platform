from kafka import KafkaConsumer
import json
# The first argument is the topic name, the second is the bootstrap server of the Kafka cluster
# The third argument is the group id, which is used to identify the consumer group

consumer = KafkaConsumer(
        bootstrap_servers=['kafka1:9092'],
        group_id='group1',
        value_deserializer=lambda v: json.loads(v.decode('ascii')),
        key_deserializer=lambda v: json.loads(v.decode('ascii')),
        max_poll_records=10,
        auto_offset_reset='earliest',
        session_timeout_ms=6000,
        heartbeat_interval_ms=3000
    )
consumer.subscribe(topics=['video-event'])


for message in consumer:
    print(message.value)
    print(message.value["user_id"])
    print(message.value["title"])
    print(message.value["resume"])

