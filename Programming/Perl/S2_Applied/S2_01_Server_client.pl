#!/usr/bin/perl
#   Server client

#T# Server socket

use Socket;

#T# create server socket with socket(), PF_INET is the constant for the Protocol Family of InterNET, getprotobyname() gets protocol by name
socket(SERVERSOCKETFH,PF_INET,SOCK_STREAM,(getprotobyname('tcp'))[2])
or die("can't make server socket, $!");

#T# bind the socket with an IP and port with bind()
bind(SERVERSOCKETFH,pack_sockaddr_in(55567,inet_aton("127.0.0.1"))) 
or die("can't bind server socket, $!");

#T# listen to N simultaneous connections with listen(FH,N)
listen(SERVERSOCKETFH,2) or tydie("server socket can't listen, $!");

#T# accept incoming connection (only once) with accept()
accept(COMM_SOCKET,SERVERSOCKETFH);

#T# print to the client socket file handle and close it
print COMM_SOCKET "Communication made\n";
close(COMM_SOCKET);

close(SERVERSOCKETFH) or die("Cant close the server socket, $!");
print "Server Ended\n";