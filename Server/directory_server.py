import socket, pickle
from threading import Thread
import threading
import os


class client_thread(Thread):

       def __init__(self,addr,c):
              Thread.__init__(self)
              self.addr = addr
              self.c = c

       def run(self):
              while True:
                     get_list(self.addr,self.c)
              

def get_list(name,sock):
    
    inp = (sock.recv(2048)).decode()
    print inp
    
    if inp == '1':
           f_name = (sock.recv(2048)).decode()
           info = (sock.recv(2048)).decode()
           f = open(f_name,"w+")
           f.write(info)
           print('done')
           f.close()
    current_working_directory = os.getcwd()
    os.chdir(current_working_directory)
    files =[]
    d1=[]
    files = os.listdir(current_working_directory)
    data=pickle.dumps(files)
    
    if inp == '2':
           sock.send(data)
           f_name = sock.recv(2048)
           
           if f_name in files:
               i=files.index(f_name)
               data = current_working_directory+f_name+' Size '+str(os.path.getsize(files[i]))+' Bytes  Last modified ' +str(os.path.getctime(files[i]))      
           else:
               data = 'File does not exist'
           data = data.encode()
           
    else:
           data = 'program terminated'
    sock.send(data)
    


def Main():
    host = '127.0.0.1'
    port = 5001
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
    

        

    



    
