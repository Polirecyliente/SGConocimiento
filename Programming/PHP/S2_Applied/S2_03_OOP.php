<!--
    OOP
-->

<html>
    <head><title>OOP</title></head>
    <body>
    <?php
//T// OOP stands for Object Oriented Programming

//T// define a class with the class keyword
        class FirstClass
        {

//T// define a public variable with the public keyword
            public $attr1 = "publicStr";

//T// make a class member private to make it accessible only to the class
            private $attr2 = "privateStr";

//T// make a class member protected to give access only to childs and package
            protected $attr3 = "protectedStr";

//T// define class methods
            function setAttr1($newA1)
            {
                $this->attr1 = $newA1;
            }
            function getAttr1()
            {
                return $this->attr1;
            }

            public $varEx1;
//T// define the constructor with __construct()
            function __construct($arg1)
            {
                $this->varEx1 = $arg1;
            }

//T// define the destructor with __destruct()
            function __destruct()
            {
                print("Object of ". __CLASS__ ." has been destroyed.<br/>");
            }

//T// create a method to get a private attribute
            function getPriv1()
            {
                return $this->attr2;
            }

//T// make members accessible without objects with the static keyword
            static $attr4 = "staticStr";

//T// methods and classes can't be overridden with the final keyword
            final function finalFunc1()
            {
                print("Unchanging code<br/>");
            }
        }

//T// create objects with the new keyword
        $Obj1 = new FirstClass("str1");
        $Obj1->setAttr1(86);
        print("Obj1 attribute one is ".$Obj1->getAttr1()."<br/>");

//T// inherit from another class with the extends keyword
        class ChildClass extends FirstClass
        {

//T// override inherited method
            function getAttr1()
            {
                $loc1 = $this->attr1;
                print("Attribute one is ".$loc1);
                return $loc1;
            }
            function getProtec1()
            {
                return $this->attr3;
            }
        }

        ini_set('display_errors',1);
        ini_set('display_startup_errors',1);
        $Obj2 = new FirstClass("argStr");
        print("PublicTest: ".$Obj2->attr1."<br/>");
        print("PrivateTest: ".$Obj2->getPriv1()."<br/>");
        $Obj2Ch = new ChildClass("argCh");
        print("ProtectedTest: ".$Obj2Ch->getProtec1()."<br/>");

//T// create an interface with the interface keyword
        interface Interf1
        {
            public function interfFun1();
        }

//T// implement an interface with the implements keyword
        class ImplemClass implements Interf1
        {

//T// create constants with the const keyword
            const firstConsNoDollar = 5;

            function func1(){return 1;}
            function interfFun1(){return 2*25;}
        }
        
//T// create abstract classes with the abstract keyword
        abstract class AbstClass
        {

//T// abstract functions must be implemented by child classes
            abstract function abstFun();
        }

//T// access static members with ::
        print("StaticTest: ".FirstClass::$attr4."<br/>");

    ?>
    </body>
</html>