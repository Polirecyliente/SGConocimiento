/*
    Collections
*/

//T// import the Collections interface
import java.util.Collections;

//T// import the Iterator interface
import java.util.Iterator;

//T// import a Collection implementation as LinkedList
import java.util.LinkedList;

//T// import the Comparator interface
import java.util.Comparator;

public class Section2_2
{
    public static void main(String args[])
    {
//T// determine the type of the collection's elements within <>
        LinkedList<String> ll1 = new LinkedList<String>();

//T// add elements to the LinkedList with add()
        ll1.add("strEl1");
        ll1.add(0,"strEl2");
        ll1.addLast("ExtraEl3");

//T// remove elements from the LinkedList with remove()
        ll1.remove("ExtraEl3");

//T// set and get a given value in the LinkedList with set(), get()
        ll1.set(1,"NewStr");
        String s1 = ll1.get(1);

        System.out.println("LinkedL contents: "+ll1);

        ComparCl1 comp1 = new ComparCl1();

//T// sort according to a Comparator object with sort()
        Collections.sort(ll1, comp1);
        System.out.println("sorted: "+ll1);

//T// create an Iterator for the LinkedList with iterator()
        Iterator iter1 = ll1.iterator();

//T// loop LinkedList with hasNext()
        while (iter1.hasNext())
        {
//T// go to the next element in the LinkedList with next()
            System.out.println("Element is "+iter1.next());
        }
    }
}

//T// create a class that implements the Comparator interface
class ComparCl1<String> implements Comparator<String>
{
    public int compare(Object a1,Object a2)
    {
        return a1.toString().compareTo(a2.toString());
    }
}