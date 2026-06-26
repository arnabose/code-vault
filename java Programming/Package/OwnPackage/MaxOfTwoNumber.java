//MaxOfTwoNumber can be accessible and operable from any other class by including OwnPackage
package OwnPackage;
public class MaxOfTwoNumber{
	public void max2(int x, int y){
		if(x>y){
			System.out.println("maximum is " + x);
		}
		else{
			System.out.println("maximum is " + y);
		}
	}
} 