/*
    Functions
*/

public class S1_06_Functions{

//T// varargs

//T// varargs with ellipsis ...
    static void fun1(int... a1)
    {
        for(int el:a1)
        {
            System.out.println("In ellipsis: "+el);
        }
    }
}