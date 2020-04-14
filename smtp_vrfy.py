#!/usr/bin/python3

import socket
import sys

# Probably u don't need it now
#if len(sys.argv) != 2:
    #print "usage: vrfy.py <username>"
    #sys.exit(0)

with open('/usr/share/wordlists/metasploit/unix_users.txt', 'r') as f:
    users = f.readlines()

#create socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to the server 
connect=s.connect(('192.168.44.133',25))
#Receive the banner
banner=s.recv(1024)
print banner

for u in users:
    user = u.strip()

    #VRFY a user
    s.send('VRFY ' + user + '\r\n')
    result=s.recv(1024)
    print result

#close the socket
s.close
