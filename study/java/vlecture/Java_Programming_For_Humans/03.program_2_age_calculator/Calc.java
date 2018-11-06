class Calc {

	public static void main(String[] args) {

		try {

			if (args.length == 0) {

				System.out.println("\nPROGRAM ERROR: You didn't enter any arguments!\n");

			} else if (args.length < 3) {

				System.out.println("\nPROGRAM ERROR: You passed fewer than 3 arguments.\n");

			} else if (args.length > 3) {

				System.out.println("\nPROGRAM ERROR: You passed more than 3 arguments.\n");

			} else {

				double a = Double.parseDouble(args[0]);
				double b = Double.parseDouble(args[2]);
				String op = args[1];

				// Product variables
				double p = a + b;
				double s = a - b;
				double m = a * b;
				double d = a / b;

				System.out.println("\n================");
				System.out.println("WELCOME TO CALC!");
				System.out.println("================");
				System.out.println("\nYou have enterd: " + a + " "+ op + " "+ b + "\n");

				switch( op) {

					case "+" :
					System.out.println("\n" + p + "\n");
					break;

					case "-" :
					System.out.println("\n" + s + "\n");
					break;

					case "x" :
					System.out.println("\n" + m + "\n");
					break;

					case "/" :
					System.out.println("\n" + d + "\n");
					break;

					default :
					System.out.println("You should type two numbers and one operatror.\n");

				}
			}

		} catch (NumberFormatException e) {

			System.out.println("\nPROGRAM ERROR");
			System.out.println("\nFirst and third agruments bust be numbers!");
			System.out.println("\nEXAMPLE: 2 + 2");
			System.out.println("\nERROR DETAILS: " + e + "\n");

		} catch (Exception e) {

			System.out.println("\nPROGRAM ERROR");
			throw e;

		}

	}

}