class calc:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)
    def div(self,a,b):
        print(a/b)
obj=calc()
print(dir(calc()))
obj.add(8,3)
obj.sub(5,1)
obj.mul(4,10)
obj.div(8,2)

    