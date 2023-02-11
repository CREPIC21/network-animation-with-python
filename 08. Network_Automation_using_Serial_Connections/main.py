### IMPORTANT ###
"""
To test serial connection buy some physical devices and then come back here.
"""

import serial
import time
    
with serial.Serial(port='/home/danijel/ttyS0', baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=8) as console:
    if console.isOpen():
        print('Serial is Opened')
        console.write(b'\n')
        time.sleep(1)
        console.write(b'show version\n')
        time.sleep(3)
    
        bytes_to_be_read = console.inWaiting()
        output = console.read(bytes_to_be_read)
        print('Output: ' + output.decode())