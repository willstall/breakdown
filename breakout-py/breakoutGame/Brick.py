class Brick():
    def __init__(self, x, y, wid, hgt, col):
        self.brickWidth = wid
        self.brickHeight = hgt;
        self.brickX = x + (self.brickWidth/2)
        self.brickY = y + (self.brickHeight/2);
        self.brickColor = col
        self.brickActive = True
        pass
        
    def display(self, b, bl):
        rectMode(CENTER)
        fill(self.brickColor)
        rect(self.brickX, self.brickY, self.brickWidth, self.brickHeight)
        self.checkCollision(b, bl)
        
    def checkCollision(self, ball, brickList):
        
        #hit bottom, top, left, right
        if ball.xPos - ball.size/2 > self.brickX - self.brickWidth/2 and \
        ball.xPos + ball.size/2 < self.brickX + self.brickWidth/2 and \
        ball.yPos - ball.size/2 < self.brickY + self.brickHeight/2 and \
        ball.yPos - ball.size/2 > self.brickY and self.brickActive:
           self.brickColor = color(0, 0, 0)
           ball.speedY *= -1
           self.brickActive = False
           println("bottom")
        elif ball.xPos - ball.size/2 > self.brickX - self.brickWidth/2 and \
        ball.xPos + ball.size/2 < self.brickX + self.brickWidth/2 and \
        ball.yPos + ball.size/2 > self.brickY - self.brickHeight/2 and \
        ball.yPos + ball.size/2 < self.brickY and self.brickActive:
           self.brickColor = color(0, 0, 0)
           ball.speedY *= -1
           self.brickActive = False
           println("top")
        elif ball.yPos - ball.size/2 > self.brickY - self.brickHeight/2 and \
        ball.yPos + ball.size/2 < self.brickY + self.brickHeight/2 and \
        ball.xPos + ball.size/2 > self.brickX - self.brickWidth/2 and \
        ball.xPos + ball.size/2 < self.brickX and self.brickActive:
            # self.brickColor = color(0, 0, 0)
            # ball.speedX *= -1
            # self.brickActive = False
            # println("left")
            pass