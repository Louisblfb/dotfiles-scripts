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
  print 'Connecting to %s:%d...' % (HOST, PORT)
  s.connect((HOST, PORT))
except socket.error:
  print 'Unable to connect.'
  sys.exit(1)

print s.recv(RECV_SIZE)
print '*** MPD-Console ***\n'



cmd = 'currentsong'
s.send(cmd + '\n')
print s.recv(RECV_SIZE)
  
print 
s.close()

