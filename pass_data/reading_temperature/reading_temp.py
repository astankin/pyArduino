import time
import serial

data = serial.Serial('COM10', 115200)
time.sleep(1)

while True:
    while data.in_waiting == 0:
        pass
    data_packet = data.readline()
    data_packet = str(data_packet, 'utf-8')
    data_packet = data_packet.split(',')
    temp = float(data_packet[0])
    hum = float(data_packet[2])
    print(f'The temperature is {temp}°C')
    print(f'The humidity is {hum}%')