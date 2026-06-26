//Displaying output from OwnPackage. (it is used to create userdefine package)
import OwnPackage.msg1;
import OwnPackage.msg2;
class msg_display_from_OwnPackage{
	public static void main(String args[]){
		msg1 a1=new msg1();
		msg2 b1=new msg2();
		a1.display();
		b1.display();
	}
}