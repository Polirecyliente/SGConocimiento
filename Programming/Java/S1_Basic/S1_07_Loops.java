/*
    Loops
*/

public class Section1_7
{
    public static void main(String args[])
    {
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