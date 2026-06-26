//Checking palindrome number using OwnPackage. (it is used to create userdefine package, which we can reuse several times infuture by importing own package)
import OwnPackage.*;    //importing all class from OwnPackage

public class palindromeTest {
    public static void main(String[] args) {
        PalindromePackage obj = new PalindromePackage();
        obj.palindrome(121);
    }
}