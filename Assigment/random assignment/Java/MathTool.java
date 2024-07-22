public class MathTool {

	public static int onlyFloat(float firstNumber, float secondNumber){

		if (firstNumber == type(float) && secondNumber == type(float)){
			
			return 2;
		}
		else if (firstNumber == type(float) && secondNumber != type(float)){

			return 1;
		}
		else if (firstNumber != type(float) && secondNumber == type(float)){

			return 1;
		}
		else if (firstNumber != type(float) && secondNumber != type(float)){

			return 0;
		}			

	} 


}