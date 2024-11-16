import network
import socket
import time
from machine import Pin
import dht
import ntptime

# Initialize Wi-Fi and DHT11 sensor
dht_sensor = dht.DHT11(Pin(15))  # Pin 15 is used in the example, can be changed

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    max_attempts = 10
    attempt = 0
    while not wlan.isconnected() and attempt < max_attempts:
        print(f"Attempt {attempt + 1} to connect to Wi-Fi...")
        time.sleep(1)
        attempt += 1

    if wlan.isconnected():
        print("Connected to Wi-Fi")
        print("IP Address:", wlan.ifconfig()[0])
        return wlan.ifconfig()[0]
    else:
        print("Failed to connect to Wi-Fi")
        return None

def get_current_time():
    try:
        ntptime.settime()  
        current_time = time.localtime()
        formatted_time = f"{current_time[0]}-{current_time[1]:02}-{current_time[2]:02} {current_time[3]:02}:{current_time[4]:02}:{current_time[5]:02}"
        return formatted_time
    except:
        return "NTP sync failed"

def get_sensor_data():
    try:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        return temperature, humidity
    except Exception as e:
        print("DHT sensor error:", e)
        return None, None

# Replace these with your Wi-Fi credentials
ssid = "**********"
password = "************"
ip_address = connect_to_wifi(ssid, password)


if ip_address:
    addr = socket.getaddrinfo(ip_address, 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    
    print('Listening on', addr)

    while True:
        cl, addr = s.accept()
        print('Client connected from', addr)

        
        temperature, humidity = get_sensor_data()
        current_time = get_current_time()

        
        response = f"""\
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>Sensor Data</title>
</head>
<body>
    <h1>Raspberry Pi Pico W Sensor Data</h1>
    <p><strong>Date & Time:</strong> {current_time}</p>
    <p><strong>Temperature:</strong> {temperature} °C</p>
    <p><strong>Humidity:</strong> {humidity} %</p>
</body>
</html>
"""
        
        cl.send(response)
        cl.close()
        print("Data served at", current_time)
        
        # Wait for 1 minute before next update (in seconds)
        time.sleep(60)

