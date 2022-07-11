from cs1_graphics import *

#Fish Class creates a large fish with an eye, gills, fins, and a tail
class Fish(Layer):

    #Fish Class comes with default body color of purple, 1 gill, eye size of 5 (scale 1), and tail at 0 degrees
    def __init__(self,bodyColor='purple',gillCount=1,eyeSize=1,angle=0):
        super().__init__()
        
        self._body = Polygon(Point(330,0),Point(300,30),Point(330,60),Point(30,60),Point(30,0))
        self._body.setFillColor(bodyColor)
        self._body.setDepth(50)
        self.add(self._body)

        self._eye = Circle(5,Point(285,15))
        self._eye.setFillColor('black')
        self._eye.setBorderWidth(2)
        self._eye.setBorderColor('white')
        self.add(self._eye)

        self._tail = Polygon(Point(30,30),Point(0,60),Point(0,0))
        self._tail.setFillColor('pink')
        self.add(self._tail)

        self._flipper = Polygon(Point(130,50),Point(130,10),Point(160,30))
        self._flipper.setFillColor('pink')
        self.add(self._flipper)

        self._fin = Polygon(Point(280,0),Point(260,-20),Point(120,0))
        self._fin.setFillColor('pink')
        self.add(self._fin)

        for i in range(gillCount):
            self._gill = Path(Point(210+10*i,10),Point(200+10*i,30),Point(210+10*i,50))
            self.add(self._gill)

    #setBodyColor function allows the user to change the body color of the fish
    def setBodyColor(self,bodyColor):
        self._body.setFillColor(bodyColor)

    #setGillCount function allows the user to add a set number of gills to the fish
    def setGillCount(self,gillCount):
        for i in range(gillCount):
            self._gill = Path(Point(210+10*i,10),Point(200+10*i,30),Point(210+10*i,50))
            self.add(self._gill)

    #setEyeSize function allows the user to increase or decrease the size of the eye of the fish
    def setEyeSize(self,eyeSize):
        self._eye.scale(eyeSize)

    #rotateTail function allows the user to change the direction of the tail of the fish
    def rotateTail(self,angle):
        self._tail.rotate(angle)

    if __name__ == '__main__':
        setBodyColor
        setGillCount
        setEyeSize
        rotateTail
