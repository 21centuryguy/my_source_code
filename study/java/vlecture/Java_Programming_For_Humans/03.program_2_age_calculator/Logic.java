class Logic{

	public static void main(String[] args){

		//boolean a = true;
		//boolean b = false;

		//boolean a = true;
		//boolean b = true;

		//boolean a = false;
		//boolean b = true;

		boolean a = false;
		boolean b = false;

		if ( (a) && (b) ) {

			System.out.println("a and b are true");
		
		} else {

			System.out.println("a and b are not true");
		}

		if ( (a) || (b) ){
			System.out.println("a or b is true");
		
		}else {

			System.out.println("a or b is not true");
		}

		if ( (!a) && (!b) ) {

			System.out.println("a and b are false");
		
		}else {

			System.out.println("a and b are not false");
		}

		if ( (!a) || (!b) ){
			System.out.println("a or b is false");
		
		}else {

			System.out.println("a or b is not false");
		}

	}
}
