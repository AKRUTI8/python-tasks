class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i",self.img,"j")

    def __add__(self,num):
        newReal = self.real + num.real
        newImg = self.img + num.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num):
        newReal = self.real - num.real
        newImg = self.img - num.img
        return Complex(newReal,newImg)

num1 = Complex(1,3)
# num1.showNumber()

num2 = Complex(2,4)
# num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()

# polymorphism for operator overloading