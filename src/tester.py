import serial

ser = serial.Serial("COM6", 9600)

ser.write(b"START\n")

response = ser.readline()

print("ECU response:", response.decode().strip())

ser.close()