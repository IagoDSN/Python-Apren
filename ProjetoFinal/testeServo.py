import serial
import time

arduino = serial.Serial('COM3', 9600)

def set_angle(angle):
    arduino.write(f"{angle}\n".encode())
    time.sleep(1)

set_angle(0)
set_angle(90)
set_angle(180)
