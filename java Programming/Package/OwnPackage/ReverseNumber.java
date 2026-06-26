//ReverseNumber can be accessible from any other class by including OwnPackage
package OwnPackage;
public class ReverseNumber{
	public void rev(int n){
		int a,s=0;
		while(n>0){
			a=n%10;
			n=n/10;
			s=s*10+a;
		}
		System.out.println("reverse is " + s);	
	}
}