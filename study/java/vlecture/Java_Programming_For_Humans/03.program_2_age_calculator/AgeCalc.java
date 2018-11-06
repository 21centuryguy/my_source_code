class AgeCalc {
	public static void main(String[] args) {

		int yob = 1977;
		int current = 2018;
		int age = current - yob;
		boolean hadBday = true;
		
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