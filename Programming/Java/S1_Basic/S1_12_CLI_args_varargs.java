/*
    CLI args, varargs
*/

public class Section1_12
{

//T// varargs with ellipsis ...
    static void fun1(int... a1)
    {
        for(int el:a1)
        {
            System.out.println("In ellipsis: "+el);
        }
    }
    public static void main(String args[])
    {
//T// access command line arguments in args[]
        System.out.println("First argument: "+args[0]);
        fun1(4,22);
    }
}