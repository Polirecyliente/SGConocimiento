/*
    Arrays
*/

import java.util.Arrays;

public class Section1_11
{
//T// arrays in functions
    static int[] fun1(int[] a1)
    {
        int[] ret;
        for(int el:a1)
        {
            System.out.println("Element is: "+el);
        }
//T// sort array's elements with sort()
        Arrays.sort(a1);
        ret = a1;
        return ret;
    }
    public static void main(String args[])
    {
//T// ways to declare arrays
        int[] arr1 = {72,1,3};
        int[] arr2;
        arr2 = new int[3];
        int[] arr3 = new int[4];

//T// arrays as arguments
        arr2 = fun1(arr1);
        fun1(new int[]{12,24,6});
        fun1(arr2);
    }
}