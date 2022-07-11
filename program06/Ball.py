class Ball:
    def __init__(self,_posX,_posY,_velX,_velY):
        self._posX = x
        self._posY = y
        self._velX = vx
        self._velY = vy
        
    def Ball(x,y,vx,vy):
        x = getPositionX(self)
        y = getPositionY(self)
        vx = self._velX
        vy = self._velY
        
    def getPositionX(self):
        return self._posX

    def getPositionY(self):
        return self._posY

    def getVelocityX(self):
        return self._velX

    def getVelocityY(self):
        return self._velY

    def advance(self,world):
        g = world.getGravity()
        self._posX += self._velX 
        self._posY += self._velY
        self._velY += g
        
