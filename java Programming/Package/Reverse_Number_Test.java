//Reversing a number using OwnPackage. (it can be used several times in future by importing own package)
import OwnPackage.ReverseNumber;    //importing ReverseNumber class from OwnPackage 

public class Reverse_Number_Test {
    public static void main(String[] args) {
        ReverseNumber obj = new ReverseNumber();
        obj.rev(12345);
    }
}