class Mathfun():
    def __init__(self):
        print("Inside init function ")
    # class functions
    def area_circle(self,r): 
        try:
            out = 3.14 *r*r
            print("inside __area_circle", out)
        except Exception as e:
            print(e)
    # class functions 
    def area_square(self, l, b,h):
        """ area of square function with 3 arguments"""
        try:
            out = l*b*h 
            self.__area_circle(7)
            print("inside area_square",out)
        except Exception as e:
            print(e)
    # static function 
    def add(a,b):
        print(a,b)
obj = Mathfun()