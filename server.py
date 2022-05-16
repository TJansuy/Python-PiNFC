# Author: Trixi Jansuy

import sys

if __name__ != "__main__":
  sys.exit("Please run server.py separately")

import socket


bind_ip = "0.0.0.0" # Since this is the server, bind to 0.0.0.0
bind_port = 42000

running = True



# Init socket
sock = None

print("Attempting to initalise server socket")
try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.settimeout(1) # 1 second timeout
  sock.bind((bind_ip, bind_port))

  if sock is None:
    raise Exception

except Exception as e:
  print(e)
  sys.exit("Unable to initialise socket")
# Socket should exist and be able to listen from this point forward

print("Server socket initialised")

# Begin main execution loop
print("Starting Server:")
while running:
  message = None
  try:
    message = sock.recvfrom(1024)
  except KeyboardInterrupt as e:
    print(e)
    running = False
    break
  except TimeoutError:
    print(".")

  if message is None:
    continue
  print(message) # Debugging
  
