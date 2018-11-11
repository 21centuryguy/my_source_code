class Rounding {

	public static void main (String[] args) {

		float myFloat = 7.2256f;

		int rounded = Math.round(myFloat);

		double down = Math.floor(myFloat);
		double up = Math.ceil(myFloat);

		int intDown = (int) down;
		int intUp = (int) up;

		System.out.println("Original number : "+ myFloat);
		System.out.println(myFloat + " rounded is : " + rounded);
		// System.out.println(down);
		// System.out.println(up);
		System.out.println(myFloat + " raised is : " + intUp);
		System.out.println(myFloat + " lowered is : " + intDown);

	}
}