import socket               # Import socket module

def directory():
    host = 'localhost'
    port = 5000
    s = socket.socket()
    s.connect((host, port))

    file_name = raw_input("Enter File Name, type exit to terminate: ")
    s.send(file_name.encode())
    data = s.recv(2048)
    data1 = data.decode()
    print data1
    file_name1 = raw_input("Type edit to modify file and exit to quit or back to open another file ")
    if file_name1 == 'edit':
        data2 = 'exit'
        s.send(data2.encode())
        fileserver(file_name)
        
    elif file_name1 == 'exit':
        file_name1.encode()
        s.send(file_name1.encode())
        print'Application Terminated'
    elif file_name1 == 'back':
        file_name = raw_input("Enter File Name, type exit to terminate: ")
        s.send(file_name.encode())
        data = s.recv(2048)
        data1 = data.decode()
        print data1
    s.close()

def fileserver(f):
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 5001               # Reserve a port for your service.

    s.connect((host, port))
    #received = s.recv(2048)
    #print received
    #remove = received[1:-1]
    #print remove
    #h = remove.split(", ")
    #f = h[2]
    #print f
    mode = ['r', 'a']
    #print mode[0]
    #g = [f, mode[0]]
    #g1 = g[0][1:-1]
    #print g1
    #g = [g1, mode[0]]
    #print g
    x = raw_input("What do you want to do? Type r for read or type a for appending the file ")

    if x == mode[0] :
        g = [f, mode[0]]
        s.send(str(g))
        with open('received_file', 'wb') as f1:
            print 'file opened'
            while True:
                print('receiving data...')
                data = s.recv(1024)

                if not data:
                    break
                    
                # write data to a file
            print data
                f1.write(data)
            f1.close()
    elif x == mode[1]:
        g = [f, mode[1]]
        s.send(str(g))
        data1 = raw_input("What do you want to write to file " + str(g))
        print "Modified content: " + str(data1)
        s.send(data1)
        print "Changes sent!"

                        # Close the socket when done

if __name__ == '__main__':
    directory()
    #fileserver()
