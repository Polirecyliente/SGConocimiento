/*
    Decision making
*/

public class Section1_8
{
    public static void main(String args[])
    {
        int i1 = 11;
//T// if, else if, else statement
        if (i1 < 10)
        {
            System.out.println("Value is less than ten");
        }else if (i1 == 10)
        {
            System.out.println("Value is ten");
        }else
        {
            System.out.println("Value is greater than ten");
        }

//T// switch, case, default statement
        switch (i1)
        {
            case 1:
                System.out.println("Value 1");
                break;
            case 11:
                System.out.println("Value 11");
                break;
            default:
                System.out.println("Other value");
        }
        
    }
}