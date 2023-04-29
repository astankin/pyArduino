import time
import serial
from vpython import *
import numpy as np

arrow_length = 1
arrow_width = 0.02
arrow_ = arrow(length=arrow_length, shaftwidth=arrow_width, color=color.red, axis=vector(-1, 0, 0))

data = serial.Serial('COM10', 115200)
time.sleep(1)

tick_length = 0.1
tick_width = 0.05
tick_height = 0.05

for theta in np.linspace(np.pi, 0, 6):
    tick_major = box(pos=vector(arrow_length * np.cos(theta), arrow_length * np.sin(theta), 0), size=vector(tick_length, tick_width, tick_height))

box_X = 2.5
box_Y = 1.5
box_Z = 0.1
my_case = box(color=color.white, size=vector(box_X, box_Y, box_Z), pos=vector(0, 0.9*box_Y/2, -box_Z/2))

while True:
    while data.in_waiting == 0:
        pass
    data_packet = str(data.readline(), 'utf-8').strip('\r\n')
    pot_val = int(data_packet)
    voltage = (5/1023)*pot_val
    theta = -2 * np.pi/3069 * pot_val + 5 * np.pi / 6
    arrow_.axis = vector(arrow_length * np.cos(theta), arrow_length * np.sin(theta), 0)
    # label.text = str(round(voltage, 1))
    # for theta in np.linspace(0, np.pi, 150):
    #     rate(25)
    #     arrow_.axis = vector(arrow_length * np.cos(theta), arrow_length * np.sin(theta), 0)
    
    # for theta in np.linspace(np.pi, 0, 150):
    #     rate(25)
    #     arrow_.axis = vector(arrow_length * np.cos(theta), arrow_length * np.sin(theta), 0)