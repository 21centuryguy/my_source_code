class Casting {

	public static void main (String[] args) {

		String numStr = "97.1234123412341234";
		double numDbl = Double.parseDouble(numStr);
		float numFlt = (float) numDbl;
		int numInt = (int) numFlt;

		System.out.println(numStr);
		System.out.println(numDbl);
		System.out.println(numFlt);
		System.out.println(numInt);

	}
}
