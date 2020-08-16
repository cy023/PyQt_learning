import serial

COM_PORT = 'COM32'
BAUD     = 38400
ser      = serial.Serial(COM_PORT, BAUD)

try:
    while True:
        while ser.in_waiting:
            data = ser.readline().decode()
            print(data)

except KeyboardInterrupt:
    ser.close()
    print(COM_PORT, 'Closed.')