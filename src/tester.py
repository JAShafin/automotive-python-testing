import serial

ser = serial.Serial("COM6", 9600, timeout=2)

ser.write(b"START\n")

response = ser.readline().decode().strip()

if response == "OK":
    print("TEST PASSED")
else:
    print("TEST FAILED")

ser.close()