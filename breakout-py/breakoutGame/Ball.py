class Ball():
    
    def __init__(self, xPos, yPos, sz, rX, rY):
        self.xPos = xPos
        self.yPos = yPos
        self.size = sz
        self.speedX = 4
        self.speedY = 4
        self.resX = rX
        self.resY = rY
    
    def clamp(self, x, minValue, maxValue):
        if x < minValue:
            return minValue
        elif x > maxValue:
            return maxValue
        else:
            return x;
    
    def checkWallCollision(self):
        if self.xPos < self.size/2:
           self.speedX *= -1
        elif self.xPos > (self.resX - self.size/2):
            self.speedX *= -1
        if self.yPos < self.size/2:
            self.speedY *= -1
    
    def resetPosition(self, x, y):
        println("resetting ball")
        self.xPos = x
        self.yPos = y
        self.speedX = 4
        self.speedY = 4
        
    
    def display(self):
        self.checkWallCollision()
        rectMode(CENTER)
        self.xPos += self.speedX
        self.yPos -= self.speedY
        fill(255)
        ellipse(self.xPos, self.yPos,
                 self.size, self.size)