from Paddle import Paddle
from Brick import Brick
paddle = Paddle(360)

brickList = []
rowColorList = [color(255, 255, 0), 
                color(0, 255, 0), 
                color(255, 153, 0),
                color(255, 0, 0)]

resX = 640
resY = 360
spaceBetweenBricks = 0
spaceFromTop = 0
brickCount = 8
rowCount = 8
brickWidth = (resX - (brickCount - 2) * spaceBetweenBricks) / brickCount
brickHeight = 15

# bricksPerRow = 5

def setup():
    size(resX, resY)
    noStroke()
    spawnBricks()

def draw():
    background(0);
    paddle.display()
    drawBricks()
    
def spawnBricks():
    println("Creating bricks")
    rowColCount = 3
    for y in range(0, rowCount):
        for x in range(0, brickCount):
            brickX = (brickWidth + spaceBetweenBricks) * x
            brickY = spaceFromTop + (brickHeight - 0.5) * y 
            brick = Brick(brickX, brickY, brickWidth, 15, rowColorList[rowColCount])
            brickList.append(brick)
            
        if(y % 2 == 1):
            rowColCount -= 1
            
    println(len(brickList))
        
def drawBricks():
    for x in range(0, len(brickList)):
        brickList[x].display()
    
def keyPressed():
    if key == 'a':
        paddle.left = 1
    if key == 'd':
        paddle.right = 1

def keyReleased():
    if key == 'a':
        paddle.left = 0
    if key == 'd':
        paddle.right = 0