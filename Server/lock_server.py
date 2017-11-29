import os.path
import socket
import select
import sys
from thread import *
import threading
from threading import Thread
import sqlite3




class client_thread(Thread):

       def __init__(self,addr,c):
              Thread.__init__(self)
              self.addr = addr
              self.c = c

       def run(self):
              while True:
                     lock(self.addr,self.c)
              

def lock(name,c):
    conn = sqlite3.connect('test.db')
    print "Opened database successfully";

    file_name = c.recv(1024)
    print(file_name)
    print('1')
    cursor = conn.execute("SELECT file_name, status from files_list")
    
    print '2'
    for row in cursor:
        print '3'
        print row[0]
        print row[1]
        d_f = row[0]
        d_s = row[1]
        if d_f!= file_name:
            print (file_name)
            d_f = file_name
            d_s = 'unlocked'
            cursor = conn.execute("INSERT INTO files_list VALUES (?, ?)", (d_f, d_s))
            conn.commit()
  
   
    
        

def Main():
    host = '127.0.0.1'
    port = 6002
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
