import socket, pickle
from threading import Thread
import threading
import os

def get_list(name,sock):
    current_working_directory = os.getcwd()
    os.chdir(current_working_directory)
    files =[]
    data=[]
    d1=[]
    files = os.listdir(current_working_directory)
    f_name = sock.recv(2048)
    
    
    if f_name in files:
        i=files.index(f_name)

        data = current_working_directory+f_name+' Size '+str(os.path.getsize(files[i]))+' Bytes  Last modified ' +str(os.path.getctime(files[i]))
        print(data)
        
        
    else:
        data1 = 'File does not exist'
        

    data1 = data.encode()
    sock.send(data1)
    


def Main():
    host = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.bind((host,port))
    s.listen(5)
    print('server started')
    while(True):
        c,addr = s.accept()
        print('client connected ip:'+str(addr))
        t= threading.Thread(target= get_list('get_list',c))
        t.start()
if __name__ == '__main__':
    Main()

        

    



    
