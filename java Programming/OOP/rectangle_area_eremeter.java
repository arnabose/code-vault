//area and perimeter of rectangle using java
import java.util.*;
class calculate_rectangle{
	void area_perimeter(){
		Scanner sc= new Scanner(System.in);
		System.out.print("Enter length of rectangle: ");
		double l = sc.nextDouble();
		System.out.print("Enter breadth of rectangle: ");
		double b = sc.nextDouble();
		System.out.println("Area of rectangle = " + (l*b));
		double p= 2*(l+b);
		System.out.println("Perimeter of rectangle = " + p);
	}
}
class rectangle_area_peremeter{
	public static void main(String args[]){
		calculate_rectangle obj = new calculate_rectangle();
		obj.area_perimeter();
	}
}