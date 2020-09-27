class Geometry(object):
    count = 0

    def __init__(self):
        self.area = 0
        Geometry.count += 1

    def circleArea(self,radious):
        self.area = 3.1415 * radious * radious

    def triangleArea(self,b,h):
        self.area =  .5 * b * h

    def squareArea(self,lenth):
        self.area = lenth * lenth

    def printDetails(self):
        print('The Area is: ',self.area)


print('No of Geometry chapters', Geometry.count)
circle = Geometry()
triangle = Geometry()
square = Geometry()
print('No of Geometry chapters', Geometry.count)
circle.circleArea(5)
print('***********')
circle.printDetails()
triangle.triangleArea(3,6)
print('***********')
triangle.printDetails()
square.squareArea(4)
print('***********')
square.printDetails()
