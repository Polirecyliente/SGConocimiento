/*
    Constructors
*/

class ConsCl1
{
    int i1;
    String s1;

//T// parameterized constructor syntax
    ConsCl1(int a1, String a2)
    {
//T// get a reference to calling object with the this keyword
        this.i1 = a1;
        this.s1 = a2;
    }
}

public class Section1_3
{
    public static void main(String args[])
    {
//T// create a new object with parameters in the constructor
        ConsCl1 o1 = new ConsCl1(5, "str1");
        System.out.println("From constructor: " + o1.i1 + " and " + o1.s1);
    }
}