# ML Engineer Task

This project demonstrates web scraping for data retrieval, managing data flow with Kafka, and creating a REST API service using Flask.

### Task 1: Kafka Installation on Docker and Basic Operations

#### 1. Starting the Zookeeper Container

To start Zookeeper on Docker, use the following command:

```sh
docker run -d --name zookeeper -p 2181:2181 zookeeper
```

#### 2. Starting the Kafka Container

To start Kafka on Docker, use the following command:

```sh
docker run -d --name kafka -p 9092:9092 --link zookeeper:zookeeper \
  -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 \
  wurstmeister/kafka
```

#### 3. Creating a Kafka Topic

To create a Kafka topic, use the following command:

```sh
docker exec -it kafka kafka-topics.sh --create --topic my-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

#### 4. Sending Messages to a Kafka Topic

To send messages to a Kafka topic, use the following command:

```sh
docker exec -it kafka kafka-console-producer.sh --topic my-topic --bootstrap-server localhost:9092
```

#### 5. Listening to Messages from a Kafka Topic

To listen to messages from a Kafka topic, use the following command:

```sh
docker exec -it kafka kafka-console-consumer.sh --topic my-topic --bootstrap-server localhost:9092 --from-beginning
```

### Task 2: Data Retrieval from Web, Writing to Kafka, and Creating a REST API Service

#### 1. Web Scraping and Writing to Kafka

To fetch data from a web page and write it to Kafka using Python, utilize libraries such as `requests`, `BeautifulSoup`, and `confluent-kafka`. Sample Python scripts (`producer.py` and `consumer.py`) are provided.

#### 2. Creating a REST API Service

To create a simple REST API service using Flask, use the `Flask` library. An example Flask application (`app.py`) is provided.

### Technologies Used

- **Kafka:** Used for distributed data streaming.
- **Zookeeper:** Used for coordinating the Kafka cluster.
- **Docker and Docker Compose:** Used for containerizing applications to run in isolated environments.
- **Python Libraries:** Utilized `requests`, `BeautifulSoup`, `confluent-kafka`, and `Flask` for data retrieval, processing, writing to Kafka, and creating a REST API service.

### How to Run?

1. Ensure Docker and Docker Compose are installed.
2. Use the `docker-compose.yml` file to run Kafka, Zookeeper, Producer, Consumer, and API services together.
3. Follow individual steps for each task to execute the operations.

### Development Environment

- **Docker:** Version 20.10 or higher
- **Python:** Version 3.8 or higher
