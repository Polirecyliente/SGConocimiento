/*
    Operators
*/

public class Section1_6
{
    public static void main(String args[])
    {
        float i1 = 5;
        float i2 = 7;
//T// arithmetic operators
        System.out.println("Sum "+(i1+i2));
        System.out.println("Difference "+(i1-i2));
        System.out.println("Multiplication "+(i1*i2));
        System.out.println("Division "+(i2/i1));
        System.out.println("Modulo "+(i2%i1));
        System.out.println("Increment "+(++i1));
        System.out.println("Decrement "+(--i1));

//T// relational operators
        System.out.println();
        System.out.println("Equals "+(i2==i1));
        System.out.println("Not equals "+(i2!=i1));
        System.out.println("Greater than "+(i2>i1));
        System.out.println("Less than "+(i2<i1));
        System.out.println("Greater than or equal to "+(i2>=i1));
        System.out.println("Less than or equal to "+(i2<=i1));

        int b1 = 0x00C98011, b2 = 0x00362057;
//T// bitwise operators
        System.out.println();
        System.out.println("AND "+(b1&b2)); //0X00000011 -> 17
        System.out.println("OR "+(b1|b2)); //0X00FFA057 -> 16752727
        System.out.println("XOR "+(b1^b2)); //0X00FFA046 -> 16752710
        System.out.println("NOT "+(~b1)); //0XFF367FEE or 0xFFFFFFFFFF367FEE
                                    //-> 4281761774 or 18446744073696346094
        System.out.println("Left shift "+(b1<<3)); //0X064C0088 -> 105644168
        System.out.println("Right shift "+(b1>>>1)); //0X0064C008 -> 6602760

        boolean bo1 = true, bo2 = false;
//T// logical operators
        System.out.println();
        System.out.println("And "+(bo1&&bo2));
        System.out.println("Or "+(bo1||bo2));
        System.out.println("Not "+(!bo2));

//T// assignment operators
        System.out.println();
        System.out.println("Equals "+(i1=i2));
        System.out.println("Plus equals "+(i1+=i2));
        System.out.println("Minus equals "+(i1-=i2));
        System.out.println("Times equals "+(i1*=i2));
        System.out.println("Divide equals "+(i1/=i2));
        System.out.println("Modulo equals "+(i1%=i2));
        System.out.println("Left shift equals "+(b1<<=1));
        System.out.println("Right shift equals "+(b1>>=1));
        System.out.println("And equals "+(b1&=b2));
        System.out.println("Or equals "+(b1|=b2));
        System.out.println("Xor equals "+(b1^=b2));

//T// ternary operator
        System.out.println("Ternary op: "+((5>7)?"Yes":"No"));

        Section1_6 o1 = new Section1_6();
//T// instanceof
        System.out.println("Instanceof "+(o1 instanceof Section1_6));
    }
}