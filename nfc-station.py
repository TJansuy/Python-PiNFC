# Author: Trixi Jansuy

"""
This code is intended to be ran from the Raspberry Pi with the PN532 NFC HAT attached
"""

# Using PN532 library from Waveshare
import RPi.GPIO
from pn532 import *

import sys 
import socket 


if __name__ != "__main__":
  sys.exit("Please run the NFC-station separately.")

# Init PN532 api
nfc = PN532_UART(debug=False, reset=20)
nfc.SAM_configuration()

try:
  
  # Main Loop
  while True:
    
    # Poll the sensor for NFC presence
    scan = nfc.read_passive_target(timeout=0.5)
    
    # Check if the poll returned anything
    if scan is not None:
      # The sensor found something
      print(scan)


finally:
  RPi.GPIO.cleanup()

