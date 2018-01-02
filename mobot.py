import Adafruit_DHT as dht
import time
while True:
    h,t = dht.read_retry(dht.DHT22, 4)
    t = t*1.8 + 32
    print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(t, h))
    time.sleep(1)