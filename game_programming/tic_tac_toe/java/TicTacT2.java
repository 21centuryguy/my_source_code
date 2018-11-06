import java.util.Scanner;

class TicTacT2 {
	
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
		System.out.println("\t1 |_"+TicTacT2.place[0]+"_|_"+TicTacT2.place[1]+"_|_"+TicTacT2.place[2]+"_|\n");
		System.out.println("\t2 |_"+TicTacT2.place[3]+"_|_"+TicTacT2.place[4]+"_|_"+TicTacT2.place[5]+"_|\n");
		System.out.println("\t3 |_"+TicTacT2.place[6]+"_|_"+TicTacT2.place[7]+"_|_"+TicTacT2.place[8]+"_|");
		System.out.println("\t  '-----------'");
		
	}
	
	public static void setup() {
		
		// Loop to reset the game board
		for ( int i = 0 ; i < 9 ; i++ ) {
			
			TicTacT2.place[i] = '_';
			
		}
		
		// Print the game board to the console
		drawBoard();
		
		while ( (TicTacT2.team != 'X') && (TicTacT2.team != 'O') ) {
			
			System.out.println("\n\nSelect Your Team! Enter 'X' or 'O' below...");
			
			System.out.print("Enter your selection: ");
			Scanner input = new Scanner(System.in);
			TicTacT2.usrStr = input.next();
			
			if (TicTacT2.usrStr.toUpperCase().equals("X")) {
				
				TicTacT2.team = 'X';
				TicTacT2.opp = 'O';
				
			} else if (TicTacT2.usrStr.toUpperCase().equals("O")) {
				
				TicTacT2.team = 'O';
				TicTacT2.opp = 'X';
				
			} else {
				
				System.out.println("You entered: " + usrStr);
				System.out.println("This is not a valid option.");
				System.out.println("Please enter either an X or an O to continue.");
				
			}
			
		}
		
		System.out.println("\nYou are team " + TicTacT2.team + "!");
		
		// Run the game method
		game();
		
	}
	
	public static void game() {
		
		// Local variable to run loop
		boolean loop = true;
		
		System.out.println("IT'S YOUR TURN!");
		
		drawBoard();
		
		do {
			
			System.out.println("\n\nChoose a column and row to place an " + TicTacT2.team + ". (EXAMPLE: A1)\n");
			
			System.out.print("Enter your selction: ");
			Scanner input = new Scanner(System.in);
			TicTacT2.usrStr = input.next().toUpperCase();
			
			switch (TicTacT2.usrStr)
			{
				case "A1" : if (TicTacT2.place[0]=='_') {
					
					TicTacT2.place[0] = TicTacT2.team;
					System.out.println("\nYou place an " + TicTacT2.team + " in A1");
					oppMove();
					loop = false;
					
				} else if (TicTacT2.place[0]==TicTacT2.team) {
					
					System.out.println("\nThere is an " + TicTacT2.team + " there already!");
					
				} else if (TicTacT2.place[0]==TicTacT2.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "B1" : if (TicTacT2.place[1]=='_') {
					
					TicTacT2.place[1] = TicTacT2.team;
					System.out.println("\nYou place an " + TicTacT2.team + " in B1");
					oppMove();
					loop = false;
					
				} else if (TicTacT2.place[1]==TicTacT2.team) {
					
					System.out.println("\nThere is an " + TicTacT2.team + " there already!");
					
				} else if (TicTacT2.place[1]==TicTacT2.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "C1" : if (TicTacT2.place[2]=='_') {
					
					TicTacT2.place[2] = TicTacT2.team;
					System.out.println("\nYou place an " + TicTacT2.team + " in C1");
					oppMove();
					loop = false;
					
				} else if (TicTacT2.place[2]==TicTacT2.team) {
					
					System.out.println("\nThere is an " + TicTacT2.team + " there already!");
					
				} else if (TicTacT2.place[2]==TicTacT2.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "A2" : if (TicTacT2.place[3]=='_') {
					
					TicTacT2.place[3] = TicTacT2.team;
					System.out.println("\nYou place an " + TicTacT2.team + " in A2");
					oppMove();
					loop = false;
					
				} else if (TicTacT2.place[3]==TicTacT2.team) {
					
					System.out.println("\nThere is an " + TicTacT2.team + " there already!");
				} else if (TicTacT2.place[3]==TicTacT2.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "B2" : if (TicTacT2.place[4]=='_') {
					
					TicTacT2.place[4] = TicTacT2.team;
					System.out.println("\nYou place an " + TicTacT2.team + " in B2");
					oppMove();
					loop = false;
					
				} else if (TicTacT2.place[4]==TicTacT2.team) {
					
					System.out.println("\nThere is an " + TicTacT2.team + " there already!");
					
				} else if (TicTacT2.place[4]==TicTacT2.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "C2" : if (TicTacT2.place[5]=='_') {
					
					TicTacT2.place[5] = TicTacT2.team;
					System.out.println("\nYou place an " + TicTacT2.team + " in C2");
					oppMove();
					loop = false;
					
				} else if (TicTacT2.place[5]==TicTacT2.team) {
					
					System.out.println("\nThere is an " + TicTacT2.team + " there already!");
					
				} else if (TicTacT2.place[5]==TicTacT2.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "A3" : if (TicTacT2.place[6]=='_') {
					
					TicTacT2.place[6] = TicTacT2.team;
					System.out.println("\nYou place an " + TicTacT2.team + " in A3");
					oppMove();
					loop = false;
					
				} else if (TicTacT2.place[6]==TicTacT2.team) {
					
					System.out.println("\nThere is an " + TicTacT2.team + " there already!");
					
				} else if (TicTacT2.place[6]==TicTacT2.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "B3" : if (TicTacT2.place[7]=='_') {
					
					TicTacT2.place[7] = TicTacT2.team;
					System.out.println("\nYou place an " + TicTacT2.team + " in B3");
					oppMove();
					loop = false;
					
				} else if (TicTacT2.place[7]==TicTacT2.team) {
					
					System.out.println("\nThere is an " + TicTacT2.team + " there already!");
					
				} else if (TicTacT2.place[7]==TicTacT2.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "C3" : if (TicTacT2.place[8]=='_') {
					
					TicTacT2.place[8] = TicTacT2.team;
					System.out.println("\nYou place an " + TicTacT2.team + " in C3");
					oppMove();
					loop = false;
					
				} else if (TicTacT2.place[8]==TicTacT2.team) {
					
					System.out.println("\nThere is an " + TicTacT2.team + " there already!");
					
				} else if (TicTacT2.place[8]==TicTacT2.opp) {
					
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
				System.out.println(TicTacT2.place[0]);
				System.out.println(TicTacT2.place[1]);
				System.out.println(TicTacT2.place[2]);
				System.out.println(TicTacT2.place[3]);
				System.out.println(TicTacT2.place[4]);
				System.out.println(TicTacT2.place[5]);
				System.out.println(TicTacT2.place[6]);
				System.out.println(TicTacT2.place[7]);
				System.out.println(TicTacT2.place[8]);

			} else { checkWin(); break; } // public static void oppMove/if[1]

		} // line 266 while close 
	
	} // public static void oppMove()


////////////////////////////////////////////////////////////////////////////////////////////////////////////*/

	public static void oppMove() {
		
		while (true) {
			
			if ( (TicTacT2.place[0]=='_') || (TicTacT2.place[1]=='_') || (TicTacT2.place[2]=='_') || (TicTacT2.place[3]=='_') || (TicTacT2.place[4]=='_') || (TicTacT2.place[5]=='_') || (TicTacT2.place[6]=='_') || (TicTacT2.place[7]=='_') || (TicTacT2.place[8]=='_') ) {
				
				/* 
				012
				345
				678

				036
				147
				258
				048
				246
				*/


				String p0=String.valueOf(TicTacT2.place[0]);
				String p1=String.valueOf(TicTacT2.place[1]);
				String p2=String.valueOf(TicTacT2.place[2]);
				String p3=String.valueOf(TicTacT2.place[3]);
				String p4=String.valueOf(TicTacT2.place[4]);
				String p5=String.valueOf(TicTacT2.place[5]);
				String p6=String.valueOf(TicTacT2.place[6]);
				String p7=String.valueOf(TicTacT2.place[7]);
				String p8=String.valueOf(TicTacT2.place[8]);

				String case1_012 = p0+p1+p2;
				String case1_345 = p3+p4+p5;
				String case1_678 = p6+p7+p8;
				String case1_036 = p0+p3+p6;
				String case1_147 = p1+p4+p7;
				String case1_258 = p2+p5+p8;
				String case1_048 = p0+p4+p8;
				String case1_246 = p2+p4+p6;

				System.out.println("case1_012 : "+case1_012);
				System.out.println("case2_453 : "+case1_345);
				System.out.println("case3_678 : "+case1_678);
				System.out.println("case4_036 : "+case1_036);
				System.out.println("case5_147 : "+case1_147);
				System.out.println("case6_258 : "+case1_258);
				System.out.println("case7_048 : "+case1_048);
				System.out.println("case8_246 : "+case1_246);

				/*System.out.println(p0+p1+p2);
				System.out.println(p3+p4+p5);
				System.out.println(p6+p7+p8);
				System.out.println(p0+p3+p6);
				System.out.println(p1+p4+p7);
				System.out.println(p2+p5+p8);
				System.out.println(p0+p4+p8);
				System.out.println(p2+p4+p6);*/


				/*System.out.println("012 : "+p0+p1+p2);
				System.out.println("345 : "+p3+p4+p5);
				System.out.println("678 : "+p6+p7+p8);
				System.out.println("036 : "+p0+p3+p6);
				System.out.println("147 : "+p1+p4+p7);
				System.out.println("258 : "+p2+p5+p8);
				System.out.println("048 : "+p0+p4+p8);
				System.out.println("246 : "+p2+p4+p6);*/



				float rn = (float) Math.random();
				// System.out.println("(float) Math.random() :" + rn);
				float m = rn * 8;
				// System.out.println("m = rn * 8 :" + m);
				int x = Math.round(m);
				// System.out.println("Math.round(m) :" + x);

				
				if (TicTacT2.place[x]=='_') {
					
					TicTacT2.place[x] = TicTacT2.opp;
					break;
					
				}
				
			} else { checkWin(); break; }
				
			}
			
		}

	////////////////////////////////////////////////////////////////////////////////////////////////////////////

	public static void checkWin() {
		
		// See if X has won the game
		
		if ( (TicTacT2.place[0]=='X') && (TicTacT2.place[1]=='X') && (TicTacT2.place[2]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT2.place[3]=='X') && (TicTacT2.place[4]=='X') && (TicTacT2.place[5]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT2.place[6]=='X') && (TicTacT2.place[7]=='X') && (TicTacT2.place[8]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT2.place[0]=='X') && (TicTacT2.place[3]=='X') && (TicTacT2.place[6]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT2.place[1]=='X') && (TicTacT2.place[4]=='X') && (TicTacT2.place[7]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT2.place[2]=='X') && (TicTacT2.place[5]=='X') && (TicTacT2.place[8]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT2.place[0]=='X') && (TicTacT2.place[4]=='X') && (TicTacT2.place[8]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT2.place[6]=='X') && (TicTacT2.place[4]=='X') && (TicTacT2.place[2]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
		}
		
		// Now, see if O has won!
		
		if ( (TicTacT2.place[0]=='O') && (TicTacT2.place[1]=='O') && (TicTacT2.place[2]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT2.place[3]=='O') && (TicTacT2.place[4]=='O') && (TicTacT2.place[5]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT2.place[6]=='O') && (TicTacT2.place[7]=='O') && (TicTacT2.place[8]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT2.place[0]=='O') && (TicTacT2.place[3]=='O') && (TicTacT2.place[6]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT2.place[1]=='O') && (TicTacT2.place[4]=='O') && (TicTacT2.place[7]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT2.place[2]=='O') && (TicTacT2.place[5]=='O') && (TicTacT2.place[8]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT2.place[0]=='O') && (TicTacT2.place[4]=='O') && (TicTacT2.place[8]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT2.place[6]=='O') && (TicTacT2.place[4]=='O') && (TicTacT2.place[2]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
		
		// Check for a tie!
		
		} else if ( (TicTacT2.place[0]!='_') && (TicTacT2.place[1]!='_') && (TicTacT2.place[2]!='_') && (TicTacT2.place[3]!='_') && (TicTacT2.place[4]!='_') && (TicTacT2.place[5]!='_') && (TicTacT2.place[6]!='_') && (TicTacT2.place[7]!='_') && (TicTacT2.place[8]!='_') ) {
			
			System.out.println("\n\n\n\tTIE GAME!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
		
		// If no one has won and no tie, keep playing!!
		
		} else { game(); }
		
	}
	
	public static void playAgain() {
		
			System.out.print("\n\nPlay again? [y/n]: ");
			Scanner input = new Scanner(System.in);
			TicTacT2.usrStr = input.next().toLowerCase();
			
			if (usrStr.equals("y")) {
				
				TicTacT2.team = '_';
				TicTacT2.opp = '_';
				setup();
				
			} else {
				
				System.exit(0);
				
			}
		
	}
	
}