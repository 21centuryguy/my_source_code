import java.util.Scanner;

class TicTacTg {
	
	// Array to hold the X or O in each space (Default value: '_')
	public static char[] place = { '_','_','_','_','_','_','_','_','_' };
	
	// Holds X or O, whichever team user chooses
	public static char team = '_';
	
	// Holds X or O, whichever team user does NOT choose!
	public static char opp = '_';
	
	// Variable to hold user input for Scanner
	public static String usrStr;

	public static void main (String[] args) {
	
		// Greeting message for user
		System.out.println("WELCOME TO TIC TAC TOE!");
		
		// Run the setup method
		setup();
			
	}
	
	public static void drawBoard() {
		

		// Draw the game board
		System.out.println("\n\t    A   B   C");
		System.out.println("\t  .-----------.");
		System.out.println("\t1 |_"+TicTacTg.place[0]+"_|_"+TicTacTg.place[1]+"_|_"+TicTacTg.place[2]+"_|\n");
		System.out.println("\t2 |_"+TicTacTg.place[3]+"_|_"+TicTacTg.place[4]+"_|_"+TicTacTg.place[5]+"_|\n");
		System.out.println("\t3 |_"+TicTacTg.place[6]+"_|_"+TicTacTg.place[7]+"_|_"+TicTacTg.place[8]+"_|");
		System.out.println("\t  '-----------'");

		////////////////////////////////////////////////////////////////////
		// Check Line Status ( How many lines are empty )
		checkLines();
		
	}
	
	public static void setup() {
		
		// Loop to reset the game board
		for ( int i = 0 ; i < 9 ; i++ ) {
			
			TicTacTg.place[i] = '_';
			
		}
		
		// Print the game board to the console
		drawBoard();
		
		while ( (TicTacTg.team != 'X') && (TicTacTg.team != 'O') ) {
			
			System.out.println("\n\nSelect Your Team! Enter 'X' or 'O' below...");
			
			System.out.print("Enter your selection: ");
			Scanner input = new Scanner(System.in);
			TicTacTg.usrStr = input.next();
			
			if (TicTacTg.usrStr.toUpperCase().equals("X")) {
				
				TicTacTg.team = 'X';
				TicTacTg.opp = 'O';
				
			} else if (TicTacTg.usrStr.toUpperCase().equals("O")) {
				
				TicTacTg.team = 'O';
				TicTacTg.opp = 'X';
				
			} else {
				
				System.out.println("You entered: " + usrStr);
				System.out.println("This is not a valid option.");
				System.out.println("Please enter either an X or an O to continue.");
				
			}
			
		}
		
		System.out.println("\nYou are team " + TicTacTg.team + "!");
		
		// Run the game method
		game();
		
	}
	
	public static void game() {
		
		// Local variable to run loop
		boolean loop = true;
		
		System.out.println("IT'S YOUR TURN!");
		
		drawBoard();
		
		do {
			
			System.out.println("\n\nChoose a column and row to place an " + TicTacTg.team + ". (EXAMPLE: A1)\n");
			
			System.out.print("Enter your selction: ");
			Scanner input = new Scanner(System.in);
			TicTacTg.usrStr = input.next().toUpperCase();
			
			switch (TicTacTg.usrStr)
			{
				case "A1" : if (TicTacTg.place[0]=='_') {
					
					TicTacTg.place[0] = TicTacTg.team;
					System.out.println("\nYou place an " + TicTacTg.team + " in A1");
					oppMove();
					loop = false;
					
				} else if (TicTacTg.place[0]==TicTacTg.team) {
					
					System.out.println("\nThere is an " + TicTacTg.team + " there already!");
					
				} else if (TicTacTg.place[0]==TicTacTg.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "B1" : if (TicTacTg.place[1]=='_') {
					
					TicTacTg.place[1] = TicTacTg.team;
					System.out.println("\nYou place an " + TicTacTg.team + " in B1");
					oppMove();
					loop = false;
					
				} else if (TicTacTg.place[1]==TicTacTg.team) {
					
					System.out.println("\nThere is an " + TicTacTg.team + " there already!");
					
				} else if (TicTacTg.place[1]==TicTacTg.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "C1" : if (TicTacTg.place[2]=='_') {
					
					TicTacTg.place[2] = TicTacTg.team;
					System.out.println("\nYou place an " + TicTacTg.team + " in C1");
					oppMove();
					loop = false;
					
				} else if (TicTacTg.place[2]==TicTacTg.team) {
					
					System.out.println("\nThere is an " + TicTacTg.team + " there already!");
					
				} else if (TicTacTg.place[2]==TicTacTg.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "A2" : if (TicTacTg.place[3]=='_') {
					
					TicTacTg.place[3] = TicTacTg.team;
					System.out.println("\nYou place an " + TicTacTg.team + " in A2");
					oppMove();
					loop = false;
					
				} else if (TicTacTg.place[3]==TicTacTg.team) {
					
					System.out.println("\nThere is an " + TicTacTg.team + " there already!");
				} else if (TicTacTg.place[3]==TicTacTg.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "B2" : if (TicTacTg.place[4]=='_') {
					
					TicTacTg.place[4] = TicTacTg.team;
					System.out.println("\nYou place an " + TicTacTg.team + " in B2");
					oppMove();
					loop = false;
					
				} else if (TicTacTg.place[4]==TicTacTg.team) {
					
					System.out.println("\nThere is an " + TicTacTg.team + " there already!");
					
				} else if (TicTacTg.place[4]==TicTacTg.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "C2" : if (TicTacTg.place[5]=='_') {
					
					TicTacTg.place[5] = TicTacTg.team;
					System.out.println("\nYou place an " + TicTacTg.team + " in C2");
					oppMove();
					loop = false;
					
				} else if (TicTacTg.place[5]==TicTacTg.team) {
					
					System.out.println("\nThere is an " + TicTacTg.team + " there already!");
					
				} else if (TicTacTg.place[5]==TicTacTg.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "A3" : if (TicTacTg.place[6]=='_') {
					
					TicTacTg.place[6] = TicTacTg.team;
					System.out.println("\nYou place an " + TicTacTg.team + " in A3");
					oppMove();
					loop = false;
					
				} else if (TicTacTg.place[6]==TicTacTg.team) {
					
					System.out.println("\nThere is an " + TicTacTg.team + " there already!");
					
				} else if (TicTacTg.place[6]==TicTacTg.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "B3" : if (TicTacTg.place[7]=='_') {
					
					TicTacTg.place[7] = TicTacTg.team;
					System.out.println("\nYou place an " + TicTacTg.team + " in B3");
					oppMove();
					loop = false;
					
				} else if (TicTacTg.place[7]==TicTacTg.team) {
					
					System.out.println("\nThere is an " + TicTacTg.team + " there already!");
					
				} else if (TicTacTg.place[7]==TicTacTg.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "C3" : if (TicTacTg.place[8]=='_') {
					
					TicTacTg.place[8] = TicTacTg.team;
					System.out.println("\nYou place an " + TicTacTg.team + " in C3");
					oppMove();
					loop = false;
					
				} else if (TicTacTg.place[8]==TicTacTg.team) {
					
					System.out.println("\nThere is an " + TicTacTg.team + " there already!");
					
				} else if (TicTacTg.place[8]==TicTacTg.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
			}
			
		} while (loop);
		
		checkWin();
		
	}
	

	public static void checkLines() {

		String p0=String.valueOf(TicTacTg.place[0]);
		String p1=String.valueOf(TicTacTg.place[1]);
		String p2=String.valueOf(TicTacTg.place[2]);
		String p3=String.valueOf(TicTacTg.place[3]);
		String p4=String.valueOf(TicTacTg.place[4]);
		String p5=String.valueOf(TicTacTg.place[5]);
		String p6=String.valueOf(TicTacTg.place[6]);
		String p7=String.valueOf(TicTacTg.place[7]);
		String p8=String.valueOf(TicTacTg.place[8]);

		String case1_012 = p0+p1+p2;
		String case2_345 = p3+p4+p5;
		String case3_678 = p6+p7+p8;
		String case4_036 = p0+p3+p6;
		String case5_147 = p1+p4+p7;
		String case6_258 = p2+p5+p8;
		String case7_048 = p0+p4+p8;
		String case8_246 = p2+p4+p6;

		System.out.println("case1_012 : "+case1_012);
		System.out.println("case2_453 : "+case2_345);
		System.out.println("case3_678 : "+case3_678);
		System.out.println("case4_036 : "+case4_036);
		System.out.println("case5_147 : "+case5_147);
		System.out.println("case6_258 : "+case6_258);
		System.out.println("case7_048 : "+case7_048);
		System.out.println("case8_246 : "+case8_246);
		
		int line1_count = case1_012.length() - case1_012.replaceAll("_","").length();
		int line2_count = case2_345.length() - case2_345.replaceAll("_","").length();
		int line3_count = case3_678.length() - case3_678.replaceAll("_","").length();

		System.out.println("line1_count / line2_count / line3_count : "+ line1_count + " / " + line2_count + " / " + line3_count);

	}		

	public static void oppMove() {

		String p0=String.valueOf(TicTacTg.place[0]);
		String p1=String.valueOf(TicTacTg.place[1]);
		String p2=String.valueOf(TicTacTg.place[2]);
		String p3=String.valueOf(TicTacTg.place[3]);
		String p4=String.valueOf(TicTacTg.place[4]);
		String p5=String.valueOf(TicTacTg.place[5]);
		String p6=String.valueOf(TicTacTg.place[6]);
		String p7=String.valueOf(TicTacTg.place[7]);
		String p8=String.valueOf(TicTacTg.place[8]);

		String case1_012 = p0+p1+p2;
		String case2_345 = p3+p4+p5;
		String case3_678 = p6+p7+p8;
		String case4_036 = p0+p3+p6;
		String case5_147 = p1+p4+p7;
		String case6_258 = p2+p5+p8;
		String case7_048 = p0+p4+p8;
		String case8_246 = p2+p4+p6;
		
		int line1_count = case1_012.length() - case1_012.replaceAll("_","").length();
		int line2_count = case2_345.length() - case2_345.replaceAll("_","").length();
		int line3_count = case3_678.length() - case3_678.replaceAll("_","").length();
		int line4_count = case4_036.length() - case4_036.replaceAll("_","").length();
		int line5_count = case5_147.length() - case5_147.replaceAll("_","").length();
		int line6_count = case6_258.length() - case6_258.replaceAll("_","").length();
		int line7_count = case7_048.length() - case7_048.replaceAll("_","").length();
		int line8_count = case8_246.length() - case8_246.replaceAll("_","").length();

		int line1_X_count = case1_012.length() - case1_012.replaceAll("X","").length();
		int line2_X_count = case2_345.length() - case2_345.replaceAll("X","").length();
		int line3_X_count = case3_678.length() - case3_678.replaceAll("X","").length();
		int line4_X_count = case4_036.length() - case4_036.replaceAll("X","").length();
		int line5_X_count = case5_147.length() - case5_147.replaceAll("X","").length();
		int line6_X_count = case6_258.length() - case6_258.replaceAll("X","").length();
		int line7_X_count = case7_048.length() - case7_048.replaceAll("X","").length();
		int line8_X_count = case8_246.length() - case8_246.replaceAll("X","").length();

		int line1_O_count = case1_012.length() - case1_012.replaceAll("O","").length();
		int line2_O_count = case2_345.length() - case2_345.replaceAll("O","").length();
		int line3_O_count = case3_678.length() - case3_678.replaceAll("O","").length();
		int line4_O_count = case4_036.length() - case4_036.replaceAll("O","").length();
		int line5_O_count = case5_147.length() - case5_147.replaceAll("O","").length();
		int line6_O_count = case6_258.length() - case6_258.replaceAll("O","").length();
		int line7_O_count = case7_048.length() - case7_048.replaceAll("O","").length();
		int line8_O_count = case8_246.length() - case8_246.replaceAll("O","").length();

		while (true) // while aaa
		{

			// 한 곳이라도 채워지지 않은 곳이 있다면
			if ( (line1_count > 0) || ( line2_count > 0 ) || ( line3_count > 0 ) )  // if bbb
			{
				System.out.println("TicTacTg.team == 'X'");
				// TicTacTg.team == 'X'
				if ( TicTacTg.team == 'X' ) // if ccc
				{
							
					if ( (line1_O_count > 1 ) || (line2_O_count > 1 )  || (line3_O_count > 1 ) || (line4_O_count > 1 ) || (line5_O_count > 1 ) || (line6_O_count > 1 ) || (line7_O_count > 1 ) || (line8_O_count > 1 )) // ddd
					{
						System.out.println("[ Warning ] You have one left to lose.");

						if ( (line1_O_count > 1 ) ) // line1_O_count
						{
							if (case1_012 == "_XX")
							{
								TicTacTg.place[0] = TicTacTg.opp;
								break;
							}
							if (case1_012 == "X_X")
							{
								TicTacTg.place[1] = TicTacTg.opp;
								break;
							}
							if (case1_012 == "XX_")
							{
								TicTacTg.place[2] = TicTacTg.opp;
								break;	
							}
						} // if line1_O_count
						
						if ( (line2_O_count > 1 ) ) // line2_O_count
						{
							if (case2_345 == "_XX")
							{
								TicTacTg.place[3] = TicTacTg.opp;
								break;
							}
							if (case2_345 == "X_X")
							{
								TicTacTg.place[4] = TicTacTg.opp;
								break;
							}
							if (case2_345 == "XX_")
							{
								TicTacTg.place[5] = TicTacTg.opp;
								break;	
							}
						} // else if line2_O_count

						if ( (line3_O_count > 1 ) ) // line3_O_count
						{
							if (case3_678 == "_XX")
							{
								TicTacTg.place[6] = TicTacTg.opp;
								break;
							}
							if (case3_678 == "X_X")
							{
								TicTacTg.place[7] = TicTacTg.opp;
								break;
							}
							if (case3_678 == "XX_")
							{
								TicTacTg.place[8] = TicTacTg.opp;
								break;	
							}
						} // else if line4_O_count

						if ( (line4_O_count > 1 ) ) // line4_O_count
						{
							if (case4_036 == "_XX")
							{
								TicTacTg.place[0] = TicTacTg.opp;
								break;
							}
							if (case4_036 == "X_X")
							{
								TicTacTg.place[3] = TicTacTg.opp;
								break;
							}
							if (case4_036 == "XX_")
							{
								TicTacTg.place[6] = TicTacTg.opp;
								break;	
							}

						} // else if line5_O_count

						if ( (line5_O_count > 1 ) ) // line5_O_count
						{
							if (case5_147 == "_XX")
							{
								TicTacTg.place[1] = TicTacTg.opp;
								break;
							}
							if (case5_147 == "X_X")
							{
								TicTacTg.place[4] = TicTacTg.opp;
								break;
							}
							if (case5_147 == "XX_")
							{
								TicTacTg.place[7] = TicTacTg.opp;
								break;	
							}
						} // else if line5_O_count

						if ( (line6_O_count > 1 ) ) // line6_O_count
						{
							if (case6_258 == "_XX")
							{
								TicTacTg.place[2] = TicTacTg.opp;
								break;
							}
							if (case6_258 == "X_X")
							{
								TicTacTg.place[5] = TicTacTg.opp;
								break;
							}
							if (case6_258 == "XX_")
							{
								TicTacTg.place[8] = TicTacTg.opp;
								break;	
							}
						} // else if line6_O_count


						if ( (line7_O_count > 1 ) ) // line7_O_count
						{
							if (case7_048 == "_XX")
							{
								TicTacTg.place[0] = TicTacTg.opp;
								break;
							}
							if (case7_048 == "X_X")
							{
								TicTacTg.place[4] = TicTacTg.opp;
								break;
							}
							if (case7_048 == "XX_")
							{
								TicTacTg.place[8] = TicTacTg.opp;
								break;	
							}
						} // else if line7_O_count

						if ( (line8_O_count > 1 ) ) // line8_O_count
						{
							if (case8_246 == "_XX")
							{
								TicTacTg.place[2] = TicTacTg.opp;
								break;
							}
							if (case8_246 == "X_X")
							{
								TicTacTg.place[4] = TicTacTg.opp;
								break;
							}
							if (case8_246 == "XX_")
							{
								TicTacTg.place[6] = TicTacTg.opp;
								break;	
							}

						} // else - if eee

					} // if ddd
					else // else fff
					{
						float rn = (float) Math.random();
						// System.out.println("(float) Math.random() :" + rn);
						float m = rn * 8;
						// System.out.println("m = rn * 8 :" + m);
						int x = Math.round(m);
						// System.out.println("Math.round(m) :" + x);
							
						if (TicTacTg.place[x]=='_') // if ggg 
						{	
							System.out.println(">>> Random input <<<");
							TicTacTg.place[x] = TicTacTg.opp;
							break;
						} // if ggg
					} // else fff
				} // if ccc 
				// TicTacTg.team == 'O'
				else
				{
					System.out.println("TicTacTg.team == 'O'");
				}
			} // if bbb
			else 
			{ 
				checkWin(); break; 
			} // else - if bbb
		}  // while aaa

	}

	public static void checkWin() {
		
		// See if X has won the game
		
		if ( (TicTacTg.place[0]=='X') && (TicTacTg.place[1]=='X') && (TicTacTg.place[2]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTg.place[3]=='X') && (TicTacTg.place[4]=='X') && (TicTacTg.place[5]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTg.place[6]=='X') && (TicTacTg.place[7]=='X') && (TicTacTg.place[8]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTg.place[0]=='X') && (TicTacTg.place[3]=='X') && (TicTacTg.place[6]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTg.place[1]=='X') && (TicTacTg.place[4]=='X') && (TicTacTg.place[7]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTg.place[2]=='X') && (TicTacTg.place[5]=='X') && (TicTacTg.place[8]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTg.place[0]=='X') && (TicTacTg.place[4]=='X') && (TicTacTg.place[8]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTg.place[6]=='X') && (TicTacTg.place[4]=='X') && (TicTacTg.place[2]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
		}
		
		// Now, see if O has won!
		
		if ( (TicTacTg.place[0]=='O') && (TicTacTg.place[1]=='O') && (TicTacTg.place[2]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTg.place[3]=='O') && (TicTacTg.place[4]=='O') && (TicTacTg.place[5]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTg.place[6]=='O') && (TicTacTg.place[7]=='O') && (TicTacTg.place[8]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTg.place[0]=='O') && (TicTacTg.place[3]=='O') && (TicTacTg.place[6]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTg.place[1]=='O') && (TicTacTg.place[4]=='O') && (TicTacTg.place[7]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTg.place[2]=='O') && (TicTacTg.place[5]=='O') && (TicTacTg.place[8]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTg.place[0]=='O') && (TicTacTg.place[4]=='O') && (TicTacTg.place[8]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTg.place[6]=='O') && (TicTacTg.place[4]=='O') && (TicTacTg.place[2]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
		
		// Check for a tie!
		
		} else if ( (TicTacTg.place[0]!='_') && (TicTacTg.place[1]!='_') && (TicTacTg.place[2]!='_') && (TicTacTg.place[3]!='_') && (TicTacTg.place[4]!='_') && (TicTacTg.place[5]!='_') && (TicTacTg.place[6]!='_') && (TicTacTg.place[7]!='_') && (TicTacTg.place[8]!='_') ) {
			
			System.out.println("\n\n\n\tTIE GAME!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
		
		// If no one has won and no tie, keep playing!!
		
		} else { game(); }
		
	}
	
	public static void playAgain() {
		
			System.out.print("\n\nPlay again? [y/n]: ");
			Scanner input = new Scanner(System.in);
			TicTacTg.usrStr = input.next().toLowerCase();
			
			if (usrStr.equals("y")) {
				
				TicTacTg.team = '_';
				TicTacTg.opp = '_';
				setup();
				
			} else {
				
				System.exit(0);
				
			}
		
	}
	
}