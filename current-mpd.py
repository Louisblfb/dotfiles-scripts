#!/usr/bin/python

try:
  import readline
except ImportError:
  pass
import socket
import sys

HOST = 'localhost'
PORT = 6600
RECV_SIZE = 2**20 # One megabyte
try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))
except socket.error:
  sys.exit(1)

print s.recv(RECV_SIZE)
s.send('currentsong' + '\n')
print s.recv(RECV_SIZE)  
s.close()

