from cs1 graphics import*

numColumns=15
numLevels=13
unitSize=50
Width=numColumns*unitSize
Length=numLevels*unitSize
width=unitSize
centerX=Width-unitSize
centerY=unitSize


paper=Canvas(Width,Length,'burlywood4','backgammon')
list1=[4,11]
for w in list1:
    background=Rectangle((numColumns-9)*unitSize,(numLevels-2)*unitSize,Point((Width)*(w/15),(Length)/2))
    background.setFillColor('navajowhite')
    paper.add(background)

list2=[2,4,6,9,11,13]
list3=[1,3,5,8,10,12]

topPoints=Layer()
for w in range(numColumns):
    triangle = Polygon(Point(unitSize*w,unitSize),Point(unitSize*(w+1),unitSize),Point(unitSize*(w+1/2),(6/numLevels*Length)))
    if w in list2:
        triangle.setFillColor('darkorange3')
        topPoints.add(triangle)
    if w in list3:
        triangle.setFillColor('tan')
        topPoints.add(triangle)
paper.add(topPoints)

bottomPoints=topPoints.clone()
bottomPoints.move(Width,Length)
bottomPoints.rotate(180)
paper.add(bottomPoints)

divider=Path(Point(Width/2,0),Point(Width/2,Length))
divider.setBorderWidth(3)
paper.add(divider)

for num,w,whiteOnTop in [(2,unitSize,True), (5,6*unitSize,False), (3,9*unitSize,False), (5, 13*unitSize,True)]:
    for num in range(num):
        topChecker = Circle(unitSize/2,Point(w+unitSize/2,(3/2+num)*unitSize))
        bottomChecker = Circle(unitSize/2,Point(w+unitSize/2,(23/2-num)*unitSize))
        if whiteOnTop == True:
            topChecker.setFillColor('white')
            paper.add(topChecker)
            bottomChecker.setFillColor('black')
            paper.add(bottomChecker)
        else:
            topChecker.setFillColor('black')
            paper.add(topChecker)
            bottomChecker.setFillColor('white')
            paper.add(bottomChecker)

list4 = [1,2,3,4,5,6,8,9,10,11,12,13]
for w in list4:
    if w >= 8:
        topNumber = Text(str(26-w),15)
        bottomNumber = Text(str(w-1),15)
    else:
        topNumber = Text(str(25-w),15)
        bottomNumber = Text(str(w),15)
        
    topNumber.move((w+1/2)*unitSize,unitSize/2)
    paper.add(topNumber)
    bottomNumber.move((w+1/2)*unitSize,unitSize*(25/2))
    paper.add(bottomNumber)
