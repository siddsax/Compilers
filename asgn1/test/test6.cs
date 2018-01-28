// Assembly1.cs  
// Compile with: /target:library  
public class BaseClass
{
    private int myValue = 0;
}

public class DerivedClass1
{
    void Access()
    {
        BaseClass baseObject = new BaseClass(arg1);

        // Error CS1540, because myValue can only be accessed by
        // classes derived from BaseClass.
        // baseObject.myValue = 5;  

        // OK, accessed through the current derived class instance
        myValue = 5;
    }
}
