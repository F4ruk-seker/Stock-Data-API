import pika

# RabbitMQ'ya bağlanmayı dene
try:
    # Bağlantı parametreleri
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Kuyruğu oluştur (varsa tekrar oluşturmayacak)
    channel.queue_declare(queue='test_queue')

    # Mesaj gönder
    message = 'Test message'
    channel.basic_publish(exchange='', routing_key='test_queue', body=message)
    print(f" [x] Sent '{message}'")

except pika.exceptions.AMQPConnectionError as e:
    print(f"RabbitMQ'ya bağlanırken hata: {e}")

except Exception as e:
    print(f"Beklenmedik bir hata: {e}")

finally:
    # Bağlantıyı kapat
    try:
        connection.close()
    except:
        pass
