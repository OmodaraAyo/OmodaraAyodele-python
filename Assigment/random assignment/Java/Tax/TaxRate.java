public class TaxRate {

	public static float singletaxcalculator(float taxableIncome){
	
		if (taxableIncome <= 0 ){
			return 0;
		}
	
		else if (taxableIncome > 0 && taxableIncome <= 8350){
			return taxableIncome * 10/100;

		}

		else if (taxableIncome > 8350 && taxableIncome <= 33950){

			return taxableIncome * 15/100;
		}
		
		else if (taxableIncome > 33950 && taxableIncome <= 82250){

			return taxableIncome * 25/100;
		}

		else if (taxableIncome > 82250 && taxableIncome <= 171550){

			return taxableIncome * 28/100;
		}

		else if (taxableIncome > 171550 && taxableIncome <= 372950){

			return taxableIncome * 33/100;
		}
	
		else if (taxableIncome > 372950){

			return taxableIncome * 35/100;
		}

		else{
			System.out.print ("Wrong Input");
			return 0;
		}

	}


	public static float marriedFillingJointly(float taxableIncome){

		if (taxableIncome < 0){
			return 0;	
		}

		else if (taxableIncome > 0 && taxableIncome <= 16700){
			
			return taxableIncome * 10/100;
		}
		
		else if (taxableIncome > 16700 && taxableIncome <= 67900){
			
			return taxableIncome * 15/100;
		}

		
		else if (taxableIncome > 67900 && taxableIncome <= 137050){
			
			return taxableIncome * 25/100;
		}
		
		
		else if (taxableIncome > 137050 && taxableIncome <= 208850){
			
			return taxableIncome * 28/100;
		}
		
		
		else if (taxableIncome > 208850 && taxableIncome <= 372950){
			
			return taxableIncome * 33/100;
		}

		
		else if (taxableIncome > 372950 ){
			
			return taxableIncome * 35/100;
		}

		else {
	
			return 0;
		}

	}

	public static float marriedFillingSeparately(float taxableIncome){

		if (taxableIncome < 0){
			return 0;	
		}

		else if (taxableIncome > 0 && taxableIncome <= 8350){
			
			return taxableIncome * 10/100;
		}
		
		else if (taxableIncome > 8350 && taxableIncome <= 33950){
			
			return taxableIncome * 15/100;
		}

		
		else if (taxableIncome > 33950 && taxableIncome <= 68525){
			
			return taxableIncome * 25/100;
		}
		
		
		else if (taxableIncome > 68525 && taxableIncome <= 104425){
			
			return taxableIncome * 28/100;
		}
		
		
		else if (taxableIncome > 104425 && taxableIncome <= 186475){
			
			return taxableIncome * 33/100;
		}

		
		else if (taxableIncome > 186475 ){
			
			return taxableIncome * 35/100;
		}

		else {
	
			return 0;
		}
	}

	public static float headOfHouseHold(float taxableIncome){

		if (taxableIncome < 0){
			return 0;	
		}

		else if (taxableIncome > 0 && taxableIncome <= 11950){
			
			return taxableIncome * 10/100;
		}
		
		else if (taxableIncome > 11950 && taxableIncome <= 45500){
			
			return taxableIncome * 15/100;
		}

		
		else if (taxableIncome > 45500 && taxableIncome <= 117450){
			
			return taxableIncome * 25/100;
		}
		
		
		else if (taxableIncome > 117450 && taxableIncome <= 190200){
			
			return taxableIncome * 28/100;
		}
		
		
		else if (taxableIncome > 190201 && taxableIncome <= 372950){
			
			return taxableIncome * 33/100;
		}

		
		else if (taxableIncome > 372950 ){
			
			return taxableIncome * 35/100;
		}

		else {
	
			return 0;
		}
	}

}