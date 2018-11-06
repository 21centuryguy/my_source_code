import java.util.Scanner;

class TicTacTe {
	
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
		System.out.println("\t1 |_"+TicTacTe.place[0]+"_|_"+TicTacTe.place[1]+"_|_"+TicTacTe.place[2]+"_|\n");
		System.out.println("\t2 |_"+TicTacTe.place[3]+"_|_"+TicTacTe.place[4]+"_|_"+TicTacTe.place[5]+"_|\n");
		System.out.println("\t3 |_"+TicTacTe.place[6]+"_|_"+TicTacTe.place[7]+"_|_"+TicTacTe.place[8]+"_|");
		System.out.println("\t  '-----------'");

		checkLines();
		
	}
	
	public static void setup() {
		
		// Loop to reset the game board
		for ( int i = 0 ; i < 9 ; i++ ) {
			
			TicTacTe.place[i] = '_';
			
		}
		
		// Print the game board to the console
		drawBoard();
		
		while ( (TicTacTe.team != 'X') && (TicTacTe.team != 'O') ) {
			
			System.out.println("\n\nSelect Your Team! Enter 'X' or 'O' below...");
			
			System.out.print("Enter your selection: ");
			Scanner input = new Scanner(System.in);
			TicTacTe.usrStr = input.next();
			
			if (TicTacTe.usrStr.toUpperCase().equals("X")) {
				
				TicTacTe.team = 'X';
				TicTacTe.opp = 'O';
				
			} else if (TicTacTe.usrStr.toUpperCase().equals("O")) {
				
				TicTacTe.team = 'O';
				TicTacTe.opp = 'X';
				
			} else {
				
				System.out.println("You entered: " + usrStr);
				System.out.println("This is not a valid option.");
				System.out.println("Please enter either an X or an O to continue.");
				
			}
			
		}
		
		System.out.println("\nYou are team " + TicTacTe.team + "!");
		
		// Run the game method
		game();
		
	}
	
	public static void game() {
		
		// Local variable to run loop
		boolean loop = true;
		
		System.out.println("IT'S YOUR TURN!");
		
		drawBoard();
		
		do {
			
			System.out.println("\n\nChoose a column and row to place an " + TicTacTe.team + ". (EXAMPLE: A1)\n");
			
			System.out.print("Enter your selction: ");
			Scanner input = new Scanner(System.in);
			TicTacTe.usrStr = input.next().toUpperCase();
			
			switch (TicTacTe.usrStr)
			{
				case "A1" : if (TicTacTe.place[0]=='_') {
					
					TicTacTe.place[0] = TicTacTe.team;
					System.out.println("\nYou place an " + TicTacTe.team + " in A1");
					oppMove();
					loop = false;
					
				} else if (TicTacTe.place[0]==TicTacTe.team) {
					
					System.out.println("\nThere is an " + TicTacTe.team + " there already!");
					
				} else if (TicTacTe.place[0]==TicTacTe.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "B1" : if (TicTacTe.place[1]=='_') {
					
					TicTacTe.place[1] = TicTacTe.team;
					System.out.println("\nYou place an " + TicTacTe.team + " in B1");
					oppMove();
					loop = false;
					
				} else if (TicTacTe.place[1]==TicTacTe.team) {
					
					System.out.println("\nThere is an " + TicTacTe.team + " there already!");
					
				} else if (TicTacTe.place[1]==TicTacTe.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "C1" : if (TicTacTe.place[2]=='_') {
					
					TicTacTe.place[2] = TicTacTe.team;
					System.out.println("\nYou place an " + TicTacTe.team + " in C1");
					oppMove();
					loop = false;
					
				} else if (TicTacTe.place[2]==TicTacTe.team) {
					
					System.out.println("\nThere is an " + TicTacTe.team + " there already!");
					
				} else if (TicTacTe.place[2]==TicTacTe.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "A2" : if (TicTacTe.place[3]=='_') {
					
					TicTacTe.place[3] = TicTacTe.team;
					System.out.println("\nYou place an " + TicTacTe.team + " in A2");
					oppMove();
					loop = false;
					
				} else if (TicTacTe.place[3]==TicTacTe.team) {
					
					System.out.println("\nThere is an " + TicTacTe.team + " there already!");
				} else if (TicTacTe.place[3]==TicTacTe.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "B2" : if (TicTacTe.place[4]=='_') {
					
					TicTacTe.place[4] = TicTacTe.team;
					System.out.println("\nYou place an " + TicTacTe.team + " in B2");
					oppMove();
					loop = false;
					
				} else if (TicTacTe.place[4]==TicTacTe.team) {
					
					System.out.println("\nThere is an " + TicTacTe.team + " there already!");
					
				} else if (TicTacTe.place[4]==TicTacTe.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "C2" : if (TicTacTe.place[5]=='_') {
					
					TicTacTe.place[5] = TicTacTe.team;
					System.out.println("\nYou place an " + TicTacTe.team + " in C2");
					oppMove();
					loop = false;
					
				} else if (TicTacTe.place[5]==TicTacTe.team) {
					
					System.out.println("\nThere is an " + TicTacTe.team + " there already!");
					
				} else if (TicTacTe.place[5]==TicTacTe.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "A3" : if (TicTacTe.place[6]=='_') {
					
					TicTacTe.place[6] = TicTacTe.team;
					System.out.println("\nYou place an " + TicTacTe.team + " in A3");
					oppMove();
					loop = false;
					
				} else if (TicTacTe.place[6]==TicTacTe.team) {
					
					System.out.println("\nThere is an " + TicTacTe.team + " there already!");
					
				} else if (TicTacTe.place[6]==TicTacTe.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "B3" : if (TicTacTe.place[7]=='_') {
					
					TicTacTe.place[7] = TicTacTe.team;
					System.out.println("\nYou place an " + TicTacTe.team + " in B3");
					oppMove();
					loop = false;
					
				} else if (TicTacTe.place[7]==TicTacTe.team) {
					
					System.out.println("\nThere is an " + TicTacTe.team + " there already!");
					
				} else if (TicTacTe.place[7]==TicTacTe.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "C3" : if (TicTacTe.place[8]=='_') {
					
					TicTacTe.place[8] = TicTacTe.team;
					System.out.println("\nYou place an " + TicTacTe.team + " in C3");
					oppMove();
					loop = false;
					
				} else if (TicTacTe.place[8]==TicTacTe.team) {
					
					System.out.println("\nThere is an " + TicTacTe.team + " there already!");
					
				} else if (TicTacTe.place[8]==TicTacTe.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
			}
			
		} while (loop);
		
		checkWin();
		
	}
	
	////////////////////////////////////////////////////////////////////////////////////////////////////////////

	public static void checkLines() {



		/*public class Example
		{
		    public String name;
		    public String location;

		    public String[] getExample()
		    {
		        String ar[] = new String[2];
		        ar[0]= name;
		        ar[1] =  location;
		        return ar; //returning two values at once
		    }
		}*/


		String p0=String.valueOf(TicTacTe.place[0]);
		String p1=String.valueOf(TicTacTe.place[1]);
		String p2=String.valueOf(TicTacTe.place[2]);
		String p3=String.valueOf(TicTacTe.place[3]);
		String p4=String.valueOf(TicTacTe.place[4]);
		String p5=String.valueOf(TicTacTe.place[5]);
		String p6=String.valueOf(TicTacTe.place[6]);
		String p7=String.valueOf(TicTacTe.place[7]);
		String p8=String.valueOf(TicTacTe.place[8]);

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

		String p0=String.valueOf(TicTacTe.place[0]);
		String p1=String.valueOf(TicTacTe.place[1]);
		String p2=String.valueOf(TicTacTe.place[2]);
		String p3=String.valueOf(TicTacTe.place[3]);
		String p4=String.valueOf(TicTacTe.place[4]);
		String p5=String.valueOf(TicTacTe.place[5]);
		String p6=String.valueOf(TicTacTe.place[6]);
		String p7=String.valueOf(TicTacTe.place[7]);
		String p8=String.valueOf(TicTacTe.place[8]);

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


		while (true) {

			if ( (line1_count > 0) || ( line2_count > 0 ) || ( line3_count > 0 ) ) {

				float rn = (float) Math.random();
				// System.out.println("(float) Math.random() :" + rn);
				float m = rn * 8;
				// System.out.println("m = rn * 8 :" + m);
				int x = Math.round(m);
				// System.out.println("Math.round(m) :" + x);

				
				if (TicTacTe.place[x]=='_') {
					
					TicTacTe.place[x] = TicTacTe.opp;
					break;
					
				}
				
			} else { checkWin(); break; }
				
			}
			
		}


	public static void checkWin() {
		
		// See if X has won the game
		
		if ( (TicTacTe.place[0]=='X') && (TicTacTe.place[1]=='X') && (TicTacTe.place[2]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTe.place[3]=='X') && (TicTacTe.place[4]=='X') && (TicTacTe.place[5]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTe.place[6]=='X') && (TicTacTe.place[7]=='X') && (TicTacTe.place[8]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTe.place[0]=='X') && (TicTacTe.place[3]=='X') && (TicTacTe.place[6]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTe.place[1]=='X') && (TicTacTe.place[4]=='X') && (TicTacTe.place[7]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTe.place[2]=='X') && (TicTacTe.place[5]=='X') && (TicTacTe.place[8]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTe.place[0]=='X') && (TicTacTe.place[4]=='X') && (TicTacTe.place[8]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTe.place[6]=='X') && (TicTacTe.place[4]=='X') && (TicTacTe.place[2]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
		}
		
		// Now, see if O has won!
		
		if ( (TicTacTe.place[0]=='O') && (TicTacTe.place[1]=='O') && (TicTacTe.place[2]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTe.place[3]=='O') && (TicTacTe.place[4]=='O') && (TicTacTe.place[5]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTe.place[6]=='O') && (TicTacTe.place[7]=='O') && (TicTacTe.place[8]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTe.place[0]=='O') && (TicTacTe.place[3]=='O') && (TicTacTe.place[6]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTe.place[1]=='O') && (TicTacTe.place[4]=='O') && (TicTacTe.place[7]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTe.place[2]=='O') && (TicTacTe.place[5]=='O') && (TicTacTe.place[8]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTe.place[0]=='O') && (TicTacTe.place[4]=='O') && (TicTacTe.place[8]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacTe.place[6]=='O') && (TicTacTe.place[4]=='O') && (TicTacTe.place[2]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
		
		// Check for a tie!
		
		} else if ( (TicTacTe.place[0]!='_') && (TicTacTe.place[1]!='_') && (TicTacTe.place[2]!='_') && (TicTacTe.place[3]!='_') && (TicTacTe.place[4]!='_') && (TicTacTe.place[5]!='_') && (TicTacTe.place[6]!='_') && (TicTacTe.place[7]!='_') && (TicTacTe.place[8]!='_') ) {
			
			System.out.println("\n\n\n\tTIE GAME!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
		
		// If no one has won and no tie, keep playing!!
		
		} else { game(); }
		
	}
	
	public static void playAgain() {
		
			System.out.print("\n\nPlay again? [y/n]: ");
			Scanner input = new Scanner(System.in);
			TicTacTe.usrStr = input.next().toLowerCase();
			
			if (usrStr.equals("y")) {
				
				TicTacTe.team = '_';
				TicTacTe.opp = '_';
				setup();
				
			} else {
				
				System.exit(0);
				
			}
		
	}
	
}