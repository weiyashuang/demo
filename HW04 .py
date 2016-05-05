class Shape():
    def __init__(self,a):
        self.a = a
        

class Ellipse(Shape):
    def __init__(self,a,b):
        super().__init__(self)
        self.a = a
        self.b = b
    def area(self):
        return   self.a*self.b*3.14
        

class Square(Shape):
    def __init__(self,a):
        super().__init__(a)
        
    def area(self):
        return   self.a*self.a 

  
class Rectangle(Shape):
    def __init__(self,a,b):
        super().__init__(a)
        self.b = b
    def area(self):
        return   self.a*self.b

    
class Circle(Shape):
    
    def __init__(self,a):
        super().__init__(a)
        
    def area(self):
        return   self.a*self.a*3.14 



def compute_area(shapes):
    s = 0
    for i in range(0,7):
        s += shapes[i].area()
    
    return s
     

def main():
    
    shapes = [Ellipse(10,20),Square(15),Circle(5),Rectangle(20,15),Circle(5),Square(15),Ellipse(10,20)]

    total_area = compute_area(shapes)

    print(total_area)


main()

    


