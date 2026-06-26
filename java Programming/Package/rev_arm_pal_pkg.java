import java.io.*;

import OwnPackage.*; //importing ArmstrongPackage, PalindromePackage,ReverseNumber
class rev_arm_pal_pkg{
	public static void main(String args[])throws IOException{
		BufferedReader br= new BufferedReader( new InputStreamReader(System.in));
		int n;
		System.out.println("enter a number: ");	
		n=Integer.parseInt(br.readLine());	
		ReverseNumber r = new ReverseNumber();
		ArmstrongPackage a = new ArmstrongPackage();
		PalindromePackage p = new PalindromePackage();
		r.rev(n);
		a.armstrong(n);
		p.palindrome(n);
	}
}