import serial
import time
# from vpython import *
arduino_data = serial.Serial('com10', 115200)
time.sleep(1)

while True:
    while (arduino_data.inWaiting() == 0):
        pass
    data_packet = arduino_data.readline()
    data_packet = str(data_packet, 'utf-8')
    data_packet = data_packet.strip('\r\n')
    split_data = data_packet.split(',')
    x = float(split_data[0])
    y = float(split_data[1])
    z = float(split_data[2])
    print(f"X = {x}, Y = {y}, Z = {z}")
