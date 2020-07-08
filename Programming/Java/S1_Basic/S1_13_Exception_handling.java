/*
    Exception handling
*/

import java.io.IOException;
import java.lang.ArrayIndexOutOfBoundsException;

public class Section1_13
{
    public static void main(String args[])
    {
//T// manage exceptions with the try, catch, finally block
        try
        {
            fun1();

//T// throw exceptions with the throw keyword
            throw new IOException();

        } catch (ArrayIndexOutOfBoundsException|IOException eO1)
        {
//T// get the message of an exception with getMessage()
            System.out.println("Message: "+eO1.getMessage());

//T// get the cause of an exception with getCause()
            System.out.println("Cause: "+eO1.getCause());

//T// print stack trace of an exception with printStackTrace()
            System.out.println("Stack trace: ");
            eO1.printStackTrace();
        } finally
        {
            System.out.println("This is always executed");
        }
    }

//T// state that a function may throw an exception with the throws keyword
    static void fun1() throws ArrayIndexOutOfBoundsException
    {
        int[] arr1 = {1,2,3};
        System.out.println("str"+arr1[34]);
    }
}