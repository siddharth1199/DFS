import socket, pickle       

def authentication():
    input1 = raw_input("Enter 1 to login, 2 to sign up: ")
    socket_authen.send(input1.encode())
    username = raw_input("Enter username: ")
    socket_authen.send(username.encode())
    password = raw_input("Enter password: ")
    socket_authen.send(password.encode())
    print(username, password, input1)
    
    
    
    val = (socket_authen.recv(1024)).decode()
    if val == 'true':
        directory()
    elif val == 'false':
        print 'Incorrect password'
        authentication()
    else:
        print 'Username already exists'
        authentication()

def directory():    
    inp = raw_input('Type 1 to create a new file, and 2 to access existing file ')
    if inp == '1':
        f_name = raw_input('enter file name ')        
        info = raw_input('Write data into file: ')
        socket_dir.send(f_name.encode())
        socket_dir.send(info.encode())
        
        data = socket_dir.recv(2048)
        files = pickle.loads(data)
        directory()
    else:
        file_name = raw_input("Enter File Name, type exit to terminate: ")
        socket_dir.send(file_name.encode())    
        data = socket_dir.recv(2048)
        data1 = data.decode()
        print data1
    file_name1 = raw_input("Type open to access file and exit to quit or back to open another file ")
    if file_name1 == 'open':
        data2 = 'exit'
        socket_dir.send(data2.encode())
        fileserver(file_name)
        
    elif file_name1 == 'exit':
        file_name1.encode()
        socket_dir.send(file_name1.encode())
        print'Application Terminated'
    elif file_name1 == 'back':
        file_name = raw_input("Enter File Name, type exit to terminate: ")
        socket_dir.send(file_name.encode())
        data = socket_dir.recv(2048)
        data1 = data.decode()
        print data1
    socket_dir.close()

def fileserver(f):
    
    status = lock(f)
    mode = ['r', 'a']
    if status == 'locked':
        q = raw_input ('File is locked for writing, only read mode avaliable. Type yes to continue or exit to quit ')
        if q == 'yes':
            x='r'
            if x == mode[0] :
                g = [f, mode[0]]
                socket_file.send(str(g))
                with open('received_file', 'wb') as f1:
                    print 'file opened'
                    while True:
                        print('receiving data...')
                        data = socket_file.recv(1024)
                        print data
                        if not data:
                            break
            
        f1.close()
    else:
        x= raw_input('File unlocked, read and write avaliable. Type r to read and a to append ')
        if(x == mode[1]):
            g = [f, mode[1]]
            socket_lock.send((str(g[0])).encode())            
            socket_file.send(str(g))
            data1 = raw_input("What do you want to write to file  " + str(g[0]))
            print "Modified content: " + str(data1)
            socket_file.send(data1)
            print "Changes sent!"
            socket_lock.send('done'.encode())
        else:
            g = [f, mode[0]]
            socket_file.send(str(g))
            with open('received_file', 'wb') as f1:
                print 'file opened'
                while True:
                    
                    print('receiving data...')
                    data = socket_file.recv(1024)
                    print data
                    if not data:                        
                        break
            

                        # Close the socket when done

def lock(file_name):    
    socket_lock.send(file_name.encode())
    status = socket_lock.recv(1024)
    print ('Status of file is : ' +str(status.decode()))
    return status




if __name__ == '__main__':
   
    host = 'localhost'
    port_dir = 5001
    socket_dir = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_dir.connect((host, port_dir))

    socket_file = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
    port_file = 5003              
    socket_file.connect((host, port_file))

    port_lock = 6002
    socket_lock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_lock.connect((host, port_lock))

    port_authen = 5009
    socket_authen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_authen.connect((host, port_authen))
    authentication()
    #fileserver()
