/*
    Strings
*/

public class Section1_10
{
    public static void main(String args[])
    {
//T// strings are objects of the class String
        String s1 = "str";

//T// get the length of the string with length()
        System.out.println("String length is: "+s1.length());

//T// concatenate strings with concat()
        System.out.println(s1.concat("Concatenated"));

//T// save a formatted string with format()
        String savedFmt1 = String.format("String and %d args %f",2,3.1);
        System.out.println("Formated str: "+savedFmt1);

//T// get the char at a given position from a string with charAt()
        System.out.println("Char at pos 2: "+s1.charAt(2));

//T// convert from string to char array with toCharArray()
        String s2 = "Rather Long String In Comparison";
        char[] cArr1 = s2.toCharArray();

//T// copy a segment of a char array into a string with copyValueOf()
        String s3 = String.copyValueOf(cArr1,3,10);
        System.out.println("Copied val: "+s3);

//T// get an int hash code for a string with hashCode()
        System.out.println("Hash from s2: "+s2.hashCode());
    }
}