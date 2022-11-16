import threading, time
from kafka import KafkaProducer

class Producer(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        producer = KafkaProducer(bootstrap_servers='localhost:9092')

        while not self.stop_event.is_set():
            producer.send('my-topic2',key=b"1", value=b"test")
            producer.send('my-topic2',key=b"2", value=b"Heelloo")
            time.sleep(1)

        producer.close()