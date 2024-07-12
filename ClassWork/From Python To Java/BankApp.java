import java.util.Scanner;

public class BankApp {
	public static void main (String... args){
	Scanner input = new Scanner (System.in);

	System.out.print ("Press -1 to exit app or enter a number to perform a transaction...\n");
	System.out.print ("\n1. Deposit          2. Withdraw          3. Balance\n");
	System.out.print("Enter a number: ");
	int userInput = input.nextInt();

	int deposit = 0;
	int withdraw = 0;
	int balance = 0;
while (userInput != -1){
		
		if (userInput == 1){
			System.out.print("Deposit: $");
			deposit = input.nextInt();

			if (deposit == 0){
			System.out.print ("Enter a valid amount...\n");
			}else
			if (deposit > 0){
			balance += deposit;
			//System.out.printf("$%d",balance);
			System.out.print("\nSuccessful.\n");
			}
			else {
			System.out.print("Failed.\n");
			}
		}
	else
		if (userInput == 2){
			System.out.print("Withdraw: $");
			withdraw = input.nextInt();
			if(withdraw == 0){
				System.out.print("Enter a valid amount...\n");
			} else
			if (withdraw < 1){
				System.out.print("Not a valid amount...\n");	
			}else
			if (withdraw > balance){
				System.out.print("Incomplete Transaction");
				System.out.print("\nEnter amount within Account balance...\n");

			} else
			if (balance >= withdraw){
				balance = deposit - withdraw;
				//System.out.printf ("$%d\n",balance);
				System.out.print ("Successful.\n");
			}
		}
	else
		if (userInput == 3){
			
			if (balance < 0){
				System.out.print("");
			}else
			if (balance >= 0){
			System.out.printf ("Balance: $%d\n", balance);
			}
		}
			

		else {
			System.out.printf("Invalid selection\n");
		}
		System.out.print ("\n1. Deposit          2. Withdraw          3. Balance");
		System.out.print ("\nEnter a number: ");
		userInput = input.nextInt();
	}
if (userInput == -1){
	System.out.print ("App Closed.");
   }

}
}