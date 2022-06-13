# Author: Trixi Jansuy

import sys

if __name__ != "__main__":
  sys.exit("Please run server.py separately")

import socket
import mariadb

bind_ip = "0.0.0.0" # Since this is the server, bind to 0.0.0.0
bind_port = 42000

running = True

# Process messages from the socket
def ProcessMessage(msg):
  print(message) # Debugging
  print(message[0].decode("utf-8"))
  return message[0].decode("utf-8")

def QueryDB(cursor, token):
  if token is None:
    return False
  cursor.execute("SELECT * FROM test;")
  names = {}
  ids = {}

  for first_name, last_name, user_id in cursor:
    names[f"{first_name} {last_name}"] = user_id
    ids[user_id] = f"{first_name} {last_name}"
  
  flag = False
  for n in names:
    print(f"Comparing: {token} in {n}")
    if token in n:
      flag = True
      break
  if not flag:
    print(f"Checking ids")
    for i in ids:
      print(f"Comparing: {token} in {i}")
      if token in str(i):
        flag = True
        break
  return flag

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

sql_conn = mariadb.connect(user="root", password="root", host="localhost", database="sample_users")
sql_cur = sql_conn.cursor()

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
  
  # Process Message
  token_name = ProcessMessage(message)
  # Query DB
  result = QueryDB(sql_cur, token_name)
  # Process Result
  if result:
    print("Success")
  else:
    print("Not Allowed")
  # Perform Function (if Allowed ?)
