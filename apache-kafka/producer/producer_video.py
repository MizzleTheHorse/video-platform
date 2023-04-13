from operator import truediv
from kafka import KafkaProducer
import json
import time
# the bootstrap server is the address of the kafka broker, i.e. the docker container. Here you can specify multiple brokers 
# separated by a comma to enable load balancing and fault tolerance.producer = KafkaProducer(bootstrap_servers='kafka1:9092')

producer = KafkaProducer(
        bootstrap_servers='kafka1:9092', 
        value_serializer=lambda v: json.dumps(v).encode('ascii'),
        key_serializer=lambda v: json.dumps(v).encode('ascii')
    )

print('producer initialized')
exit = False
while not exit:
    
    msg = input("Enter a message: ")
    if(input == "exit"):
        exit == True
        break
    producer.send(
        'video-event',
        key={"video_id": 'test123'},
        value={
            "user_id": 1,
            "title": 'shreck',
            "resume": 'he is green and ogry',
            "category": 'fantasy'
        })
    producer.flush()