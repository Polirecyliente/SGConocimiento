/*
    Templates
*/

//T// generics as templates

public class Section2_3
{
//T// write the generic type's name within <>
    <Type1> void fun1(Type1 a1)
    {
        System.out.println("Printing type1: "+a1);
    }
    public static void main(String args[])
    {
        Section2_3 o1 = new Section2_3();
        Integer i1 = 6;
        String s1 = "str";

//T// call the generic function with different types
        o1.fun1(i1);
        o1.fun1(s1);
        
    }
}