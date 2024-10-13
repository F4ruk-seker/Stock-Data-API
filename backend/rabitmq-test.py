# import pika
#
# # RabbitMQ'ya bağlanmayı dene
# try:
#     # Bağlantı parametreleri
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#     channel = connection.channel()
#
#     # Kuyruğu oluştur (varsa tekrar oluşturmayacak)
#     channel.queue_declare(queue='test_queue')
#
#     # Mesaj gönder
#     message = 'Test message'
#     channel.basic_publish(exchange='', routing_key='test_queue', body=message)
#     print(f" [x] Sent '{message}'")
#
# except pika.exceptions.AMQPConnectionError as e:
#     print(f"RabbitMQ'ya bağlanırken hata: {e}")
#
# except Exception as e:
#     print(f"Beklenmedik bir hata: {e}")
#
# finally:
#     # Bağlantıyı kapat
#     try:
#         connection.close()
#     except:
#         pass

import redis

# Redis sunucusuna bağlan
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Redis'teki tüm anahtarları al
all_keys = r.keys('*')

# Anahtarları listele
if all_keys:
    print("Redis'teki tüm anahtarlar:")
    for key in all_keys:
        print(key.decode())  # Anahtarlar byte formatında döner, bu yüzden decode yapıyoruz.
else:
    print("Redis'te hiç anahtar yok.")

# Tüm anahtarları silmek için onay iste
confirm = input("Tüm anahtarları silmek istediğinizden emin misiniz? (y/n): ")

if confirm.lower() == 'y':
    # Redis'teki tüm anahtarları sil
    r.flushdb()  # Bu komut tüm veritabanını temizler
    print("Tüm anahtarlar silindi.")
else:
    print("İşlem iptal edildi.")
