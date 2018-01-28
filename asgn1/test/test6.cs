// Assembly1.cs  
// Compile with: /target:library  
/* test
 * new */
/* skjflsjdflj */
public class BaseClass
{
    private int myValue = 0;
}

public class DerivedClass1
{
    void Access()
    {
        t1:
        BaseClass baseObject = new BaseClass(arg1);

        // Error CS1540, because myValue can only be accessed by
        // classes derived from BaseClass.
        // baseObject.myValue = 5;  
        goto t1;

        // OK, accessed through the current derived class instance
        myValue = 5;
    }
}
