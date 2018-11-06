class Arrays {

	public static void main (String[] args) {

		int x = Integer.parseInt(args[0]);		

		switch(x){

			case 1 :

				int[] intArr1 = {1, 2, 3};
				String[] strArr1 = {"Jack", "Uvmark", "Kim"};

				System.out.println(intArr1[0] + "," + intArr1[1] + "," + intArr1[2]);
				System.out.println(strArr1[0] + " " + strArr1[1] + " " + strArr1[2]);

				break;

			case 2 :

				int[] intArr2 = new int[3];
				intArr2[0] = 4;
				intArr2[1] = 5;
				intArr2[2] = 6;

				String[] strArr2 = new String[3];
				strArr2[0] = "Mac";
				strArr2[1] = "Kim";
				strArr2[2] = "Guyver";

				System.out.println(intArr2[0] + "," + intArr2[1] + "," + intArr2[2]);
				System.out.println(strArr2[0] + " " + strArr2[1] + " " + strArr2[2]);

				break;

		}

	}
}
