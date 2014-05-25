import serial

print("Hammering.")

ser = serial.Serial('/dev/ttyACM0', 9600)
ser.write('A')
time.sleep(.500)
ser.write('Z')

