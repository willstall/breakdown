class Brick():
    def __init__(self, x, y, wid, hgt, col):
        self.brickWidth = wid
        self.brickHeight = hgt;
        self.brickX = x + (self.brickWidth/2)
        self.brickY = y + (self.brickHeight/2);
        self.brickColor = col
        pass
        
    def display(self):
        rectMode(CENTER)
        fill(self.brickColor)
        rect(self.brickX, self.brickY, self.brickWidth, self.brickHeight)