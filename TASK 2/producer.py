from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
from confluent_kafka import Producer, KafkaException
import atexit

# Kafka Producer settings
producer = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# WebDriver setup
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Navigate to the main page
    url = 'https://scrapeme.live/shop/'
    driver.get(url)
    time.sleep(5)  # Wait for page to load (adjust as necessary)

    # Find products on the page
    products = driver.find_elements(By.CSS_SELECTOR, 'ul.products li.product')

    # Process each product on the page
    for product in products:
        name = product.find_element(By.CSS_SELECTOR, 'h2.woocommerce-loop-product__title').text
        link = product.find_element(By.CSS_SELECTOR, 'a.woocommerce-LoopProduct-link').get_attribute('href')

        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(link)
        time.sleep(2)  # Wait for product page to load

        # Extract product information
        product_info = {
            "Name": driver.find_element(By.CLASS_NAME, "product_title").text,
            "Price": driver.find_element(By.CSS_SELECTOR, ".price span.woocommerce-Price-amount.amount").text,
            "Description": driver.find_element(By.CLASS_NAME, "woocommerce-product-details__short-description").text,
            "Stock": driver.find_element(By.CLASS_NAME, "stock").text
        }

        # Produce message to Kafka topic
        producer.produce('my-topic', key=str(time.time()), value=json.dumps(product_info), callback=delivery_report)
        producer.poll(0)  # Trigger delivery report callback
        time.sleep(1)  # Delay before closing window

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

finally:
    driver.quit()
    producer.flush()
