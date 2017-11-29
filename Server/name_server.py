import socket, pickle
from threading import Thread
import threading
import os
from threading import Thread

class client_thread(Thread):

       def __init__(self,addr,c):
              Thread.__init__(self)
              self.addr = addr
              self.c = c

       def run(self):
              while True:
                     get_list(self.addr,self.c)
              

def get_list(name,sock):
    current_working_directory = os.getcwd()
    os.chdir(current_working_directory)
    files =[]
    d1=[]
    files = os.listdir(current_working_directory)
    f_name = sock.recv(2048)        
    if f_name in files:
        i=files.index(f_name)
        data = current_working_directory+f_name+' Size '+str(os.path.getsize(files[i]))+' Bytes  Last modified ' +str(os.path.getctime(files[i]))      
    else:
        data = 'File does not exist'
    data1 = data.encode()
    sock.send(data1)
    


def Main():
    host = '127.0.0.1'
    port = 5000
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
    

        

    



    
