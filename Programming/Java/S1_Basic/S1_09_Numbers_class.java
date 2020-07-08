/*
    Numbers class
*/

public class Section1_9
{
    public static void main(String args[])
    {
//T// wrapper classes for primitive types
        Byte byO1 = 5;
        Short shO1 = 12;
        Short shO2 = 12;
        Integer iO1 = 79;
        Long lO1 = 140l;
        Float fO1 = 4.91f;
        Double dO1 = 23.4;

//T// convert a number to another class with classValue()
        System.out.println("iO1 to double: "+iO1.doubleValue());

//T// make comparisons with compareTo()
        System.out.println("iO1 compared to 80: "+iO1.compareTo(80));

//T// test for equality with equals()
        System.out.println("shO1 == shO2? "+shO1.equals(shO2));

//T// return string as number with valueOf()
        System.out.println("str as num: "+Float.valueOf("11"));

//T// return number as string with toString()
        System.out.println("num as str: "+dO1.toString());

//T// get absolute value with abs()
        System.out.println("abs of lO1: "+Math.abs(lO1));

//T// get arc from catheti with atan2()
        System.out.println("arc: "+Math.atan2(byO1,fO1));

//T// get random number with random()
        System.out.println("rand: "+Math.random());
    }
}