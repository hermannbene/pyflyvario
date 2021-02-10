import serial
from time import sleep
from baro import read
while True:
    try:
        ser = serial.Serial('/dev/rfcomm0')
        break
    except:
        print("wait for bt")
        sleep(1)
        pass
def cksum(msg):
    calc_cksum = 0
    for s in msg:
        calc_cksum ^= ord(s)
    return hex(calc_cksum)[2:]

def send(pressure):
    msg = 'LK8EX1,'+str(pressure)+',99999,9999,99,999,'
    cks = cksum(msg)
    eol = '\n'
    ser.write(bytes('$'+msg+'*'+cks+eol, 'utf-8'))     # write a string

while True:
    try:
        send(read())
        sleep(0.1)
    except:
        ser.close()
        print("lost bt")
        sleep(1)
        try:
            ser = serial.Serial('/dev/rfcomm0')
        except:
            pass 

ser.close()             # close port

