%{
    Exception handling
%}

#T# handle exceptions with the try catch end_try_catch block
try
    A = input("Enter a nonexistant var to trigger try catch\n");
catch error1

#T# get the error identifier and its message
    printf("The error identifier is: %s\n",error1.identifier);
    printf("The error message is: %s\n",error1.message);
end_try_catch