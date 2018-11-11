import java.util.Scanner;

class TicTacT {
	
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
		System.out.println("\t1 |_"+TicTacT.place[0]+"_|_"+TicTacT.place[1]+"_|_"+TicTacT.place[2]+"_|\n");
		System.out.println("\t2 |_"+TicTacT.place[3]+"_|_"+TicTacT.place[4]+"_|_"+TicTacT.place[5]+"_|\n");
		System.out.println("\t3 |_"+TicTacT.place[6]+"_|_"+TicTacT.place[7]+"_|_"+TicTacT.place[8]+"_|");
		System.out.println("\t  '-----------'");
		
	}
	
	public static void setup() {
		
		// Loop to reset the game board
		for ( int i = 0 ; i < 9 ; i++ ) {
			
			TicTacT.place[i] = '_';
			
		}
		
		// Print the game board to the console
		drawBoard();
		
		while ( (TicTacT.team != 'X') && (TicTacT.team != 'O') ) {
			
			System.out.println("\n\nSelect Your Team! Enter 'X' or 'O' below...");
			
			System.out.print("Enter your selection: ");
			Scanner input = new Scanner(System.in);
			TicTacT.usrStr = input.next();
			
			if (TicTacT.usrStr.toUpperCase().equals("X")) {
				
				TicTacT.team = 'X';
				TicTacT.opp = 'O';
				
			} else if (TicTacT.usrStr.toUpperCase().equals("O")) {
				
				TicTacT.team = 'O';
				TicTacT.opp = 'X';
				
			} else {
				
				System.out.println("You entered: " + usrStr);
				System.out.println("This is not a valid option.");
				System.out.println("Please enter either an X or an O to continue.");
				
			}
			
		}
		
		System.out.println("\nYou are team " + TicTacT.team + "!");
		
		// Run the game method
		game();
		
	}
	
	public static void game() {
		
		// Local variable to run loop
		boolean loop = true;
		
		System.out.println("IT'S YOUR TURN!");
		
		drawBoard();
		
		do {
			
			System.out.println("\n\nChoose a column and row to place an " + TicTacT.team + ". (EXAMPLE: A1)\n");
			
			System.out.print("Enter your selction: ");
			Scanner input = new Scanner(System.in);
			TicTacT.usrStr = input.next().toUpperCase();
			
			switch (TicTacT.usrStr)
			{
				case "A1" : if (TicTacT.place[0]=='_') {
					
					TicTacT.place[0] = TicTacT.team;
					System.out.println("\nYou place an " + TicTacT.team + " in A1");
					oppMove();
					loop = false;
					
				} else if (TicTacT.place[0]==TicTacT.team) {
					
					System.out.println("\nThere is an " + TicTacT.team + " there already!");
					
				} else if (TicTacT.place[0]==TicTacT.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "B1" : if (TicTacT.place[1]=='_') {
					
					TicTacT.place[1] = TicTacT.team;
					System.out.println("\nYou place an " + TicTacT.team + " in B1");
					oppMove();
					loop = false;
					
				} else if (TicTacT.place[1]==TicTacT.team) {
					
					System.out.println("\nThere is an " + TicTacT.team + " there already!");
					
				} else if (TicTacT.place[1]==TicTacT.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "C1" : if (TicTacT.place[2]=='_') {
					
					TicTacT.place[2] = TicTacT.team;
					System.out.println("\nYou place an " + TicTacT.team + " in C1");
					oppMove();
					loop = false;
					
				} else if (TicTacT.place[2]==TicTacT.team) {
					
					System.out.println("\nThere is an " + TicTacT.team + " there already!");
					
				} else if (TicTacT.place[2]==TicTacT.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "A2" : if (TicTacT.place[3]=='_') {
					
					TicTacT.place[3] = TicTacT.team;
					System.out.println("\nYou place an " + TicTacT.team + " in A2");
					oppMove();
					loop = false;
					
				} else if (TicTacT.place[3]==TicTacT.team) {
					
					System.out.println("\nThere is an " + TicTacT.team + " there already!");
					
				} else if (TicTacT.place[3]==TicTacT.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "B2" : if (TicTacT.place[4]=='_') {
					
					TicTacT.place[4] = TicTacT.team;
					System.out.println("\nYou place an " + TicTacT.team + " in B2");
					oppMove();
					loop = false;
					
				} else if (TicTacT.place[4]==TicTacT.team) {
					
					System.out.println("\nThere is an " + TicTacT.team + " there already!");
					
				} else if (TicTacT.place[4]==TicTacT.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "C2" : if (TicTacT.place[5]=='_') {
					
					TicTacT.place[5] = TicTacT.team;
					System.out.println("\nYou place an " + TicTacT.team + " in C2");
					oppMove();
					loop = false;
					
				} else if (TicTacT.place[5]==TicTacT.team) {
					
					System.out.println("\nThere is an " + TicTacT.team + " there already!");
					
				} else if (TicTacT.place[5]==TicTacT.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "A3" : if (TicTacT.place[6]=='_') {
					
					TicTacT.place[6] = TicTacT.team;
					System.out.println("\nYou place an " + TicTacT.team + " in A3");
					oppMove();
					loop = false;
					
				} else if (TicTacT.place[6]==TicTacT.team) {
					
					System.out.println("\nThere is an " + TicTacT.team + " there already!");
					
				} else if (TicTacT.place[6]==TicTacT.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "B3" : if (TicTacT.place[7]=='_') {
					
					TicTacT.place[7] = TicTacT.team;
					System.out.println("\nYou place an " + TicTacT.team + " in B3");
					oppMove();
					loop = false;
					
				} else if (TicTacT.place[7]==TicTacT.team) {
					
					System.out.println("\nThere is an " + TicTacT.team + " there already!");
					
				} else if (TicTacT.place[7]==TicTacT.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
				
				case "C3" : if (TicTacT.place[8]=='_') {
					
					TicTacT.place[8] = TicTacT.team;
					System.out.println("\nYou place an " + TicTacT.team + " in C3");
					oppMove();
					loop = false;
					
				} else if (TicTacT.place[8]==TicTacT.team) {
					
					System.out.println("\nThere is an " + TicTacT.team + " there already!");
					
				} else if (TicTacT.place[8]==TicTacT.opp) {
					
					System.out.println("\nThis space is already taken!");
					
				}; break;
			}
			
		} while (loop);
		
		checkWin();
		
	}
	
	public static void oppMove() {
		
		while (true) {
			
			if ( (TicTacT.place[0]=='_') || (TicTacT.place[1]=='_') || (TicTacT.place[2]=='_') || (TicTacT.place[3]=='_') || (TicTacT.place[4]=='_') || (TicTacT.place[5]=='_') || (TicTacT.place[6]=='_') || (TicTacT.place[7]=='_') || (TicTacT.place[8]=='_') ) {

				////////* TicTacT.opp == 'O' *////////
				if ( TicTacT.opp == 'O' ) {

					System.out.println("TicTacT.opp == 'O' 274");
					///* 0, 1 ,2 *///
					if ( (TicTacT.place[0] == 'X'&&TicTacT.place[1] == 'X') || (TicTacT.place[0] == 'X'&&TicTacT.place[2] == 'X') || (TicTacT.place[1] == 'X'&&TicTacT.place[2] == 'X')) {

						System.out.println("if 278");
						boolean zero_one = (TicTacT.place[0] == 'X'&&TicTacT.place[1] == 'X');
						boolean zero_two = (TicTacT.place[0] == 'X'&&TicTacT.place[2] == 'X');
						if (zero_one) {

							System.out.println("222");
							TicTacT.place[2] = TicTacT.opp;
							break;

						} else if (zero_two) {
							System.out.println("333");
							TicTacT.place[1] = TicTacT.opp;
							break;
						
						} else {
								
								if (TicTacT.place[0]=='_') {
									TicTacT.place[0] = TicTacT.opp;
									break;

								} 	
						}
						
					///* 3, 4 ,5 *///
					} else if  ( (TicTacT.place[3] == 'X'&&TicTacT.place[4] == 'X') || (TicTacT.place[3] == 'X'&&TicTacT.place[5] == 'X') || (TicTacT.place[4] == 'X'&&TicTacT.place[5] == 'X')) {

						System.out.println("else if 314");
						boolean zero_one = (TicTacT.place[3] == 'X'&&TicTacT.place[4] == 'X');
						boolean zero_two = (TicTacT.place[3] == 'X'&&TicTacT.place[5] == 'X');
						if (zero_one) {

							TicTacT.place[5] = TicTacT.opp;
							break;

						} else if (zero_two) {

							TicTacT.place[4] = TicTacT.opp;
							break;

						} else {
								
								if (TicTacT.place[3]=='_') {
									TicTacT.place[3] = TicTacT.opp;
									break;

								} else {
									System.out.println("543");
									float rn = (float) Math.random();
									// System.out.println("(float) Math.random() :" + rn);
									float m = rn * 8;
									// System.out.println("m = rn * 8 :" + m);
									int x = Math.round(m);
									// System.out.println("Math.round(m) :" + x);

									if (TicTacT.place[x]=='_') {
										
										TicTacT.place[x] = TicTacT.opp;
										break;	
									}
								}	
						}
						


					///* 6, 7 ,8 *///
					} else if  ( (TicTacT.place[6] == 'X'&&TicTacT.place[7] == 'X') || (TicTacT.place[6] == 'X'&&TicTacT.place[8] == 'X') || (TicTacT.place[7] == 'X'&&TicTacT.place[8] == 'X')) {

						System.out.println("else if 351");
						boolean zero_one = (TicTacT.place[6] == 'X'&&TicTacT.place[7] == 'X');
						boolean zero_two = (TicTacT.place[6] == 'X'&&TicTacT.place[8] == 'X');
						if (zero_one) {

							TicTacT.place[8] = TicTacT.opp;
							break;

						} else if (zero_two) {

							TicTacT.place[7] = TicTacT.opp;
							break;

						} else {
								
								if (TicTacT.place[6]=='_') {
									TicTacT.place[6] = TicTacT.opp;
									break;

								} else {
									System.out.println("876");
									float rn = (float) Math.random();
									// System.out.println("(float) Math.random() :" + rn);
									float m = rn * 8;
									// System.out.println("m = rn * 8 :" + m);
									int x = Math.round(m);
									// System.out.println("Math.round(m) :" + x);

									if (TicTacT.place[x]=='_') {
										
										TicTacT.place[x] = TicTacT.opp;
										break;	
									}
								}	
						}
						


					///* 0, 3 ,6 *///
					} else if  ( (TicTacT.place[0] == 'X'&&TicTacT.place[3] == 'X') || (TicTacT.place[0] == 'X'&&TicTacT.place[6] == 'X') || (TicTacT.place[3] == 'X'&&TicTacT.place[6] == 'X')) {

						System.out.println("else if 388");
						boolean zero_one = (TicTacT.place[0] == 'X'&&TicTacT.place[3] == 'X');
						boolean zero_two = (TicTacT.place[0] == 'X'&&TicTacT.place[6] == 'X');
						if (zero_one) {

							TicTacT.place[6] = TicTacT.opp;
							break;

						} else if (zero_two) {

							TicTacT.place[3] = TicTacT.opp;
							break;

						} else {
								
								if (TicTacT.place[0]=='_') {
									TicTacT.place[0] = TicTacT.opp;
									break;

								} else {
									System.out.println("630");
									float rn = (float) Math.random();
									// System.out.println("(float) Math.random() :" + rn);
									float m = rn * 8;
									// System.out.println("m = rn * 8 :" + m);
									int x = Math.round(m);
									// System.out.println("Math.round(m) :" + x);

									if (TicTacT.place[x]=='_') {
										
										TicTacT.place[x] = TicTacT.opp;
										break;	
									}
								}	
						}
						


					///* 1, 4 ,7 *///
					} else if  ( (TicTacT.place[1] == 'X'&&TicTacT.place[4] == 'X') || (TicTacT.place[1] == 'X'&&TicTacT.place[7] == 'X') || (TicTacT.place[4] == 'X'&&TicTacT.place[7] == 'X')) {

						System.out.println("else if 425");
						boolean zero_one = (TicTacT.place[1] == 'X'&&TicTacT.place[4] == 'X');
						boolean zero_two = (TicTacT.place[1] == 'X'&&TicTacT.place[7] == 'X');
						if (zero_one) {

							TicTacT.place[7] = TicTacT.opp;
							break;

						} else if (zero_two) {

							TicTacT.place[4] = TicTacT.opp;
							break;

						} else {
								
								if (TicTacT.place[1]=='_') {
									TicTacT.place[1] = TicTacT.opp;
									break;

								} else {
									System.out.println("741");
									float rn = (float) Math.random();
									// System.out.println("(float) Math.random() :" + rn);
									float m = rn * 8;
									// System.out.println("m = rn * 8 :" + m);
									int x = Math.round(m);
									// System.out.println("Math.round(m) :" + x);

									if (TicTacT.place[x]=='_') {
										
										TicTacT.place[x] = TicTacT.opp;
										break;	
									}
								}	
						}
						



					///* 2, 5 ,8 *///
					} else if  ( (TicTacT.place[2] == 'X'&&TicTacT.place[5] == 'X') || (TicTacT.place[2] == 'X'&&TicTacT.place[8] == 'X') || (TicTacT.place[5] == 'X'&&TicTacT.place[8] == 'X')) {

						System.out.println("else if 463");
						boolean zero_one = (TicTacT.place[2] == 'X'&&TicTacT.place[5] == 'X');
						boolean zero_two = (TicTacT.place[2] == 'X'&&TicTacT.place[8] == 'X');
						if (zero_one) {

							TicTacT.place[8] = TicTacT.opp;
							break;

						} else if (zero_two) {

							TicTacT.place[5] = TicTacT.opp;
							break;

						} else {
								
								if (TicTacT.place[2]=='_') {
									TicTacT.place[2] = TicTacT.opp;
									break;

								} else {
									System.out.println("852");
									float rn = (float) Math.random();
									// System.out.println("(float) Math.random() :" + rn);
									float m = rn * 8;
									// System.out.println("m = rn * 8 :" + m);
									int x = Math.round(m);
									// System.out.println("Math.round(m) :" + x);

									if (TicTacT.place[x]=='_') {
										
										TicTacT.place[x] = TicTacT.opp;
										break;	
									}
								}	
						}
						


					///* 0, 4 ,8 *///
					} else if  ( (TicTacT.place[0] == 'X'&&TicTacT.place[4] == 'X') || (TicTacT.place[0] == 'X'&&TicTacT.place[8] == 'X') || (TicTacT.place[4] == 'X'&&TicTacT.place[8] == 'X')) {

						System.out.println("else if 500");
						boolean zero_one = (TicTacT.place[0] == 'X'&&TicTacT.place[4] == 'X');
						boolean zero_two = (TicTacT.place[0] == 'X'&&TicTacT.place[8] == 'X');
						if (zero_one) {

							TicTacT.place[8] = TicTacT.opp;
							break;

						} else if (zero_two) {

							TicTacT.place[4] = TicTacT.opp;
							break;

						} else {
								
								if (TicTacT.place[0]=='_') {
									TicTacT.place[0] = TicTacT.opp;
									break;

								} else {
									System.out.println("840");
									float rn = (float) Math.random();
									// System.out.println("(float) Math.random() :" + rn);
									float m = rn * 8;
									// System.out.println("m = rn * 8 :" + m);
									int x = Math.round(m);
									// System.out.println("Math.round(m) :" + x);

									if (TicTacT.place[x]=='_') {
										
										TicTacT.place[x] = TicTacT.opp;
										break;	
									}
								}	
						}
						


					///* 2, 4 ,6 *///
					} else if  ( (TicTacT.place[2] == 'X'&&TicTacT.place[4] == 'X') || (TicTacT.place[2] == 'X'&&TicTacT.place[6] == 'X') || (TicTacT.place[4] == 'X'&&TicTacT.place[6] == 'X')) {

						System.out.println("else if 537");
						boolean zero_one = (TicTacT.place[2] == 'X'&&TicTacT.place[4] == 'X');
						boolean zero_two = (TicTacT.place[2] == 'X'&&TicTacT.place[6] == 'X');
						if (zero_one) {

							TicTacT.place[6] = TicTacT.opp;
							break;

						} else if (zero_two) {

							TicTacT.place[4] = TicTacT.opp;
							break;

						} else {
								
								if (TicTacT.place[2]=='_') {
									TicTacT.place[2] = TicTacT.opp;
								} else {
									System.out.println("642");
									float rn = (float) Math.random();
									// System.out.println("(float) Math.random() :" + rn);
									float m = rn * 8;
									// System.out.println("m = rn * 8 :" + m);
									int x = Math.round(m);
									// System.out.println("Math.round(m) :" + x);

									if (TicTacT.place[x]=='_') {
										
										TicTacT.place[x] = TicTacT.opp;
										break;	
									}
								}	
						}
						
					} else {
						System.out.println("endo_of_xxx_move 570");
						float rn = (float) Math.random();
						// System.out.println("(float) Math.random() :" + rn);
						float m = rn * 8;
						// System.out.println("m = rn * 8 :" + m);
						int x = Math.round(m);
						// System.out.println("Math.round(m) :" + x);
						
						if (TicTacT.place[x]=='_') {
							
							TicTacT.place[x] = TicTacT.opp;
							break;
						}
					}

				}

				if ( TicTacT.opp == 'X') {

					System.out.println("TicTacT.opp == 'X' 589");
					///* 0, 1 ,2 *///
					if ( (TicTacT.place[0] == 'O'&&TicTacT.place[1] == 'O') || (TicTacT.place[0] == 'O'&&TicTacT.place[2] == 'O') || (TicTacT.place[1] == 'O'&&TicTacT.place[2] == 'O')) {

						System.out.println("if 592");
						boolean zero_one = (TicTacT.place[0] == 'O'&&TicTacT.place[1] == 'O');
						boolean zero_two = (TicTacT.place[0] == 'O'&&TicTacT.place[2] == 'O');
						if (zero_one) {

							TicTacT.place[2] = TicTacT.opp;
							break;

						} else if (zero_two) {

							TicTacT.place[1] = TicTacT.opp;
							break;

						} else {
								
								if (TicTacT.place[0]=='_') {
									TicTacT.place[0] = TicTacT.opp;
									break;

								} 	
						}
						


					///* 3, 4 ,5 *///
					} else if  ( (TicTacT.place[3] == 'O'&&TicTacT.place[4] == 'O') || (TicTacT.place[3] == 'O'&&TicTacT.place[5] == 'O') || (TicTacT.place[4] == 'O'&&TicTacT.place[5] == 'O')) {

						System.out.println("else if 629");
						boolean zero_one = (TicTacT.place[3] == 'O'&&TicTacT.place[4] == 'O');
						boolean zero_two = (TicTacT.place[3] == 'O'&&TicTacT.place[5] == 'O');
						if (zero_one) {

							TicTacT.place[5] = TicTacT.opp;
							break;

						} else if (zero_two) {

							TicTacT.place[4] = TicTacT.opp;
							break;

						} else {
								
								if (TicTacT.place[3]=='_') {
									TicTacT.place[3] = TicTacT.opp;
									break;

								} else {
									System.out.println("543");
									float rn = (float) Math.random();
									// System.out.println("(float) Math.random() :" + rn);
									float m = rn * 8;
									// System.out.println("m = rn * 8 :" + m);
									int x = Math.round(m);
									// System.out.println("Math.round(m) :" + x);

									if (TicTacT.place[x]=='_') {
										
										TicTacT.place[x] = TicTacT.opp;
										break;	
									}
								}	
						}
						


					///* 6, 7 ,8 *///
					} else if  ( (TicTacT.place[6] == 'O'&&TicTacT.place[7] == 'O') || (TicTacT.place[6] == 'O'&&TicTacT.place[8] == 'O') || (TicTacT.place[7] == 'O'&&TicTacT.place[8] == 'O')) {

						System.out.println("else if 666");
						boolean zero_one = (TicTacT.place[6] == 'O'&&TicTacT.place[7] == 'O');
						boolean zero_two = (TicTacT.place[6] == 'O'&&TicTacT.place[8] == 'O');
						if (zero_one) {

							TicTacT.place[8] = TicTacT.opp;
							break;

						} else if (zero_two) {

							TicTacT.place[7] = TicTacT.opp;
							break;

						} else {
								
								if (TicTacT.place[6]=='_') {
									TicTacT.place[6] = TicTacT.opp;
									break;

								} else {
									System.out.println("876");
									float rn = (float) Math.random();
									// System.out.println("(float) Math.random() :" + rn);
									float m = rn * 8;
									// System.out.println("m = rn * 8 :" + m);
									int x = Math.round(m);
									// System.out.println("Math.round(m) :" + x);

									if (TicTacT.place[x]=='_') {
										
										TicTacT.place[x] = TicTacT.opp;
										break;	
									}
								}	
						}
						


					///* 0, 3 ,6 *///
					} else if  ( (TicTacT.place[0] == 'O'&&TicTacT.place[3] == 'O') || (TicTacT.place[0] == 'O'&&TicTacT.place[6] == 'O') || (TicTacT.place[3] == 'O'&&TicTacT.place[6] == 'O')) {

						System.out.println("else if 703");
						boolean zero_one = (TicTacT.place[0] == 'O'&&TicTacT.place[3] == 'O');
						boolean zero_two = (TicTacT.place[0] == 'O'&&TicTacT.place[6] == 'O');
						if (zero_one) {

							TicTacT.place[6] = TicTacT.opp;
							break;  //continue;

						} else if (zero_two) {

							TicTacT.place[3] = TicTacT.opp;
							break;

						} else {
								
								if (TicTacT.place[0]=='_') {
									TicTacT.place[0] = TicTacT.opp;
									break;

								} else {
									System.out.println("630");
									float rn = (float) Math.random();
									// System.out.println("(float) Math.random() :" + rn);
									float m = rn * 8;
									// System.out.println("m = rn * 8 :" + m);
									int x = Math.round(m);
									// System.out.println("Math.round(m) :" + x);

									if (TicTacT.place[x]=='_') {
										
										TicTacT.place[x] = TicTacT.opp;
										break;	
									}
								}	
						}
						


					///* 1, 4 ,7 *///
					} else if  ( (TicTacT.place[1] == 'O'&&TicTacT.place[4] == 'O') || (TicTacT.place[1] == 'O'&&TicTacT.place[7] == 'O') || (TicTacT.place[4] == 'O'&&TicTacT.place[7] == 'O')) {

						System.out.println("else if 740");
						boolean zero_one = (TicTacT.place[1] == 'O'&&TicTacT.place[4] == 'O');
						boolean zero_two = (TicTacT.place[1] == 'O'&&TicTacT.place[7] == 'O');
						if (zero_one) {

							TicTacT.place[7] = TicTacT.opp;
							break;

						} else if (zero_two) {

							TicTacT.place[4] = TicTacT.opp;
							break;

						} else {
								
								if (TicTacT.place[1]=='_') {
									TicTacT.place[1] = TicTacT.opp;
									break;

								} else {
									System.out.println("741");
									float rn = (float) Math.random();
									// System.out.println("(float) Math.random() :" + rn);
									float m = rn * 8;
									// System.out.println("m = rn * 8 :" + m);
									int x = Math.round(m);
									// System.out.println("Math.round(m) :" + x);

									if (TicTacT.place[x]=='_') {
										
										TicTacT.place[x] = TicTacT.opp;
										break;	
									}
								}	
						}



					///* 2, 5 ,8 *///
					} else if  ( (TicTacT.place[2] == 'O'&&TicTacT.place[5] == 'O') || (TicTacT.place[2] == 'O'&&TicTacT.place[8] == 'O') || (TicTacT.place[5] == 'O'&&TicTacT.place[8] == 'O')) {

						System.out.println("else if 777");
						boolean zero_one = (TicTacT.place[2] == 'O'&&TicTacT.place[5] == 'O');
						boolean zero_two = (TicTacT.place[2] == 'O'&&TicTacT.place[8] == 'O');
						if (zero_one) {

							TicTacT.place[8] = TicTacT.opp;
							break;

						} else if (zero_two) {

							TicTacT.place[5] = TicTacT.opp;
							break;

						} else {
								
								if (TicTacT.place[2]=='_') {
									TicTacT.place[2] = TicTacT.opp;
								} else {
									System.out.println("852");
									float rn = (float) Math.random();
									// System.out.println("(float) Math.random() :" + rn);
									float m = rn * 8;
									// System.out.println("m = rn * 8 :" + m);
									int x = Math.round(m);
									// System.out.println("Math.round(m) :" + x);

									if (TicTacT.place[x]=='_') {
										
										TicTacT.place[x] = TicTacT.opp;
										break;	
									}
								}	
						}
						


					///* 0, 4 ,8 *///
					} else if  ( (TicTacT.place[0] == 'O'&&TicTacT.place[4] == 'O') || (TicTacT.place[0] == 'O'&&TicTacT.place[8] == 'O') || (TicTacT.place[4] == 'O'&&TicTacT.place[8] == 'O')) {

						System.out.println("else if 814");
						boolean zero_one = (TicTacT.place[0] == 'O'&&TicTacT.place[4] == 'O');
						boolean zero_two = (TicTacT.place[0] == 'O'&&TicTacT.place[8] == 'O');
						if (zero_one) {

							TicTacT.place[8] = TicTacT.opp;
							break;

						} else if (zero_two) {

							TicTacT.place[4] = TicTacT.opp;
							break;

						} else {
								
								if (TicTacT.place[0]=='_') {
									TicTacT.place[0] = TicTacT.opp;
									break;

								} else {
									System.out.println("840");
									float rn = (float) Math.random();
									// System.out.println("(float) Math.random() :" + rn);
									float m = rn * 8;
									// System.out.println("m = rn * 8 :" + m);
									int x = Math.round(m);
									// System.out.println("Math.round(m) :" + x);

									if (TicTacT.place[x]=='_') {
										
										TicTacT.place[x] = TicTacT.opp;
										break;	
									}
								}	
						}
						


					///* 2, 4 ,6 *///
					} else if  ( (TicTacT.place[2] == 'O'&&TicTacT.place[4] == 'O') || (TicTacT.place[2] == 'O'&&TicTacT.place[6] == 'O') || (TicTacT.place[4] == 'O'&&TicTacT.place[6] == 'O')) {

						System.out.println("else if 851");
						boolean zero_one = (TicTacT.place[2] == 'O'&&TicTacT.place[4] == 'O');
						boolean zero_two = (TicTacT.place[2] == 'O'&&TicTacT.place[6] == 'O');
						if (zero_one) {

							TicTacT.place[6] = TicTacT.opp;
							break;

						} else if (zero_two) {

							TicTacT.place[4] = TicTacT.opp;
							break;

						} else {
								
								if (TicTacT.place[2]=='_') {
									TicTacT.place[2] = TicTacT.opp;
									break;
									
								} else {
									System.out.println("642");
									float rn = (float) Math.random();
									// System.out.println("(float) Math.random() :" + rn);
									float m = rn * 8;
									// System.out.println("m = rn * 8 :" + m);
									int x = Math.round(m);
									// System.out.println("Math.round(m) :" + x);

									if (TicTacT.place[x]=='_') {
										
										TicTacT.place[x] = TicTacT.opp;
										break;	
									}
								}	
						}
						

					} else {

						System.out.println("end_of_ooo_move 886");
						float rn = (float) Math.random();
						// System.out.println("(float) Math.random() :" + rn);
						float m = rn * 8;
						// System.out.println("m = rn * 8 :" + m);
						int x = Math.round(m);
						// System.out.println("Math.round(m) :" + x);
						
						if (TicTacT.place[x]=='_') {
							
							TicTacT.place[x] = TicTacT.opp;
							break;
						}
					}

				}

				
			} else { checkWin(); break; }
				
			}
			
		}
	
	
	public static void checkWin() {
		
		// See if X has won the game
		
		if ( (TicTacT.place[0]=='X') && (TicTacT.place[1]=='X') && (TicTacT.place[2]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT.place[3]=='X') && (TicTacT.place[4]=='X') && (TicTacT.place[5]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT.place[6]=='X') && (TicTacT.place[7]=='X') && (TicTacT.place[8]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT.place[0]=='X') && (TicTacT.place[3]=='X') && (TicTacT.place[6]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT.place[1]=='X') && (TicTacT.place[4]=='X') && (TicTacT.place[7]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT.place[2]=='X') && (TicTacT.place[5]=='X') && (TicTacT.place[8]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT.place[0]=='X') && (TicTacT.place[4]=='X') && (TicTacT.place[8]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT.place[6]=='X') && (TicTacT.place[4]=='X') && (TicTacT.place[2]=='X') ) {
			
			System.out.println("\n\n\n\tX WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
		}
		
		// Now, see if O has won!
		
		if ( (TicTacT.place[0]=='O') && (TicTacT.place[1]=='O') && (TicTacT.place[2]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT.place[3]=='O') && (TicTacT.place[4]=='O') && (TicTacT.place[5]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT.place[6]=='O') && (TicTacT.place[7]=='O') && (TicTacT.place[8]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT.place[0]=='O') && (TicTacT.place[3]=='O') && (TicTacT.place[6]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT.place[1]=='O') && (TicTacT.place[4]=='O') && (TicTacT.place[7]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT.place[2]=='O') && (TicTacT.place[5]=='O') && (TicTacT.place[8]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT.place[0]=='O') && (TicTacT.place[4]=='O') && (TicTacT.place[8]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
			
		} else if ( (TicTacT.place[6]=='O') && (TicTacT.place[4]=='O') && (TicTacT.place[2]=='O') ) {
			
			System.out.println("\n\n\n\tO WINS!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
		
		// Check for a tie!
		
		} else if ( (TicTacT.place[0]!='_') && (TicTacT.place[1]!='_') && (TicTacT.place[2]!='_') && (TicTacT.place[3]!='_') && (TicTacT.place[4]!='_') && (TicTacT.place[5]!='_') && (TicTacT.place[6]!='_') && (TicTacT.place[7]!='_') && (TicTacT.place[8]!='_') ) {
			
			System.out.println("\n\n\n\tTIE GAME!!!!"); drawBoard(); playAgain(); System.out.println("\n\n");
		
		// If no one has won and no tie, keep playing!!
		
		} else { game(); }
		
	}
	
	public static void playAgain() {
		
			System.out.print("\n\nPlay again? [y/n]: ");
			Scanner input = new Scanner(System.in);
			TicTacT.usrStr = input.next().toLowerCase();
			
			if (usrStr.equals("y")) {
				
				TicTacT.team = '_';
				TicTacT.opp = '_';
				setup();
				
			} else {
				
				System.exit(0);
				
			}

	}
	
}