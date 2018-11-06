class AgeCalc2 {
	public static void main(String[] args) {

		int yob = Integer.parseInt(args[1]);
		int current = Integer.parseInt(args[0]);
		int age = current - yob;
		boolean hadBday = Boolean.parseBoolean(args[2]);
		
		if(hadBday){
		 System.out.println("You've already had your britthday.");

		} 

		else {
			age--;
			System.out.println("You've not had your britthday.");
		}

		System.out.println("You are " + age + " years old !");

	}
}