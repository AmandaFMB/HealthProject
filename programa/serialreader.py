import serial
import datetime

ser = serial.Serial(
    port='/dev/cu.usbserial-0001',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)

line = []


file1 = open('myfile.txt', 'w')
file1.write('Date;heartRate;confidence;oxygen;status \n')
file1.close()
while True:
    for c in ser.read():
        if chr(c) == '\n':
            print(str(datetime.datetime.now()) + ';' + ''.join(line))
            # Date;heartRate;confidence;oxygen;status
            file1 = open('myfile.txt', 'a')
            file1.write(str(datetime.datetime.now()) + ';' + ''.join(line))
            file1.close()
            line = []
            break
        else:
            line.append(chr(c))

ser.close()