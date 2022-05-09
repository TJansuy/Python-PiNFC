# Author: Trixi Jansuy

"""
This code is intended to be ran from the Raspberry Pi with the PN532 NFC HAT attached
"""

# Using PN532 library from Waveshare
import pn532.uart

import RPi.GPIO

import sys 

if __name__ != "__main__":
  sys.exit("Please run the NFC-station separately.")


# Init PN532 api
nfc = pn532.uart.PN532_UART 
nfc.SAM_configuration()

try:
  
  # Main Loop
  while True:
    
    scan = nfc.read_pass_target(timeout=0.5)
    
    print(scan)

finally:
  RPi.GPIO.cleanup()

