/*
    Multithreading
*/

#include <iostream>
#include <unistd.h>

//T// include the headers to create threads pthread
#include <pthread.h>

using namespace std;

void* threadWork1(void* threadIDarg)
{
    long tid;
    tid = (long)threadIDarg;
    cout << "Executing thread " << tid << "\n";

//T// exit a thread with pthread_exit()
    pthread_exit(NULL);
}

int main()
{
    int numThreads = 7;

//T// create threads with the pthread_t type
    pthread_t threads[numThreads];

    for (int i1 = 72;i1 < numThreads + 72;i1++)
    {
        cout << "in main\n";

//T// relate the threads to the functions they execute with pthread_create()
        pthread_create(&threads[i1],NULL,threadWork1,(void *)i1);
    }

    pthread_exit(NULL);
}