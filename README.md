# DFS
A simple distributed file system written in Python

Run all the server files and then run the client file

The components are as follows:
File Server Provides access to files on the machine using a NFS style access model. It provides read and write access to the clients present in a directory (Obtained from the directory server).

Directory Server Responsible for mapping file names into identifiers used by the file system. Stores all files in a file server, which this server maintains the mapping of full file names to server fileneame mappings.

Lock Server A client asks the lock server for access to a file. Lock server checks the status of the file from an SQL database. If file is unlocked, then the client has read and write access. If file is locked, then the client has read access only. Files get locked when client has write access. Multiple clients cannot change access the file for writing at the same time.

Authentication Server Basic Server that checks a database to see if a correct Username and Password were provided.
I worked on the all the 4 servers (File server, Directory Server, Lock Server and Authentication server), and the client


Siddharth Sheshadri
17310763
