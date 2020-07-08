/*
    Inner classes, inheritance
*/

public class Section1_14
{
//T// create inner classes like regular classes inside a class
    private class innCl1
    {
        void clPrint1()
        {
            System.out.println("In inner class");
        }
    }

    innCl1 oAtrr1 = new innCl1();

    void fun1()
    {
        System.out.println("In fun1 Superclass");
    }

    public static void main(String args[])
    {
        Section1_14 o1 = new Section1_14();

//T// access methods of inner class
        o1.oAtrr1.clPrint1();

//T// instantiate an inner class object with this syntax
        Section1_14.innCl1 o2 = o1.new innCl1();
        o2.clPrint1();

        ChiCl1 subO1 = new ChiCl1();
        subO1.fun1();
        subO1.fun1SUP();
    }
}

//T// inherit from another class with the extends keyword
class ChiCl1 extends Section1_14
{
//T// override super class methods
    void fun1()
    {
        System.out.println("In fun1 SUB class");
    }

    void fun1SUP()
    {
//T// use a parent member with the super keyword
        super.fun1();
    }
}