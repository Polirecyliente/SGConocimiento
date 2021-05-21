/*
    Abstract classes, interfaces
*/

//T// create abstract classes and methods with the abstract keyword
abstract class AbsCl1
{
    abstract void fun1();
}

//T// create an interface with the interface keyword
interface InterF1
{
    void fun2();
}

public class Section1_15 extends AbsCl1 implements InterF1
{
//T// override abstract methods
    void fun1()
    {
        System.out.println("Implemented from abstract class");
    }
//T// override interface methods
    public void fun2()
    {
        System.out.println("Implemented from interface");
    }
    public static void main(String args[])
    {
//T// create an abstract or interface reference to a concrete object
        AbsCl1 o1 = new Section1_15();
        o1.fun1();
        InterF1 o2 = new Section1_15();
        o2.fun2();
    }
}