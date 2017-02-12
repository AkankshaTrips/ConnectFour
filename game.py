from squares import*

def drawGrid(win,x1,y1,x2,y2):
    
    grid = []
    for i in range(7):
        grid.append([])
        
        for j in range(8):
            grid[i].append(0)
            
    for i in range (0,7):
        for j in range (0,8):
            
            square = make_square(x1+50*j, y1-50*i, x2+50*j, y2-50*i)
            grid[i][j] = square
            shape = Rectangle(square.a, square.b)
            
            if (i+j)% 2 == 0:
                shape.setFill('red')
            else:
                shape.setFill('brown')
            shape.draw(win)
    return grid     

def play(win,grid):

    player = 1
    moves = 0
    label1 = displayNextMove(player,win)
    label2 = displayNoOfMoves(moves,win)
    winner = 0
    
    while (winner == 0):

        label1.undraw()
        label2.undraw()
        
        label1 = displayNextMove(player,win)
        label2 = displayNoOfMoves(moves,win)
        
        mouse = win.getMouse()
        for i in grid:
            for j in i:
                
                if condition(j,mouse):
                    moves = moves + 1
                    if player == 1:
                        drawCross(j,win)
                        player = 2
                        j.checker = 1

                    elif player == 2:
                        drawCircle(j,win)
                        player = 1
                        j.checker = 2

                    winner = checkAllConditions(grid,win)
    return winner
                        

                                                                                                
def condition(square, mouse):
    if square.checker == 0:
        if mouse.x >= square.x1 and mouse.x <= square.x2 and mouse.y <= square.y1 and mouse.y >= square.y2:
            return True
    return False

def drawCross(square,win):
    line1 = Line(square.cross1,square.cross2)
    line2 = Line(square.cross3,square.cross4)
    
    line1.setWidth(10)
    line2.setWidth(10)
    
    line1.draw(win)
    line2.draw(win)

    return

def drawCircle(square,win):
    cir = Circle(square.mid,square.circleRadius)
    cir.setWidth(10)
    cir.draw(win)

    return
    
            
def displayNextMove(player,win):
    string1 = str("Next move: Player %0.0f" %player)
    
    label1 = Text(Point(150, 450), string1)
    label1.setSize(15)
    label1.draw(win)
        
    return label1

def displayNoOfMoves(moves,win):
    string2 = str("No. of moves: %0.0f" %moves)
        
    label2 =  Text(Point (350,450),string2)
    label2.setSize(18)
    label2.draw(win)

    return label2

def checkConnection(four,win):
    if(four[0].checker == four[1].checker and four[0].checker == four[2].checker and four[0].checker == four[3].checker and four[0].checker !=0):
        line = Line(four[0].mid,four[3].mid)
        line.setWidth(four[0].checkerWidth-5)
        line.setFill("yellow")
        line.draw(win)
        return 1
    return 0
    
       
def checkAllConditions(grid,win):
    winner = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if j+3 < len(grid[i]):
                
                four = []
                four.append(grid[i][j])
                four.append(grid[i][j+1])
                four.append(grid[i][j+2])
                four.append(grid[i][j+3])
                if(checkConnection(four,win)):
                    winner = four[0].checker
                    break

            if i+3 < len(grid):
                
                    four = []
                    four.append(grid[i][j])
                    four.append(grid[i+1][j])
                    four.append(grid[i+2][j])
                    four.append(grid[i+3][j])
                    if(checkConnection(four,win)):
                        winner = four[0].checker
                        break

            if i+3 < len(grid) and j+3 < len(grid[i]):
                
                four = []
                four.append(grid[i][j])
                four.append(grid[i+1][j+1])
                four.append(grid[i+2][j+2])
                four.append(grid[i+3][j+3])
                if(checkConnection(four,win)):
                    winner = four[0].checker
                    break
                
                        
            if j-3 >= 0 and i+3 < len(grid):
                
                four = []
                four.append(grid[i][j])
                four.append(grid[i+1][j-1])
                four.append(grid[i+2][j-2])
                four.append(grid[i+3][j-3])
                if(checkConnection(four,win)):
                    winner = four[0].checker
                    break
                

    return winner
        
def main():
    win = GraphWin('Tic-Tac-Toe',500,600)
        
    yMax = 500
    xMax = 500
    win.setCoords(0,0,xMax,yMax)

    grid = drawGrid(win,50,400,100,350)

    winner = play(win,grid)
    print("The winner is player",winner,"!")
    
    time.sleep(3)
    win.close()

main()
