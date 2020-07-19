
#   Client socket

#T# socket module
use Socket;

#T# create client socket with socket()
socket(CLIENTSOCKETFH,PF_INET,SOCK_STREAM,(getprotobyname('tcp'))[2])
or die("can't make client socket: $!");

#T# connect client socket to server socket with connect(), pack_sockaddr_in() returns port and IP address combined, inet_aton() converts ASCII string of IP to Network
connect(CLIENTSOCKETFH,pack_sockaddr_in(55567,inet_aton("127.0.0.1")))
or die("Can't connect client socket to server socket: $!");

my $var1;
#T# print whatever the server writes to the file handle of the client
while ($var1 = <CLIENTSOCKETFH>)
{
    print "$var1\n";
}

close(CLIENTSOCKETFH) or die("can't close client socket: $!");
print "Client Ended\n";