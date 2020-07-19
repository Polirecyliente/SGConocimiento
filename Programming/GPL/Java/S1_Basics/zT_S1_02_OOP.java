/*
    OOP
*/

//T// OOP stands for Object Oriented Programming

//T// import statement
import java.io.*;

//T// class
class Obj1
{
//T// instance variable;
    int ins1;

//T// class variable
    static int cla1;

//T// method
    int method1()
    {
//T// local variable
        int loc1 = 5;
        return loc1;
    }
//T// constructor
    public Obj1(int a1)
    {
        ins1 = a1;
    }
}

public class Section1_2
{
//T// object declaration and instantiation
    Obj1 nObj1 = new Obj1(67);
    
//T// access an instance variables or methods with . (dot)
    int objVal = nObj1.ins1;
}