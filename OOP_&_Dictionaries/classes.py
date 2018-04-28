class Square:
    NUMSIDES = 4;
    
    def __init__(self,color):
        self.numsides = 10;
        self.color = color;

sq = Square("red");
print(sq.color)