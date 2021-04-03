/*
    Data structures
*/

//T// Data structure's superceded old interface is Enumeration
import java.util.Enumeration;

//T// Vector data structure
import java.util.Vector;

//T// BitSet data structure
import java.util.BitSet;

//T// Stack data structure
import java.util.Stack;

//T// Hashtable data structure
import java.util.Hashtable;

public class Section2_1
{
    public static void main(String args[])
    {
        Enumeration coll1;
        Vector elems = new Vector();
        BitSet bs1 = new BitSet(17);
        Stack st1 = new Stack();
        Hashtable ht1 = new Hashtable();

//T// add elements to a Vector object with add()
        elems.add("str1");
        elems.add(5.9);

//T// point Enumeration interface to a concrete data structure
        coll1 = elems.elements();

//T// scroll through all elements in a Vector with this syntax
        while (coll1.hasMoreElements())
        {
            System.out.println("Element in Vector is "+coll1.nextElement());
        }

//T// set the bits in a BitSet with set()
        for (int i1 = 0;i1<8;i1++)
        {
            bs1.set(i1);
        }

//T// get the bits in a BitSet with get()
        for (int i1 = 0;i1 < 17;i1++)
        {
            System.out.println("Bit in "+i1+" is "+bs1.get(i1));
        }

//T// push and pop in a Stack with push(), pop()
        st1.push("item1");
        System.out.println("Popping: "+st1.pop());

//T// put key-value pairs in a Hashtable with put()
        ht1.put("key1",6);
        ht1.put("k2", "val2");

//T// get the keys from a Hashtable with keys()
        Enumeration en1 = ht1.keys();

        while (en1.hasMoreElements())
        {
//T// get the value from a key with get()
            System.out.println("Value in key is "
            +ht1.get(en1.nextElement()));
        }

    }
}