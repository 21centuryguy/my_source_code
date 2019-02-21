class Switch {

	public static void main(String[] args) {

		int x = Integer.parseInt(args[0]);

		switch(x){
			case 1 : System.out.println("The number you typed is 1."); break;
			case 2 : System.out.println("The number you typed is 2"); break;
			case 3 : System.out.println("The number you typed is 3"); break;
			case 4 : System.out.println("The number you typed is 4"); break;
			case 5 : System.out.println("The number you typed is 5"); break;
			case 6 : System.out.println("The number you typed is 6"); break;
			case 7 : System.out.println("The number you typed is 7"); break;
			case 8 : System.out.println("The number you typed is 8"); break;
			case 9 : System.out.println("The number you typed is 9"); break;
			default: System.out.println("You should type a number between 1-9"); break;

		}
	}
}
