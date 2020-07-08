/*
    Modifiers
*/

//T// non access modifiers (3)
    abstract class Cl1{}

public class Section1_5
{
    static int i3 = 44;
    final int i4 = 328;
//T// access modifiers (3)
    private int i1 = 63;
    protected int i2 = 27;
    public static void main(String args[])
    {
        Section1_5 o1 = new Section1_5();
        System.out.println("Private value: "+o1.i1);
        System.out.println("Protected value: "+o1.i2);
        System.out.println("Static value: "+i3);
        System.out.println("Final value: "+o1.i4);
    }
}