class Paddle():
    
    def __init__(self, yPosition, sz):
        self.xPos = 320
        self.yPos = yPosition - 25
        self.left = 0
        self.right = 0
        self.speed = 10.0
        self.size = sz
        self.ySize = 10
    
    def clamp(self, x, minValue, maxValue):
        if x < minValue:
            return minValue
        elif x > maxValue:
            return maxValue
        else:
            return x;
    
    def display(self):
        rectMode(CENTER)
        self.xPos += (self.right - self.left) * self.speed
        self.xPos = self.clamp(self.xPos, self.size/2, width - (self.size/2))
        fill(255)
        rect(self.xPos, self.yPos, self.size, self.ySize)