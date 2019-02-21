class Random {

	public static void main (String[] args) {

		/*double rn = Math.random();
		float f = (float) rn;

		System.out.println(rn);
		System.out.println(f);*/		

		float rn = (float) Math.random();
		float m = rn*10;
		int x = (int) Math.ceil(m);

		System.out.println(rn);
		System.out.println(m);
		System.out.println(x);

	}
}