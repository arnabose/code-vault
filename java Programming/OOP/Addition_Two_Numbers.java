//addition of two numbers in java using oop
import java.util.*;
class operation{
	void addition(){
		Scanner sc= new Scanner(System.in);
		System.out.print("Enter 1st number: ");
		int a = sc.nextInt();
		System.out.print("Enter 2nd number: ");
		int b = sc.nextInt();
		System.out.println("Addition is: " + (a+b));
	}
}
class Addition_Two_Numbers{
	public static void main(String args[]){
		operation obj = new operation();
		obj.addition();
	}
}