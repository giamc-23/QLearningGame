import random

def mingame(Q):
    if Q == "A000" or Q == "B000":
        return 0
    actionmap = dict()
    for i in QValues.keys():
        if i[0] == Q:
            actionmap[i[1]] = QValues[(i)]
    minimum = min(actionmap.values())
    for key in actionmap:
        if actionmap[key] == minimum:
            return key
def maxgame(Q):
    if Q == "A000" or Q == "B000":
        return 0
    actionmap = dict()
    for i in QValues.keys():
        if i[0] == Q:
            actionmap[i[1]] = QValues[(i)]
    maximum = max(actionmap.values())
    for key in actionmap:
        if actionmap[key] == maximum:
            return key

def minaction(Q):
    if Q == "A000" or Q == "B000":
        return 0
    actionmap = dict()
    for i in QValues.keys():
        if i[0] == Q:
            actionmap[i[1]] = QValues[(i)]
    minimum = min(actionmap.values())
    for key in actionmap:
        if actionmap[key] == minimum:
            return QValues[(Q,key)]

def maxaction(Q):
    if Q == "A000" or Q == "B000":
        return 0
    actionmap = dict()
    for i in QValues.keys():
        if i[0] == Q:
            actionmap[i[1]] = QValues[(i)]
    maximum = max(actionmap.values())
    for key in actionmap:
        if actionmap[key] == maximum:
            return QValues[(Q,key)]

def getallactions(Q):
    actionset = set()
    if int(Q[1]) > 0:
        pile = Q[1]
        action = "0"
        for i in range(int(pile)):
            takeaway = int(pile) - i
            action += str(takeaway)
            actionset.add(action)
            action  = "0"
    if int(Q[2]) > 0:
        pile = Q[2]
        action = "1"
        for i in range(int(pile)):
            takeaway = int(pile) - i
            action += str(takeaway)
            actionset.add(action)
            action  = "1"
    if int(Q[3]) > 0:
        pile = Q[3]
        action = "2"
        for i in range(int(pile)):
            takeaway = int(pile) - i
            action += str(takeaway)
            actionset.add(action)
            action  = "2"
    return actionset       


def nextstate(Q,action):
    nextstate = []
    if Q[0] == "A":
        nextstate.append("B")
    else:
        nextstate.append("A")
    nextstate.append(Q[1])
    nextstate.append(Q[2])
    nextstate.append(Q[3])
    actionpile = int(action[0])+1
    sub = int(action[1])
    takeaway = int(nextstate[actionpile])
    takeaway = takeaway - sub
    nextstate[actionpile] = str(takeaway)
    return ("".join(nextstate))
    

def InitpossibleState(Q):
    allactions = getallactions(Q)
    for action in allactions:
        QKey = (Q, action)
        if QKey not in QValues:
            QValues[QKey] = 0
            new_Q = nextstate(Q, action)
            InitpossibleState(new_Q)

def Q_alg(Q,numGames):
    A = 1
    G = 0.9
    currstate = Q
    i = 0
    while(i != numGames):
            if currstate == "B000" or currstate == "A000":
                currstate = Q
                i += 1
            r = 0
            allactions = getallactions(currstate)
            action = random.sample([*allactions], 1)
            action = action[0]
            newstate = nextstate(currstate, action)
            if newstate == "A000":
                r = 1000    
            elif newstate == "B000":
                r = -1000
            if currstate.startswith("A"):
                QValues[(currstate, action)] += A*(r + G*(minaction(newstate)) - QValues[(currstate, action)])
            else:
                QValues[(currstate, action)] += A*(r + G*(maxaction(newstate)) - QValues[(currstate, action)])
            currstate = newstate
        
    

def main():
    pile0 = input("Number in pile 0 ")
    pile1 = input("Number in pile 1 ")
    pile2 = input("Number in pile 2 ")
    numGames = int(input("Number of games to simulate? "))

    global QValues
    QValues = dict()         
    Q = "A"+str(pile0)+str(pile1)+str(pile2)
    InitpossibleState(Q)
    Q_alg(Q, numGames)
    print("Final Q Values: ")
    for val in QValues:
        print("Q["+val[0] +", " + val[1] +"] = "+ str(QValues[val]))


    endgame = False
    while endgame != True:
        board = Q
        firstmove = int(input("Who moves first, (1) User or (2) Computer? 2 "))
        if firstmove == 1:
            user = "(user)"
        else:
            user = "(computer)"
        gameover = False
        winner = "No one"
        while gameover != True:
            if board == "A000":
                winner = "A"
                gameover = True 
            elif board == "B000":
                winner = "B"
                gameover = True 
            else:
                currboard = "(" + board[1] + "," + board[2] + "," + board[3] + ")."
                if user == "(computer)":
                    print("Player "+ board[0] + user + "'s turn; board is " + currboard)
                    action = mingame(board)
                    if firstmove == 2:
                        action = maxgame(board)
                    board = nextstate(board, action)
                    print("Computer chooses pile " + action[0] + " and removes "+ action[1])
                    user = "(user)"
                elif user == "(user)":
                    print("Player "+ board[0] + user + "'s turn; board is " + currboard)
                    pile = input("What pile? ")
                    amt = input("How many? ")
                    action = pile+amt
                    board = nextstate(board, action)
                    user = "(computer)"
        print("Game over")
        print("Winner is "+winner + user)
        again = int(input("Play again? (1) Yes (2) No: "))
        if again == 2:
            endgame = True
        
        
            

        
    
            
        
    
        
    
    

    

    
        




main()
