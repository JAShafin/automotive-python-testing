while True:
    command = input("ECU received: ")

    if command == "START":
        print("ECU response: OK")

    elif command == "STOP":
        print("ECU response: STOPPED")

    else:
        print("ECU response: UNKNOWN COMMAND")