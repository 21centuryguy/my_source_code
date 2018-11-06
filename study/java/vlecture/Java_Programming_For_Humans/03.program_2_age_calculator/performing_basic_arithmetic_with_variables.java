public class performing_basic_arithmetic_with_variables{
	public static void main(String[] args){
		int a = 4096;
		int add = a+a;
		int sub = a-a;
		int multiply = a*a;
		int divide = a/a;
		int mod = a%a;

		System.out.println("My number is " + a);
		System.out.println(a + " added is " + add);
		System.out.println(a + " subtracted is " + sub);
		System.out.println(a + " multipled is " + multiply);
		System.out.println(a + " divided is " + divide);
		System.out.println(a + " divided has a remainder of " + mod);

	}
}