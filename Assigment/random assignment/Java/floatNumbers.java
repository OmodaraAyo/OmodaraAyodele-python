import java.util.Scanner;
public class floatNumbers {

	public static void main (String...args){
	Scanner input = new Scanner(System.in);

	System.out.print("Enter a number: ");
	int firstNumber = input.nextInt();

	System.out.print("Enter a number: ");
	int secondNumber = input.nextInt();

	result = MathTool.onlyFloat(firstNumber, secondNumber);
	System.out.println(result);


 }
}