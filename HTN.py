import time
import smbus # module of I2C
import serial
import os

os.system('sudo rfcomm bind rfcomm0 00:14:03:06:75:D3')
bluetooth = serial.Serial(port='/dev/rfcomm0', baudrate=115200, parity=serial.PARITY_ODD, stopbits=serial.STOPBITS_TWO, bytesize=serial.SEVENBITS)
arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.1)

# PWR_MGMT_1 = 0x6B
# SMPLRT_DIV = 0X19
# CONFIG = 0x1A
# GYRO_CONFIG = 0x1B
# INT_ENABLE = 0x38
# GYRO_XOUT_H = 0x43
# GYRO_YOUT_H = 0X45
# GYRO_ZOUT_H = 0X47

# def MPU_Init():
#     bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
#     bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
#     bus.write_byte_data(Device_Address, CONFIG, 0)
#     bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
#     bus.write_byte_data(Device_Address, INT_ENABLE, 1)

# def read_raw_data(addr):
#     high = bus.read_byte_data(Device_Address, addr)
#     low = bus.read_byte_data(Device_Address, addr+1)
#     value = (high << 8 )| low
#     if value > 32768:
#         value =value - 65536
#     return value

# bus =smbus.SMBus(1)
# Device_Address = 0x68

# MPU_Init()

# desiredAngle = 0 

while 1:
    if bluetooth.inWaiting() > 0:
        direction = bluetooth.readline().rstrip().decode("utf-8")
        if direction == 'F':
            arduino.write(bytes(b"L50\n"))
            arduino.write(bytes(b"R50\n"))
            print("move forward")
        elif direction == 'B':
            arduino.write(bytes(b"L-50\n"))
            arduino.write(bytes(b"R-50\n"))
            print("move backward")
        elif direction == 'L':
            arduino.write(bytes(b"L-50\n"))
            arduino.write(bytes(b"R50\n"))
            print("turn left")
        elif direction == 'R':
            arduino.write(bytes(b"L50\n"))
            arduino.write(bytes(b"R-50\n"))
            print("turn right")
        elif direction == 'S':
            arduino.write(bytes(b"L0\n"))
            arduino.write(bytes(b"R0\n"))
            print("stop")
    if arduino.inWaiting() > 0:
        print(arduino.readline())
    # Gx = read_raw_data(GYRO_XOUT_H)/131.0
    # Gy = read_raw_data(GYRO_YOUT_H)/131.0
    # Gz = read_raw_data(GYRO_ZOUT_H)/131.0


