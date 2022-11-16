## Run kafka server

Start Apache Zookeeper. bin/zookeeper-server-start.sh config/zookeeper.properties.
Start the Kafka server. bin/kafka-server-start.sh config/server.properties.


## Check the topic and create

bin/kafka-topics.sh --list --bootstrap-server localhost:9092

kafka-topics.sh -zookeeper localhost:2181 -describe --topic <name>

bin/kafka-topics.sh --create --topic testkafka --bootstrap-server localhost:9092 --replication-factor 1 --partitions 4

## Consumer
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic testkafka --from-beginning


## producer 
bin/kafka-console-producer.sh -broker-list localhost:9092 -topic testkafka


## checking the consumer group detail
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 -describe --group first
