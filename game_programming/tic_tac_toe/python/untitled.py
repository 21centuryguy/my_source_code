'''
#############################################################
Tic-tac-toe game player.
Input the index of where you wish to place your mark at your turn.

http://rosettacode.org/wiki/Tic-tac-toe#Python
#############################################################
'''
 
import random
from inspect import currentframe, getframeinfo
import inspect
cf = currentframe()

board = list('123456789')
wins = ((0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6))

#####################################
def printboard():
    cf = currentframe(); print("[ DEBUG ] line :" + str(cf.f_lineno) + " def printboard() ")
    
    print("------")
    print('\n'.join(' '.join(board[x:x+3]) for x in(0,3,6)))
    print("------")

#####################################
def score():
    
    cf = currentframe(); print("[ DEBUG ] line :" + str(cf.f_lineno) + " def score() ")
    print(111)
    print(cf.f_back)
    print(222)
    print(cf.f_builtins)
    print(333)
    print(cf.f_code)
    print(444)
    print(cf.f_globals)
    print(555)
    print(cf.f_lasti)
    print(666)
    print(cf.f_lineno)
    print(777)
    print(cf.f_locals)
    print(888)
    # print(cf.f_restricted)
    print(999)
    print(cf.f_trace)
    print(1010)
    # print(cf)
    # print(inspect.stack())
    # print(inspect.stack())
    # print([s for s in inspect.stack() if "function='score'" in s])
    
    # print(len(inspect.stack()))

    print("1"*100)
    print(type(inspect.stack()))
    print("2"*100)
    print(len(inspect.stack()))
    print("3"*100)
    print([xxx for xxx in inspect.stack()])
    print("4"*100)
    print(inspect.stack()[0])
    print("5"*100)
    print(inspect.stack()[0][3]) 
    print("6"*100)
    print(inspect.stack()[0][2])   
    print("7"*100)

    # print(inspect.stack()[0])
    # print(inspect.stack()[1])
    # print(inspect.stack()[2])
    # print(inspect.stack()[0][2])
    # print(inspect.stack()[0][3])
    print("[ DEBUG ] line :" + str(cf.f_lineno) + " wins : ", wins)
    for w in wins:
        print("[ DEBUG ] line :" + str(cf.f_lineno) + " w : ", w)
        b = board[w[0]]
        print("[ DEBUG ] line :" + str(cf.f_lineno) + " b : ", b)
        if b in 'XO' and all (board[i] == b for i in w):
            return b, [i+1 for i in w]
            print("[ DEBUG ] line :" + str(cf.f_lineno) + " b : ", b)
    return None, None

##################################### 
def finished():
    cf = currentframe(); print("[ DEBUG ] line :" + str(cf.f_lineno) + " def finished() ")

    return all (b in 'XO' for b in board)
 
##################################### 
def space():
    cf = currentframe(); print("[ DEBUG ] line :" + str(cf.f_lineno) + " def space() ")

    return [ b for b in board if b not in 'XO']

##################################### 
def my_turn(xo):
    cf = currentframe(); print("[ DEBUG ] line :" + str(cf.f_lineno) + " def my_turn(xo) ")

    options = space()
    print("line 43 options : ",options)
    print("line 46 / board :",board)
    choice = random.choice(options)
    print("line 44 choice : ",choice)
    board[int(choice)-1] = xo
    board[int(choice)-1] = xo
    return choice

##################################### 
def your_turn(xo):
    cf = currentframe(); print("[ DEBUG ] line :" + str(cf.f_lineno) + " def your_turn(xo) ")

    options = space()
    while True:
        choice = input(" Put your %s in any of these positions: %s : "
                       % (xo, ''.join(options))).strip()
        if choice in options:
            break
        print( "Whoops I don't understand the input" )
    board[int(choice)-1] = xo
    return choice

##################################### 
def me(xo='X'):
    cf = currentframe(); print("[ DEBUG ] line :" + str(cf.f_lineno) + " def me(xo='X')")

    printboard()
    print('I go at', my_turn(xo))
    return score()
    assert not s[0], "\n%s wins across %s" % s

##################################### 
def you(xo='O'):
    cf = currentframe(); print("[ DEBUG ] line :" + str(cf.f_lineno) + " def you(xo='O')")

    printboard()
    # Call my_turn(xo) below for it to play itself
    print('You went at', your_turn(xo))
    return score()
    assert not s[0], "\n%s wins across %s" % s
 
 
print(__doc__)
while not finished():
    s = me('X')
    if s[0]:
        printboard()
        print("\n%s wins across %s" % s)
        break
    if not finished():
        s = you('O')
        if s[0]:
            printboard()
            print("\n%s wins across %s" % s)
            break
else:
    print('\nA draw')
 