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
        # if ball.xPos > self.brickX - self.brickWidth/2 and \
        # ball.xPos < self.brickX + self.brickWidth/2 and \
        # ball.yPos < self.brickY + self.brickHeight/2 and \
        # ball.yPos > self.brickY - self.brickHeight/2:
        #     self.brickColor = color(0, 0, 0)
            
        #hit bottom
        if ball.xPos - ball.size/2 > self.brickX - self.brickWidth/2 and \
        ball.xPos + ball.size/2 < self.brickX + self.brickWidth/2 and \
        ball.yPos - ball.size/2 < self.brickY + self.brickHeight/2:
            self.brickColor = color(0, 0, 0)
            ball.speedY *= -1
            brickActive = False