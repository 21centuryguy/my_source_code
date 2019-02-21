class Check_Arrays {

	public static void main (String[] args) {

		int x = Integer.parseInt(args[0]);		

		switch(x){

			case 1 :

				int[] intArr1 = {1, 2, 3};
				String[] strArr1 = {"Jack", "Uvmark", "Kim"};

				System.out.println(intArr1[0] + "," + intArr1[1] + "," + intArr1[2]);
				System.out.println(strArr1[0] + " " + strArr1[1] + " " + strArr1[2]);

				/*if (intArr1.contains(1)) {

					System.out.println("'1' IN intArr1[0] ^.^");
				
				} else {

					System.out.println("'1' NOT IN intArr1[0] -_-;");
				}*/


				//////////* contanis() check with string *//////////
				if (strArr1[0].contains("Mac")) {

					System.out.println("'Mac' IN strArr1[0] ^.^");
				
				} else {

					System.out.println("'Mac' NOT IN strArr1[0] -_-;");
				}


				//////////* boolean true false check *//////////
				boolean xxx = (strArr1[0].contains("Bauer"));
				if (xxx) {

					System.out.println("line 42 : "+xxx);
				} else {

					System.out.println("line 45 : "+xxx);
				}

				break;

			case 2 :

				int[] intArr2 = new int[3];
				intArr2[0] = 4;
				intArr2[1] = 5;
				intArr2[2] = 6;

				/*if (intArr2[0].contains(4)) {

					System.out.println("'4' in intArr2[0]");
				}*/

				//////////* contanis() check with string *//////////
				String[] strArr2 = new String[3];
				strArr2[0] = "Mac";
				strArr2[1] = "Kim";
				strArr2[2] = "Guyver";

				if (strArr2[0].contains("Mac")) {

					System.out.println("'Mac' in strArr2[0] ^.^");
				
				} else {

					System.out.println("'Mac' NOT IN strArr2[0] -_-;");
				}

				System.out.println(intArr2[0] + "," + intArr2[1] + "," + intArr2[2]);
				System.out.println(strArr2[0] + " " + strArr2[1] + " " + strArr2[2]);

				break;

		}

	}
}
