import os.path
import socket
import select
import sys
from thread import *
import threading


def lock():
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 6002                 # Reserve a port for your service.
    s.bind(('', port))        # Bind to the port
    print 'server started'
    s.listen(5)
    files = {'hello.txt':'unlocked'}
    c, addr = s.accept()
    file_name = c.recv(1024)
    print(file_name)
    
    if file_name in files.keys():
        value = files.get(file_name)
        c.send(value.encode())
    else:
        files[file_name]='unlocked'
        value = files.get(file_name)
        
        c.send(value.encode())
        f2 = c.recv(1024)
        print(f2)
        if f2 in files.keys():
            files[f2] = 'locked'
            print(files)
        f3 = c.recv(1024)
        if f3=='done':
            files[f2]= 'unlocked'
            print(files)
    
        

if __name__ == '__main__':
    lock()
    
    
