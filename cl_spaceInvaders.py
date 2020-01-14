#Cathy Liu
#Python 7
#4/27/2017
#cl_spaceInvaders.py

#Defender has three lives. When the defender loses a life, you lose 500 points. You gain 100 points for each invader you kill.
#When the defender is hit, the game pauses briefly to alert the user.
#Ask user to play again after game ends.
#Bottom row of invaders shoot.

import pygame,sys,random,time
from pygame.locals import *

#CONSTANTS

# window
WINDOWWIDTH = 1000
WINDOWHEIGHT = 1000

# movement
IDLE = 0
LEFT = 1
RIGHT = 3

ISPEED = 2 #invader speed
DSPEED = 8 #defender speed
PSPEED = 8 #projectile speed

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

ATTACKRATE = 20

#CLASSES
class Invader:
    def __init__(self,initX=0,initY=0,initWindow=0):
        self.x = initX
        self.y = initY
        self.color = WHITE
        self.dir = RIGHT
        self.rect = pygame.Rect(self.x,self.y,50,50)
        self.window = initWindow
        self.pList = [] #projectile list
    def draw(self):
        pygame.draw.rect(self.window,self.color,(self.rect))
    def move(self):
        if self.dir == LEFT:
            self.rect.left -= ISPEED
        elif self.dir == RIGHT:
            self.rect.right += ISPEED
    def attack(self): #create new projectile
        self.pList.append(Projectile(self.rect.centerx-5,self.rect.bottom,self.window))

class Defender:
    def __init__(self,initWindow=0):
        self.color = WHITE
        self.dir = IDLE
        self.rect = pygame.Rect(0,900,70,70) 
        self.window = initWindow
        self.pList = [] #projectile list
    def draw(self):
        pygame.draw.rect(self.window,self.color,(self.rect))
    def move(self):
        if self.dir == LEFT:
            self.rect.left -= DSPEED
        elif self.dir == RIGHT:
            self.rect.right += DSPEED
        elif self.dir == IDLE:
            self.rect.left += 0
    def attack(self): #create new projectile
         self.pList.append(Projectile(self.rect.centerx-5,self.rect.top,self.window))

class Wall:
    def __init__(self,initX=0,initWindow=0):
        self.x = initX
        self.color = GREEN
        self.rect = pygame.Rect(initX,800,100,30)
        self.window = initWindow
    def draw(self):
        pygame.draw.rect(self.window,self.color,self.rect)
    def reduce(self):
        self.rect.inflate_ip(-2) #probably put this in GAME STATE, actually

class Projectile: 
    def __init__(self,initX=0,initY=0,initWindow=0):
        self.x = initX
        self.y = initY
        self.color = RED
        self.rect = pygame.Rect(self.x,self.y,10,10)
        self.window = initWindow
    def draw(self):
        pygame.draw.rect(self.window,self.color,self.rect)
    def moveUp(self):
        self.rect.top -= PSPEED
    def moveDown(self):
        self.rect.bottom += PSPEED
        
#USER-DEFINED FUNCTIONS
        
def main():
    pygame.init()
    
    while True: #1st loop: reset variables
        
        #VARIABLE CREATION
        mainClock = pygame.time.Clock() 
        windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32) 

        d = Defender(windowSurface) #create defender object
        
        invaders = [[],[],[]] #create empty invader list
        for x in range(3): #3 rows of 5 invaders each
            for y in range(5):
                invaders[x].append(Invader(50+100*y,50+100*x,windowSurface)) #append invaders to list

        walls = [] #create empty walls list
        for x in range(5): #5 walls
            walls.append(Wall(50+200*x,windowSurface))
            
        # defender movement variable setup
        dLeft = False
        dRight = False
        dAttack = False

        changeDir = False

        # invader attacking variable setup
        timer = 0
        attackIndex = 0
        randomAttack = 0

        #font object setup
        fontObj = pygame.font.Font('freesansbold.ttf',20)

        score = 0
        lives = 3

        #win/loss variable setup
        endState = ''
        gameOver = False
        loseLife = False
        playAgain = False
        
        while True: #2nd loop: run animation
            
            #EVENT HANDLING
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                # user controlled defender movement
                if event.type == KEYDOWN:
                    if event.key == K_LEFT or event.key == K_a: 
                        dLeft = True #defender moves left
                    if event.key == K_RIGHT or event.key == K_d:
                        dRight = True #defender moves right
                if event.type == KEYUP:
                    if event.key == K_ESCAPE: 
                        pygame.quit()
                        sys.exit()
                    if event.key == K_LEFT or event.key == K_a:
                        dLeft = False
                    if event.key == K_RIGHT or event.key == K_d:
                        dRight = False
                    if event.key == K_SPACE: #defender shoots projectile on spacebar release
                        dAttack = True 
                if event.type == MOUSEBUTTONUP:
                    if gameOver: #if game is over, clicking the mouse will allow user to replay
                        gameOver = False
                        playAgain = True
                        
            #GAME STATE
            if not gameOver: #stop if game is over
                
                # invader movement
                for invaderList in invaders: 
                    for invader in invaderList:
                        if invader.rect.right >= WINDOWWIDTH or invader.rect.left <= 0:
                            changeDir = True #change direction if invader hits left or right border of window

                if changeDir:
                    for invaderList in invaders:
                        for invader in invaderList:
                            if invader.dir == LEFT:
                                invader.dir = RIGHT
                                invader.rect.bottom += 25 #invaders descend upon changing direction
                            elif invader.dir == RIGHT:
                                invader.dir = LEFT
                                invader.rect.bottom += 25
                            if invader.rect.bottom >= 800: #if invaders descend past the walls
                                gameOver = True
                                endState = 'YOU LOSE'
                                
                    changeDir = False
                    
                for invaderList in invaders:
                    for invader in invaderList:
                        invader.move()

                # defender movement
                if dLeft:
                    if d.rect.left <= 0:
                        d.dir = IDLE
                    else:
                        d.dir = LEFT
                    d.move()
                elif dRight:
                    if d.rect.right >= WINDOWWIDTH:
                        d.dir = IDLE
                    else:
                        d.dir = RIGHT
                    d.move()
                    
                # defender attacking
                if dAttack:
                    d.attack() #create projectile
                    dAttack = False
                    
                # move defender projectile
                for projectile in d.pList[:]:
                    projectile.moveUp()
                    if projectile.rect.bottom <= 0: #remove projectile when it hits the bottom of the screen
                        d.pList.remove(projectile)
                    for wall in walls[:]:
                        if projectile.rect.colliderect(wall.rect): #projectile collides with wall
                            wall.rect.inflate_ip(0,-10) #wall height reduced by 2
                            d.pList.remove(projectile) #remove projectile from list on collision with wall
                            if wall.rect.height <= 0: #if wall height is zero, remove wall from list
                                walls.remove(wall)
                    for invaderList in invaders[:]:
                        for invader in invaderList:
                            if projectile.rect.colliderect(invader.rect):
                                invaderList.remove(invader) #remove invader from list on collision with projectile
                                d.pList.remove(projectile) #remove projectile from list on collision with invader
                                score += 100 #earn 100 points

                # invader attacking
                if len(invaders) > 0:
                    if len(invaders[-1]) == 0: #remove empty invader row list from invaders list of lists 
                        invaders.remove(invaders[-1])
                if len(invaders) == 0:
                    gameOver = True
                    endState = 'YOU WIN'
                    
                timer += 1
                randomAttack = random.randint(1,20)
                if timer >= ATTACKRATE:
                    if randomAttack == 1:
                        attackIndex = random.randint(0,len(invaders[-1])-1)
                        timer = 0
                        invaders[-1][attackIndex].attack() #randomly selected invader from bottom row attacks
                for invaderList in invaders:
                    for invader in invaderList:
                        for projectile in invader.pList[:]:
                            projectile.moveDown()
                            if projectile.rect.bottom <= 0: #remove projectile when it hits the bottom of the screen
                                invader.pList.remove(projectile)
                            if projectile.rect.colliderect(d.rect): #projectile collides with defender
                                lives -= 1 #lose a life
                                score -= 500 #lose 500 points
                                time.sleep(1) #pause for 1 seconds
                                invader.pList.remove(projectile)
                            for wall in walls[:]:
                                if projectile.rect.colliderect(wall.rect): #projectile collides with wall
                                    wall.rect.inflate_ip(0,-10) #wall height reduced by 2
                                    invader.pList.remove(projectile) #remove projectile from list on collision with wall
                                    if wall.rect.height <= 0: #if wall height is zero, remove wall from list
                                        walls.remove(wall)
                                        
                if lives == 0: #if user runs out of lives, the game ends with a loss
                    gameOver = True
                    endState = 'YOU LOSE'
                                                        
            #DRAW SCREEN
            windowSurface.fill(BLACK)
            
            d.draw() #draw defender
            
            for projectile in d.pList: #draw defender projectiles
                projectile.draw()
            
            for invaderList in invaders: #draw invaders
                for invader in invaderList:
                    invader.draw()
                    
            for invaderList in invaders: #draw invader projectiles
                for invader in invaderList:
                    for projectile in invader.pList:
                        projectile.draw()

            for wall in walls: #draw walls
                wall.draw()

            # render text
            scoreSurfaceObj = fontObj.render('SCORE: ' + str(score),True,WHITE) #score
            scoreRectObj = scoreSurfaceObj.get_rect()
            scoreRectObj.center = (875,25)
            windowSurface.blit(scoreSurfaceObj,scoreRectObj)

            livesSurfaceObj = fontObj.render('LIVES: ' + str(lives),True,WHITE) #lives
            livesRectObj = livesSurfaceObj.get_rect()
            livesRectObj.center = (750,25)
            windowSurface.blit(livesSurfaceObj,livesRectObj)
            
            endSurfaceObj = fontObj.render('GAME OVER: ' + endState,True,WHITE) #GAME OVER screen
            endRectObj = endSurfaceObj.get_rect()
            endRectObj.center = (500,500)

            playAgainSurfaceObj = fontObj.render('CLICK MOUSE TO PLAY AGAIN',True,WHITE)
            playAgainRectObj = playAgainSurfaceObj.get_rect()
            playAgainRectObj.center = (500,540)

            if gameOver:
                windowSurface.blit(endSurfaceObj,endRectObj)
                windowSurface.blit(playAgainSurfaceObj,playAgainRectObj)

            pygame.display.update()
            mainClock.tick(100)
            
            if playAgain: #if user wants to play again, break out of 2nd loop into 1st loop to reset variables
                break

main()
