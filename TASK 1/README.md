### Task 1: Kafka Installation on Docker and Basic Operations

#### 1. Starting the Zookeeper Container

```sh
docker run -d --name zookeeper -p 2181:2181 zookeeper
```
- **Description:** Starts the Zookeeper container.
- `-d`: Runs the container in detached mode.
- `--name zookeeper`: Sets the container name to "zookeeper".
- `-p 2181:2181`: Maps the port used by Zookeeper (2181 on the host machine).

#### 2. Starting the Kafka Container

```sh
docker run -d --name kafka -p 9092:9092 --link zookeeper:zookeeper \
  -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 \
  wurstmeister/kafka
```
- **Description:** Starts the Kafka container.
- `--name kafka`: Sets the container name to "kafka".
- `-p 9092:9092`: Maps the port used by the Kafka broker (9092 on the host machine).
- `--link zookeeper:zookeeper`: Establishes the necessary connection between Kafka and Zookeeper.
- `-e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181`: Specifies the address and port for Kafka to connect to Zookeeper.
- `-e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092`: Specifies the advertised listener address for Kafka.
- `-e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092`: Specifies the listener address for Kafka broker.
- `wurstmeister/kafka`: Official Kafka image to be pulled from Docker Hub.

#### 3. Creating a Kafka Topic

```sh
docker exec -it kafka kafka-topics.sh --create --topic my-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
- **Description:** Executes a command inside the Kafka container.
- `kafka-topics.sh`: Kafka topic management tool.
- `--create`: Indicates the creation of a new topic.
- `--topic my-topic`: Specifies the name of the topic to be created (named "my-topic").
- `--bootstrap-server localhost:9092`: Specifies the bootstrap server to connect to Kafka broker.
- `--partitions 1`: Specifies the number of partitions for the topic (1 partition in this example).
- `--replication-factor 1`: Specifies the number of replicas for each partition (1 replica in this example).

#### 4. Sending Messages to a Kafka Topic

```sh
docker exec -it kafka kafka-console-producer.sh --topic my-topic --bootstrap-server localhost:9092
```
- **Description:** Tool to send messages to Kafka topic via console.
- `--topic my-topic`: Specifies the name of the topic to send messages to (named "my-topic").
- `--bootstrap-server localhost:9092`: Specifies the bootstrap server to connect to Kafka broker.

#### 5. Listening to Messages from a Kafka Topic

```sh
docker exec -it kafka kafka-console-consumer.sh --topic my-topic --bootstrap-server localhost:9092 --from-beginning
```
- **Description:** Tool to listen to messages from Kafka topic via console.
- `--topic my-topic`: Specifies the name of the topic to listen to (named "my-topic").
- `--bootstrap-server localhost:9092`: Specifies the bootstrap server to connect to Kafka broker.
- `--from-beginning`: Displays all messages from the beginning of the topic.

These commands set up Kafka on Docker, create a topic, send and listen to messages using Kafka CLI commands.