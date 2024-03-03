l=[1,2,3,4,5,6,7,8,9]
def board():
    print("-----------------")
    print(l[0]," | ",l[1]," | ",l[2]," | ")
    print(l[3]," | ",l[4]," | ",l[5]," | ")
    print(l[6]," | ",l[7]," | ",l[8]," | ")
    print("-----------------")
def player1():
    t1=True
    while(t1==True):
        board()
        try:
            num1=int(input("Enter the position : "))
            if num1<=9:
                if(l[num1-1]=="X" or l[num1-1]=="O"):
                    print("position is already filled")
                    t1=True
                else:
                    l[num1-1]="X"
                    t1=False
            else:
                print("invaild position")
                t1=True
        except:
            print("invailid position")

def player2():
    t2=True
    while(t2==True):
        board()
        try:
            num2=int(input("Enter the position "))
            if num2<=9:
                if(l[num2-1]=='X' or l[num2-1]=="O"):
                    print("position is already filled")
                    t2=True
                else:
                    l[num2-1]="O"
                    t2=False
            else:
                print("invailid position")
                t2=True
        except:
            print("invailid position")
def check():
    if(l[0]=="X" and l[1]=="X" and l[2]=="X")or(l[3]=="X" and l[4]=="X" and l[5]=="X")or(l[6]=="X" and l[7]=="X" and l[8]=="X")or(l[0]=="X" and l[3]=="X" and l[6]=="X")or(l[1]=="X" and l[4]=="X" and l[7]=="X")or(l[2]=="X" and l[5]=="X" and l[8]=="X") or (l[0]=="X" and l[4]=="X" and l[8]=="X")or(l[2]=="X" and l[4]=="X" and l[6]=="X"):
        print("player one win's the game")
        return True
    elif(l[0]=="O" and l[1]=="O" and l[2]=="O")or(l[3]=="O" and l[4]=="O" and l[5]=="O")or(l[6]=="O" and l[7]=="O" and l[8]=="O")or(l[0]=="O" and l[3]=="O" and l[6]=="O")or(l[1]=="O" and l[4]=="O" and l[7]=="O")or(l[2]=="O" and l[5]=="O" and l[8]=="O") or (l[0]=="O" and l[4]=="O" and l[8]=="O")or(l[2]=="O" and l[4]=="O" and l[6]=="O"):
        print("congratulation for player 2")
        return True
print("--------------------WELCOME TO THE TIC-TAC-TOA GAME--------------------")
for i in range(1,10):
    if check()==True:
        board()
        print("game over")
        print("play again")
        break
    else:
        if i%2!=0:
            print("player 1")
            player1()
        else:
            print("player 2")
            player2()
        if i==9:
            print(board())
            print("game over")
    i=i+1
