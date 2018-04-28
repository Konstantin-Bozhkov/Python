class Square:
    NUMSIDES = 4;
    
    def __init__(self,width,heigth,color):
        self.color = color;
        self.width = width;
        self.heigth = heigth;
    
    def area(self):
        return self.heigth * self.width;
    
    def __str__(self):
        return "Square (%sx%s)" % (self.heigth, self.width);



class Car:
    MAKE = "LADA";
    MODEL = "1960";
    
    
    def __init__(self,color = "silver"):
        self.color = color;
    
    def drive(self,speed = 50):
        print( "Dragging my but in my %s at %s km/h" % (self,speed));
    
    def __str__(self):
        return "%s %s %s" % (self.color[0].upper() + self.color[1:], self.MAKE, self.MODEL);
    
    


class AudiTT(Car):
    MAKE = "Audi";
    MODEL = "TT";
    
    def __init__(self,color = "brown"):
        super(AudiTT,self).__init__(color);
        


sq = Square(3,5,"red");
car = Car("black")
audi = AudiTT("red")      

print(sq.area())
print(car.drive())
print(audi.drive(200))