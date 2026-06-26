//MaxOfThreeNumber can be accessible and operable from any other class by including OwnPackage
package OwnPackage;
public class MaxOfThreeNumber{
	public void max3(int x, int y, int z){
		if(x>y && x>z){
			System.out.println("maximum is " + x);
		}
		else if (y>x && y>z){
			System.out.println("maximum is " + y);
		}
		else{
			System.out.println("maximum is " + z);
		}
	}
} 