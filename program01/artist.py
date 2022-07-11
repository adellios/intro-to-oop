#from cs1graphics import

Canvas()
paper=Canvas(500,500,'blue','Bigger Fish')
sky=Rectangle(500,150,Point(250,75))
sky.setFillColor('lightSkyBlue')
paper.add(sky)

island=Layer()
sand=Polygon(Point(100,150),Point(150,120),Point(200,120),Point(250,150))
sand.setFillColor('yellow')
island.add(sand)
tree=Polygon(Point(170,120),Point(180,120),Point(180,50),Point(170,50))
tree.setFillColor('brown')
island.add(tree)
leaf=Polygon(Point(125,105),Point(225,105),Point(175,30))
leaf.setFillColor('darkGreen')
leaf.setBorderWidth(5)
leaf.setBorderColor('green')
island.add(leaf)
leaf2=Polygon(Point(125,85),Point(225,85),Point(175,10))
leaf2.setFillColor('darkGreen')
leaf2.setBorderWidth(5)
leaf2.setBorderColor('green')
island.add(leaf2)
rock=Circle(5,Point(155,137))
island.add(rock)
rock2=Circle(5,Point(164,132))
island.add(rock2)
island.moveTo(0,0)
island.setDepth(0)
paper.add(island)

fish=Layer()
head=Circle(25,Point(-50,250))
head.setFillColor('orange')
fish.add(head)
tail=Polygon(Point(-75,250),Point(-100,225),Point(-100,275))
tail.setFillColor('orange')
fish.add(tail)
eye=Circle(5,Point(-45,245))
eye.setFillColor('white')
eye.setBorderWidth(2)
eye.setBorderColor('black')
fish.add(eye)
fin=Polygon(Point(-60,250),Point(-80,230),Point(-80,270))
fin.setFillColor('orange')
fin.rotate(-10)
fish.add(fin)

fish.setDepth(0)
paper.add(fish)

bird=Layer()
birdHead=Circle(15,Point(-50,-50))
birdHead.setFillColor('white')
bird.add(birdHead)
birdBeak=Polygon(Point(-57,-48),Point(-50,-40),Point(-43,-48))
birdBeak.setFillColor('yellow')
bird.add(birdBeak)
birdBody=Polygon(Point(-50,-35),Point(-70,-5),Point(-30,-5))
birdBody.setFillColor('white')
bird.add(birdBody)
birdEye1=Circle(2,Point(-55,-55))
birdEye1.setFillColor('black')
bird.add(birdEye1)
birdEye2=Circle(2,Point(-45,-55))
birdEye2.setFillColor('black')
bird.add(birdEye2)
birdWing1=Polygon(Point(-55,-27),Point(-50,-18),Point(-82,-30))
birdWing1.setFillColor('white')
bird.add(birdWing1)
birdWing2=Polygon(Point(-45,-27),Point(-40,-20),Point(-18,-30))
birdWing2.setFillColor('white')
bird.add(birdWing2)
birdFoot1=Polygon(Point(-60,5),Point(-50,5),Point(-55,-5))
birdFoot1.setFillColor('yellow')
bird.add(birdFoot1)
birdFoot2=Polygon(Point(-40,5),Point(-50,5),Point(-45,-5))
birdFoot2.setFillColor('yellow')
bird.add(birdFoot2)

bird.setDepth(-10)
paper.add(bird)

bird2=Path(Point(400,50),Point(430,60),Point(460,50))
paper.add(bird2)
bird3=Path(Point(370,80),Point(400,90),Point(430,80))
paper.add(bird3)

bigFish=Layer()
bigBody=Polygon(Point(-50,220),Point(-80,250),Point(-50,280),Point(-350,280),Point(-350,220))
bigBody.setFillColor('purple')
bigFish.add(bigBody)
bigEye=Circle(5,Point(-95,235))
bigEye.setFillColor('black')
bigEye.setBorderWidth(2)
bigEye.setBorderColor('white')
bigFish.add(bigEye)
bigTail=Polygon(Point(-350,250),Point(-380,280),Point(-380,220))
bigTail.setFillColor('pink')
bigFish.add(bigTail)
bigFin=Polygon(Point(-250,270),Point(-250,230),Point(-220,250))
bigFin.setFillColor('pink')
bigFish.add(bigFin)
back=Polygon(Point(-100,220),Point(-120,200),Point(-260,220))
back.setFillColor('pink')
bigFish.add(back)

bigFish.setDepth(-20)
paper.add(bigFish)

text=Text('Look Out!',10,Point(120,50))
text2=Text('?',30,Point(200,205))
text2.setDepth(-20)

from time import sleep
timeDelay=0.3
fish.move(50,0)
sleep(timeDelay)
fish.move(50,0)
sleep(timeDelay)
fish.move(50,0)
sleep(timeDelay)
fish.move(50,0)
sleep(timeDelay)
fish.move(50,0)

sleep(timeDelay)
bird.move(43,23)
sleep(timeDelay)
bird.move(43,23)
sleep(timeDelay)
bird.move(43,23)
sleep(timeDelay)
bird.move(43,23)
sleep(timeDelay)
bird.move(43,23)
sleep(timeDelay)
paper.add(text)
sleep(timeDelay)
paper.add(text2)
sleep(timeDelay)
paper.remove(text2)
paper.remove(text)

sleep(timeDelay)
bird.move(43,-24)
sleep(timeDelay)
bird.move(43,-24)
sleep(timeDelay)
bird.move(43,-24)
sleep(timeDelay)
bird.move(43,-24)
sleep(timeDelay)
bird.move(43,-24)

sleep(timeDelay)
bigFish.move(50,0)
sleep(timeDelay)
bigFish.move(50,0)
sleep(timeDelay)
bigFish.move(50,0)
sleep(timeDelay)
bigFish.move(50,0)
sleep(timeDelay)
bigFish.move(50,0)
sleep(timeDelay)
bigFish.move(50,0)
sleep(timeDelay)
bigFish.move(50,0)
paper.remove(fish)
sleep(timeDelay)
bigFish.move(50,30)
sleep(timeDelay)
bigFish.move(50,30)
sleep(timeDelay)
bigFish.move(50,30)
sleep(timeDelay)
bigFish.move(50,30)
bigFish.rotate(12)
sleep(timeDelay)
bigFish.move(50,30)
sleep(timeDelay)
bigFish.move(50,30)
sleep(timeDelay)
bigFish.move(50,30)
sleep(timeDelay)
bigFish.move(50,30)
sleep(timeDelay)
bigFish.move(50,30)
sleep(timeDelay)
bigFish.move(50,30)
sleep(timeDelay)
bigFish.move(50,30)
sleep(timeDelay)
bigFish.move(50,30)
