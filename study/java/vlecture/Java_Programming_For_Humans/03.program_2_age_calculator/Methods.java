class Methods {

	public static void main (String[] args) {

		System.out.println("Welcom to the main method!");
		System.out.println("Numbers from the num method: ");

		num();
		num();
		num();
		num();

	}

	public static void num() {

		double x = Math.random();
		System.out.println(x);

	}
}