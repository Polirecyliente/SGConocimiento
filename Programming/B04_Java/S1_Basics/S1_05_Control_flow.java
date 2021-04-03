/*
    Control flow
*/

//T// Contents
//T// Decision making
//T// Loops

public class Section1_8
{
    public static void main(String args[])
    {

//T// Decision making

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

//T// Loops

int i1 = 5;
//T// while loop
        while (true)
        {
            System.out.println("Infinite while loop?");
            i1++;
            if (i1 == 7) break;
        }

//T// for loop
        for (i1=i1;i1<=10;i1++)
        {
            if (i1 == 8) continue;
            System.out.println("In for loop");
        }

//T// do while loop
        do
        {
            System.out.println("Do while loop");
        } while (i1 < 10);

        int[] arr1 = {6,2,38,3};
//T// for loop in array
        for(int i2:arr1)
        {
            System.out.println("Current value: "+i2);
        }
    }
}