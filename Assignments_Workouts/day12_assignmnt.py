class Coordinate():

    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.repr()
        
    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y
        
    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
       
    def eq(self):
        if self.x==self.y:
            return True
        else:
            return False
    def repr(self):
        out=eval(repr(self.eq()))
        print(out)
        
obj = Coordinate(4,5)