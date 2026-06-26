import java.io.*;

import OwnPackage.MaxOfTwoNumber;
import OwnPackage.MaxOfThreeNumber;
class maxnumpkg{
	public static void main(String args[])throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a,b,c;
		System.out.println("enter three numbers: ");	
		a=Integer.parseInt(br.readLine());
		b=Integer.parseInt(br.readLine());
		c=Integer.parseInt(br.readLine());
		MaxOfTwoNumber m1 = new MaxOfTwoNumber();
		MaxOfThreeNumber m2 = new MaxOfThreeNumber();
		m1.max2(a,b);	
		m2.max3(a,b,c);
	}
}