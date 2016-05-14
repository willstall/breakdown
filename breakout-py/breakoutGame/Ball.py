class Ball():
    
    def __init__(self, xPos, yPos, sz):
        self.xPos = xPos
        self.yPos = yPos
        self.size = sz
    
    def clamp(self, x, minValue, maxValue):
        if x < minValue:
            return minValue
        elif x > maxValue:
            return maxValue
        else:
            return x;
    
    def display(self):
        rectMode(CENTER)
        fill(255)
        ellipse(self.xPos, self.yPos, self.size, self.size)