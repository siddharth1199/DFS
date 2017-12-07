import os.path
import socket
import select
import sys
from thread import *
from threading import Thread

class client_thread(Thread):

       def __init__(self,addr,c):
              Thread.__init__(self)
              self.addr = addr
              self.c = c

       def run(self):
              while True:
                     file_server(self.addr,self.c)
              

def file_server(name,c):

       path = os.getcwd()
       dir = os.listdir(path)
       print 'Server started'


       a = c.recv(1024)
       remove = a[1:-1]
       h = remove.split(", ")
       h1 = h[0].replace("'", "")
       f1 = h[1]

       if f1 == "'r'":
              print "Read"
              f = open(h1)
              l = f.read(1024)
              while (l):
                     c.send(l)
                     print('Sent ',repr(l))
                     l = f.read(1024)
              f.close()
              print "File was sent"
       elif f1 == "'a'":
              a1 = c.recv(1024)
              print a1
              f = open(h1, 'a')
              l = f.write(a1)
              print "File Modified"
              f.close()

       else:
              print "Failed to Read"
                           # Close the connection


def Main():
    host = '127.0.0.1'
    port = 5003
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('',port))
    s.listen(5)

    
    print('server started')
    while(True):
        (c,addr) = s.accept()
        print('client connected ip:'+str(addr))
        Thread = client_thread(addr,c)
        Thread.start()


        
if __name__ == '__main__':    
    Main()
