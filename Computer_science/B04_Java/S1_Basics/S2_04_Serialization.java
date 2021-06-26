/*
    Serialization
*/

import java.io.IOException;

//T// import the Serializable interface
import java.io.Serializable;

//T// import the classes to serialize: FileOutputStream and ObjectOutputStream
import java.io.FileOutputStream;
import java.io.ObjectOutputStream;

//T// import the classes to deserialize: FileInputStream and ObjectInputStream
import java.io.FileInputStream;
import java.io.ObjectInputStream;

//T// serialize objects from a class that implements Serializable
class SerialCl1 implements Serializable
{
    public int i1;

//T// do not serialize a variable in the object with the transient keyword
    public transient int i2;
}

public class Section2_4
{
    public static void main(String args[])
    {
        SerialCl1 o1 = new SerialCl1();
        o1.i1 = 72;
        o1.i2 = 599;

        String fName1;
        fName1 = "PolirecylBases/"
        +"tutos/Java/Section2/Section2_4Aux.ser";

        try
        {
//T// create a FileOutputStream object, and an ObjectOutputStream object
            FileOutputStream fileWr1 = new FileOutputStream(fName1);
            ObjectOutputStream objWr1 = new ObjectOutputStream(fileWr1);

//T// write the serialized object to disk with writeObject()
            objWr1.writeObject(o1);

//T// close output streams with close()
            objWr1.close();
            fileWr1.close();
        }
        catch (IOException exc1)
        {
            System.out.println("Can't create serialized file");
            exc1.printStackTrace();
        }

//T// deserialize object with this syntax
        SerialCl1 deSerObj1 = null;
        try
        {
//T// create a FileInputStream object, and an ObjectInputStream object
            FileInputStream fileRe1 = new FileInputStream(fName1);
            ObjectInputStream objRe1 = new ObjectInputStream(fileRe1);

//T// deserialize the object with readObject()
            deSerObj1 = (SerialCl1) objRe1.readObject();

//T// close input objects with close()
            objRe1.close();
            fileRe1.close();
        }
        catch (IOException exc1)
        {
            System.out.println("Can't read serialized file");
            exc1.printStackTrace();
        }
        catch (ClassNotFoundException exc2)
        {
            System.out.println("Class file for SerialCl1 not found");
            exc2.printStackTrace();
        }

        System.out.println("Deserialized data: "+deSerObj1.i1+
        " and "+deSerObj1.i2);
    }
}