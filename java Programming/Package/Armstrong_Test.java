//Checking armstrong number using OwnPackage. (it is used to create userdefine package, which we can reuse several times infuture by importing own package)
import OwnPackage.*;    //importing ArmstrongPackage class from OwnPackage

public class Armstrong_Test {
    public static void main(String[] args) {
        ArmstrongPackage obj = new ArmstrongPackage();
        obj.armstrong(121);
    }
}