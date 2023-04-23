import time
import serial
from vpython import *

tube = cylinder(color=color.blue, radius=1, length=5, axis=vector(0, 1, 0))
label = label(text='5 Volts', box=False)

data = serial.Serial('COM10', 115200)
time.sleep(1)

while True:
    while data.in_waiting == 0:
        pass
    data_packet = str(data.readline(), 'utf-8').strip('\r\n')
    pot_val = int(data_packet)
    voltage = (5/1023)*pot_val
    # print(round(voltage, 1))
    if voltage == 0:
        voltage = 0.001
    tube.length = voltage
    label.text = str(round(voltage, 1))