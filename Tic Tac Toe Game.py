m = [[" ","|"," ","|"," "],[" ","|"," ","|"," "],[" ","|"," ","|"," "]]
p1,p2 = 0,0
o = 1
def tic(x,y,val):
    if y%2==0 and m[x][y]==" ":
        m[x][y]=val
def check(x,y,pl1,pl2):
    if (x==0 and y==0) or (x==1 and y==2) or (x==2 and y==4):
        if m[0][0]==m[1][2]==m[2][4]==pl1[0] or m[0][0]==m[1][2]==m[2][4]==pl2[0]:
            return True
    elif (x==0 and y==4) or (x==1 and y==2) or (x==2 and y==0):
        if m[0][0]==m[1][2]==m[2][0]==pl1[0] or m[0][0]==m[1][2]==m[2][0]==pl2[0]:
            return True
    if (m[x][0]==m[x][2] and m[x][0]==m[x][4]) or (m[0][y]==m[1][y] and m[2][y]==m[0][y]):
        return True
def game():
    if m[0].count(" ")==0 and m[1].count(" ")==0 and m[2].count(" ")==0:
        return True
def player1():
    return True
def player2():
    return True
pl1 = {}
pl2 = {}
while True:
    if game():
        for i in m:
            print(*i)
            print("-----------")
        print("Game Over")
        break
    for i in m:
        print(*i)
        print("-----------")
    if o%2!=0:
        print("Player 1 : ")
        if p1==0:
            val = input("Choose X or O : ")
            pl1[0] = val
        else:
            if player1():
                val = pl1[0]
        x = int(input("Enter Row : "))
        y = int(input("Enter Column : "))
        if pl1[0]=="X":
            pl2[0]="O"
        else:
            pl2[0]="X"
        tic(x,y,val)
        if check(x,y,pl1,pl2)==True:
            for i in m:
                print(*i)
                print("-----------")
            print("Player1 has won")
            break
        p1+=1
    else:
        print("Player 2 : ")
        if pl1[0]=="X":
            pl2[0] = "O"
        else:
            pl2[0] = "X"
        if player2():
            val = pl2[0]
        x = int(input("Enter Row : "))
        y = int(input("Enter Column : "))
        tic(x,y,val)
        if check(x,y,pl1,pl2)==True:
            for i in m:
                print(*i)
                print("-----------")
            print("Player2 has won")
            break
        p2+=1
    o+=1
    
        
