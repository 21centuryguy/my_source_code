import java.util.Scanner;

class TicTacTd {
	
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
		System.out.println("\t1 |_"+TicTacTd.place[0]+"_|_"+TicTacTd.place[1]+"_|_"+TicTacTd.place[2]+"_|\n");
		System.out.println("\t2 |_"+TicTacTd.place[3]+"_|_"+TicTacTd.place[4]+"_|_"+TicTacTd.place[5]+"_|\n");
		System.out.println("\t3 |_"+TicTacTd.place[6]+"_|_"+TicTacTd.place[7]+"_|_"+TicTacTd.place[8]+"_|");
		System.out.println("\t  '-----------'");

		String p0=String.valueOf(TicTacTd.place[0]);
		String p1=String.valueOf(TicTacTd.place[1]);
		String p2=String.valueOf(TicTacTd.place[2]);
		String p3=String.valueOf(TicTacTd.place[3]);
		String p4=String.valueOf(TicTacTd.place[4]);
		String p5=String.valueOf(TicTacTd.place[5]);
		String p6=String.valueOf(TicTacTd.place[6]);
		String p7=String.valueOf(TicTacTd.place[7]);
		String p8=String.valueOf(TicTacTd.place[8]);

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
	
	public static void setup() {
		
		// Loop to reset the game board
		for ( int i = 0 ; i < 9 ; i++ ) {
			
			TicTacTd.place[i] = '_';
			
		}
		
		// Print the game board to the console
		drawBoard();
		
		while ( (TicTacTd.team != 'X') && (TicTacTd.team != 'O') ) {
			
			System.out.println("\n\nSelect Your Team! Enter 'X' or 'O' below...");
			
			System.out.print("Enter your selection: ");
			Scanner input = new Scanner(System.in);
			TicTacTd.usrStr = input.next();
			
			if (TicTacTd.usrStr.toUpperCase().equals("X")) {
				
				TicTacTd.team = 'X';
				TicTacTd.opp = 'O';
				
			} else if (TicTacTd.usrStr.toUpperCase().equals("O")) {
				
				TicTacTd.team = 'O';
				TicTacTd.opp = 'X';
				
			} else {
				
				System.out.println("You entered: " + usrStr);
				System.out.println("This is not a valid option.");
				System.out.println("Please enter either an X or an O to continue.");
				
			}
			
		}
		
		System.out.println("\nYou are team " + TicTacTd.team + "!");
		
		// Run the game method
		game();
		
	}
	
	public static void game() {
		
		// Local variable to run loop
		boolean loop = true;
		
		System.out.println("IT'S YOUR TURN!");
		
		drawBoard();
		
		do {
			
			System.out.println("\n\nChoose a column and row to place an " + TicTacTd.team + ". (EXAMPLE: A1)\n");
			
			System.out.print("Enter your selction: ");
			Scanner input = new Scanner(System.in);
			TicTacTd.usrStr = input.next().toUpperCase();
			
			switch (TicTacTd.usrStr)
			{
				case "A1" : if (TicTacTd.place[0]=='_') {
					
					TicTacTd.place[0] = TicTacTd.team;
					System.out.println("\nYou place an " + TicTacTd.team + " in A1");
					oppMove();
					loop = false;
					
				} else if (TicTacTd.place[0]==TicTacTd.team) {
					
					System.out.println("\nThere is an " + TicTacTd.team + " there already!");
					
				} else if (TicTacTd.place[0]==TicTacTd.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "B1" : if (TicTacTd.place[1]=='_') {
					
					TicTacTd.place[1] = TicTacTd.team;
					System.out.println("\nYou place an " + TicTacTd.team + " in B1");
					oppMove();
					loop = false;
					
				} else if (TicTacTd.place[1]==TicTacTd.team) {
					
					System.out.println("\nThere is an " + TicTacTd.team + " there already!");
					
				} else if (TicTacTd.place[1]==TicTacTd.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "C1" : if (TicTacTd.place[2]=='_') {
					
					TicTacTd.place[2] = TicTacTd.team;
					System.out.println("\nYou place an " + TicTacTd.team + " in C1");
					oppMove();
					loop = false;
					
				} else if (TicTacTd.place[2]==TicTacTd.team) {
					
					System.out.println("\nThere is an " + TicTacTd.team + " there already!");
					
				} else if (TicTacTd.place[2]==TicTacTd.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "A2" : if (TicTacTd.place[3]=='_') {
					
					TicTacTd.place[3] = TicTacTd.team;
					System.out.println("\nYou place an " + TicTacTd.team + " in A2");
					oppMove();
					loop = false;
					
				} else if (TicTacTd.place[3]==TicTacTd.team) {
					
					System.out.println("\nThere is an " + TicTacTd.team + " there already!");
				} else if (TicTacTd.place[3]==TicTacTd.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "B2" : if (TicTacTd.place[4]=='_') {
					
					TicTacTd.place[4] = TicTacTd.team;
					System.out.println("\nYou place an " + TicTacTd.team + " in B2");
					oppMove();
					loop = false;
					
				} else if (TicTacTd.place[4]==TicTacTd.team) {
					
					System.out.println("\nThere is an " + TicTacTd.team + " there already!");
					
				} else if (TicTacTd.place[4]==TicTacTd.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "C2" : if (TicTacTd.place[5]=='_') {
					
					TicTacTd.place[5] = TicTacTd.team;
					System.out.println("\nYou place an " + TicTacTd.team + " in C2");
					oppMove();
					loop = false;
					
				} else if (TicTacTd.place[5]==TicTacTd.team) {
					
					System.out.println("\nThere is an " + TicTacTd.team + " there already!");
					
				} else if (TicTacTd.place[5]==TicTacTd.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "A3" : if (TicTacTd.place[6]=='_') {
					
					TicTacTd.place[6] = TicTacTd.team;
					System.out.println("\nYou place an " + TicTacTd.team + " in A3");
					oppMove();
					loop = false;
					
				} else if (TicTacTd.place[6]==TicTacTd.team) {
					
					System.out.println("\nThere is an " + TicTacTd.team + " there already!");
					
				} else if (TicTacTd.place[6]==TicTacTd.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "B3" : if (TicTacTd.place[7]=='_') {
					
					TicTacTd.place[7] = TicTacTd.team;
					System.out.println("\nYou place an " + TicTacTd.team + " in B3");
					oppMove();
					loop = false;
					
				} else if (TicTacTd.place[7]==TicTacTd.team) {
					
					System.out.println("\nThere is an " + TicTacTd.team + " there already!");
					
				} else if (TicTacTd.place[7]==TicTacTd.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "C3" : if (TicTacTd.place[8]=='_') {
					
					TicTacTd.place[8] = TicTacTd.team;
					System.out.println("\nYou place an " + TicTacTd.team + " in C3");
					oppMove();
					loop = false;
					
				} else if (TicTacTd.place[8]==TicTacTd.team) {
					
					System.out.println("\nThere is an " + TicTacTd.team + " there already!");
					
				} else if (TicTacTd.place[8]==TicTacTd.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
			}
			
		} while (loop);
		
		checkWin();
		
	}
	
	/*////////////////////////////////////////////////////////////////////////////////////////////////////////////

	public static void oppMove() {
		
		while (true) {
			if ( TicTacT.opp == 'O' ) {
				System.out.println(TicTacTd.place[0]);
				System.out.println(TicTacTd.place[1]);
				System.out.println(TicTacTd.place[2]);
				System.out.println(TicTacTd.place[3]);
				System.out.println(TicTacTd.place[4]);
				System.out.println(TicTacTd.place[5]);
				System.out.println(TicTacTd.place[6]);
				System.out.println(TicTacTd.place[7]);
				System.out.println(TicTacTd.place[8]);

			} else { checkWin(); break; } // public static void oppMove/if[1]

		} // line 266 while close 
	
	} // public static void oppMove()


////////////////////////////////////////////////////////////////////////////////////////////////////////////*/

	public static void oppMove() {

		String p0=String.valueOf(TicTacTd.place[0]);
		String p1=String.valueOf(TicTacTd.place[1]);
		String p2=String.valueOf(TicTacTd.place[2]);
		String p3=String.valueOf(TicTacTd.place[3]);
		String p4=String.valueOf(TicTacTd.place[4]);
		String p5=String.valueOf(TicTacTd.place[5]);
		String p6=String.valueOf(TicTacTd.place[6]);
		String p7=String.valueOf(TicTacTd.place[7]);
		String p8=String.valueOf(TicTacTd.place[8]);

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

		while (true) {
			
			if ( (line1_count > 0) || ( line2_count > 0 ) || ( line3_count > 0 ) ) {

				float rn = (float) Math.random();
				// System.out.println("(float) Math.random() :" + rn);
				float m = rn * 8;
				// System.out.println("m = rn * 8 :" + m);
				int x = Math.round(m);
				// System.out.println("Math.round(m) :" + x);

				
				if (TicTacTd.place[x]=='_') {
					
					TicTacTd.place[x] = TicTacTd.opp;
					break;
					
				}
				
			} else { checkWin(); break; }
				
			}
			
		}

	////////////////////////////////////////////////////////////////////////////////////////////////////////////

	public static void checkWin() {
		
		// See if X has won the game
		
		if ( (TicTacTd.place[0]=='X') && (TicTacTd.place[1]=='X') && (TicTacTd.place[2]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTd.place[3]=='X') && (TicTacTd.place[4]=='X') && (TicTacTd.place[5]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTd.place[6]=='X') && (TicTacTd.place[7]=='X') && (TicTacTd.place[8]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTd.place[0]=='X') && (TicTacTd.place[3]=='X') && (TicTacTd.place[6]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTd.place[1]=='X') && (TicTacTd.place[4]=='X') && (TicTacTd.place[7]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTd.place[2]=='X') && (TicTacTd.place[5]=='X') && (TicTacTd.place[8]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTd.place[0]=='X') && (TicTacTd.place[4]=='X') && (TicTacTd.place[8]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTd.place[6]=='X') && (TicTacTd.place[4]=='X') && (TicTacTd.place[2]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
		}
		
		// Now, see if O has won!
		
		if ( (TicTacTd.place[0]=='O') && (TicTacTd.place[1]=='O') && (TicTacTd.place[2]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTd.place[3]=='O') && (TicTacTd.place[4]=='O') && (TicTacTd.place[5]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTd.place[6]=='O') && (TicTacTd.place[7]=='O') && (TicTacTd.place[8]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTd.place[0]=='O') && (TicTacTd.place[3]=='O') && (TicTacTd.place[6]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTd.place[1]=='O') && (TicTacTd.place[4]=='O') && (TicTacTd.place[7]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTd.place[2]=='O') && (TicTacTd.place[5]=='O') && (TicTacTd.place[8]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTd.place[0]=='O') && (TicTacTd.place[4]=='O') && (TicTacTd.place[8]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTd.place[6]=='O') && (TicTacTd.place[4]=='O') && (TicTacTd.place[2]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
		
		// Check for a tie!
		
		} else if ( (TicTacTd.place[0]!='_') && (TicTacTd.place[1]!='_') && (TicTacTd.place[2]!='_') && (TicTacTd.place[3]!='_') && (TicTacTd.place[4]!='_') && (TicTacTd.place[5]!='_') && (TicTacTd.place[6]!='_') && (TicTacTd.place[7]!='_') && (TicTacTd.place[8]!='_') ) {
			
			System.out.println("\n\n\n\tTIE GAME!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
		
		// If no one has won and no tie, keep playing!!
		
		} else { game(); }
		
	}
	
	public static void playAgain() {
		
			System.out.print("\n\nPlay again? [y/n]: ");
			Scanner input = new Scanner(System.in);
			TicTacTd.usrStr = input.next().toLowerCase();
			
			if (usrStr.equals("y")) {
				
				TicTacTd.team = '_';
				TicTacTd.opp = '_';
				setup();
				
			} else {
				
				System.exit(0);
				
			}
		
	}
	
}