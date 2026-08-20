import serial

ser = serial.Serial("COM7", 9600)

while True:
    data = ser.readline()

    command = data.decode().strip()

    if command == "START":
        #pass
        ser.write(b"OK\n")

    elif command == "STOP":
        ser.write(b"STOPPED\n")

    elif command == "STATUS":
        ser.write(b"READY\n")

    elif command == "TEMP":
        ser.write(b"25.4\n")

    elif command == "EXIT":
        ser.write(b"ECU shutting down...\n")
        break

    else:
        ser.write(b"UNKNOWN COMMAND\n")

ser.close()