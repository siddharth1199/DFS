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
    d_f=[]
    d_s=[]
    file_name = c.recv(1024)
    print(file_name)
    print('1')
    cursor = conn.execute("SELECT file_name, status from files_list")
    i=0
    for row in cursor:       
        print row[0]
        print row[1]
        if file_name == row[0]:
               i = i+1
    if i==0:
           d_f = file_name
           d_s = 'unlocked'
           cursor = conn.execute("INSERT INTO files_list VALUES (?, ?)", (d_f, d_s))
           conn.commit()
    else:
           print 'file exists'
           cursor = conn.execute("SELECT status from files_list WHERE file_name = (?)", (file_name,))
           for row in cursor:                  
                  d_s = row[0]
    c.send(d_s.encode())

    f_name = c.recv(1024)
    cursor = conn.execute("UPDATE files_list SET status = 'locked' WHERE file_name = (?)",(f_name,))
    conn.commit()
    print('file locked')
    inp = c.recv(1024)
    if inp == 'done':
           cursor = conn.execute("UPDATE files_list SET status = 'unlocked' WHERE file_name = (?)",(f_name,))
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
