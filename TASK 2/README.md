### Project Components and Technologies Used

1. **Kafka and Zookeeper:**
   - **Kafka:** A distributed data streaming platform that facilitates the production, processing, and consumption of messages (producer-consumer model).
   - **Zookeeper:** A service that manages coordination and management for Kafka. It stores configuration information and status for the Kafka cluster.

2. **Docker and Docker Compose:**
   - **Docker:** Allows packaging applications, dependencies, and configurations into containers for consistent running across different environments (development, testing, production).
   - **Docker Compose:** Tool for managing multiple Docker containers as a single unit. Used in this project to run and connect Kafka and Zookeeper containers.

3. **Web Scraping and Data Processing:**
   - **requests and BeautifulSoup:** Python libraries used for fetching and parsing data from web pages. In this project, they are used to extract product information from an e-commerce site.

4. **Kafka Producer (`producer.py`):**
   - Python script that writes data extracted from the web to Kafka. It sends information such as product name, price, and rating to a Kafka topic, enabling real-time data streaming via Kafka.

5. **Kafka Consumer (`consumer.py`):**
   - Python script that reads data from a Kafka topic. It stores incoming data into a JSON file, providing a means to persist and process data retrieved from Kafka as needed.

6. **REST API Service (`app.py`):**
   - Simple REST API service created using Flask. This service allows access to data stored in Kafka via HTTP endpoints. For example, the `/data` endpoint returns data in JSON format.

### Purpose

- **Data Streaming Management:** Kafka is ideal for managing large-scale data streams in distributed systems. This project utilizes Kafka to process and store product data obtained from an e-commerce site in real-time.

- **Use of Docker and Docker Compose:** Docker simplifies application development and deployment processes, while Docker Compose manages multiple containers in a unified structure. In this project, Kafka and Zookeeper are managed and isolated using Docker containers.

- **Web Scraping and Data Processing:** Leveraging libraries like `requests` and `BeautifulSoup`, the project extracts and processes web data. Data is streamed into Kafka for real-time processing and stored using Kafka Consumer for future use.

These components and technologies ensure efficient management of project processes. 