class Scope {

	// public static String txt = "Class string"; // global variable

	public static final String txt = "Class string"; // global variable

	public static void main (String[] args) {

		String txt = "Main method string"; // main method variable

		System.out.println(Scope.txt); // print global variable
		System.out.println(txt); // print main method variable
		sec();

	}

	public static void sec() {

		String txt = "Second method string"; // second method variable
		System.out.println(txt); // print second method variable


	}

}