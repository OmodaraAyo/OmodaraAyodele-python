import java.util.Scanner;
public class UnitedStatesFederalPersonalIncomeTax {

	public static void main (String... args){
	Scanner input = new Scanner(System.in);

	System.out.print("\n");
	System.out.print("0. Single filers\n1. Married filling jointly\n2. Married filling separately\n3. Head of household\n");
	System.out.print("\nWhat is your status?: ");
	int userInput = input.nextInt();
while (userInput != 0 && userInput != 1 && userInput != 2 && userInput != 3){
	if (userInput < 0 || userInput >= 4){
		System.out.print("Wrong input! try again...\n");
	}
	System.out.print("\n");
	System.out.print("0. Single filers\n1. Married filling jointly\n2. Married filling separately\n3. Head of household\n");
	System.out.print("\nWhat is your status?: ");
	userInput = input.nextInt();

	}

	if (userInput == 0){
		System.out.print("Marginal Tax Rate	  Single\n");
		System.out.print("  10%			$0 - $8,350\n");
		System.out.print("  15%			$8,351 - $33,950\n");
		System.out.print("  25%			$33,951 - $82,250\n");
		System.out.print("  28%			$82,251 - $171,550\n");
		System.out.print("  33%			$171,551 - $372,950\n");
		System.out.print("  35%			$372,951+\n");
		System.out.print("\nTaxable income: $");
		float taxableIncome = input.nextFloat();
		while (taxableIncome < 0){
			System.out.print("Wrong input! try again...\n");
			System.out.print("\nTaxable income: $");
			taxableIncome = input.nextFloat();
		}
		float taxResult = TaxRate.singletaxcalculator(taxableIncome);
		System.out.println("Tax is $"+taxResult );
	}

	else if (userInput == 1){
		System.out.print("Marginal Tax Rate	Married filling jointly\n");
		System.out.print("  10%			$0 - $16,700\n");
		System.out.print("  15%			$16,701 - $67,900\n");
		System.out.print("  25%			$67,901 - $137,050\n");
		System.out.print("  28%			$137,051 - $208,850\n");
		System.out.print("  33%			$208,851 - $372,950\n");
		System.out.print("  35%			$372,951+\n");
		System.out.print("\nTaxable income: $");
		float taxableIncome = input.nextFloat();
		while (taxableIncome < 0){
			System.out.print("Wrong input! try again...\n");
			System.out.print("\nTaxable income: $");
			taxableIncome = input.nextFloat();
		}
		float taxResult = TaxRate.marriedFillingJointly(taxableIncome);
		System.out.println("Tax is $"+taxResult );			

	}

	else if (userInput == 2){
		System.out.print("Marginal Tax Rate	Married filling separately\n");
		System.out.print("  10%			$0 - $8,350\n");
		System.out.print("  15%			$8,351 - $33,950\n");
		System.out.print("  25%			$33,951 - $68,525\n");
		System.out.print("  28%			$68,526 - $104,425\n");
		System.out.print("  33%			$104,426 - $186,475\n");
		System.out.print("  35%			$186,476+\n");
		System.out.print("\nTaxable income: $");
		float taxableIncome = input.nextFloat();
		while (taxableIncome < 0){
			System.out.print("Wrong input! try again...\n");
			System.out.print("\nTaxable income: $");
			taxableIncome = input.nextFloat();
		}
		float taxResult = TaxRate.marriedFillingSeparately(taxableIncome);
		System.out.println("Tax is $"+taxResult );			

	}

	else if (userInput == 3){
		System.out.print("Marginal Tax Rate	Head of Household\n");
		System.out.print("  10%			$0 - $11,950\n");
		System.out.print("  15%			$11,951 - $45,500\n");
		System.out.print("  25%			$45,501 - $117,450\n");
		System.out.print("  28%			$117,451 - $190,200\n");
		System.out.print("  33%			$190,201 - $372,950\n");
		System.out.print("  35%			$372,951+\n");
		System.out.print("\nTaxable income: $");
		float taxableIncome = input.nextFloat();
		while (taxableIncome < 0){
			System.out.print("Wrong input! try again...\n");
			System.out.print("\nTaxable income: $");
			taxableIncome = input.nextFloat();
		}
		float taxResult = TaxRate.headOfHouseHold(taxableIncome);
		System.out.println("Tax is $"+taxResult );			

	}


}
}