/*
    Signal handling
*/

#include <iostream>
#include <unistd.h>

//T// include the signal handling library csignal
#include <csignal>

using namespace std;

void responseToSIGINT1(int signum)
{
    cout << "Signal " << signum << " received, exiting.\n";
    exit(signum);
}

int main()
{
//T// register a function as a signal handler with signal()
    signal(SIGINT,responseToSIGINT1);
    int i = 0;
    while(true)
    {
        cout << "In normal process\n";
        sleep(1);
        if (i == 2)
        {
//T// raise a signal with raise()
            raise(SIGINT);
        }
        i++;
    }
    return 0;
}