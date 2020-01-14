#Cathy Liu
#Python 7
#5/16/2017

import pygame,sys,random,time,os
from pygame.locals import *

pygame.init()
pygame.mixer.init()

#CONSTANTS

CLOCK = pygame.time.Clock()

# colors
B = (0,0,0)
BG = B #background
W = (255,255,255)
R = (255,0,0)

# window
SCREENWIDTH = 800
SCREENHEIGHT = 800
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT),0,32)

# textbox
TBOXWIDTH = 780
TBOXHEIGHT = 200
TBOXBORDER = (SCREENWIDTH-TBOXWIDTH)/2

# font
FONTPATH = os.path.join(os.getcwd(),'fonts','GeosansLight.ttf')
FONT = pygame.font.Font(FONTPATH,24)
TITLE = pygame.font.Font(FONTPATH,60)

# music
TITLEPATH = os.path.join(os.getcwd(),'music','Arkadiusz Reikowski - Main Theme ft. Airis Quartet.mp3')
MUSICPATH = os.path.join(os.getcwd(),'music','Woods Darker Than Night.mp3')

#CLASSES

class Trapezoid:
    def __init__(self,initX1=0,initY1=0,initWidth1=0,initX2=0,initY2=0,initWidth2=0,initColor=W):
        self.window = SCREEN

        self.x1 = initX1
        self.y1 = initY1
        self.width1 = initWidth1 
        
        self.x2 = initX2
        self.y2 = initY2
        self.width2 = initWidth2 

        self.height = self.y2-self.y1
        self.color = initColor
        
        self.pList = [(self.x1,self.y1),(self.x1+self.width1,self.y1),(self.x2+self.width2,self.y2),(self.x2,self.y2)]

        self.rect = pygame.Rect(self.x1,self.y1,self.width1,self.height)
        
    def draw(self):
        pygame.draw.polygon(self.window,self.color,(self.pList[0],self.pList[1],self.pList[2],self.pList[3]))
        
class Textbox:
    def __init__(self,initX=TBOXBORDER,initY=SCREENHEIGHT-TBOXHEIGHT-TBOXBORDER,initWidth=TBOXWIDTH,initHeight=TBOXHEIGHT):
        self.window = SCREEN

        # border box attributes
        self.xB = initX
        self.yB = initY
        self.widthB = initWidth
        self.heightB = initHeight
        self.colorB = W
        self.rectB = pygame.Rect(self.xB,self.yB,self.widthB,self.heightB)

        # inner box attributes
        self.x = self.xB+TBOXBORDER
        self.y = self.yB+TBOXBORDER
        self.width = self.widthB-2*TBOXBORDER
        self.height = self.heightB-2*TBOXBORDER
        self.color = B
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        
    def drawBox(self):
        pygame.draw.rect(self.window,self.colorB,(self.rectB))
        pygame.draw.rect(self.window,self.color,(self.rect))

    def drawText(self,text,color=W):
        surface = FONT.render(text,True,color) 
        rect = surface.get_rect()
        rect.center = self.rect.center
        SCREEN.blit(surface,rect)

#USER DEFINED FUNCTIONS

def menu():
    
    # play music
    pygame.mixer.music.load(TITLEPATH)
    pygame.mixer.music.play(loops=-1)
    
    #VARIABLE CREATION
    
    title = {'text':'THE FOREST','color':W,'pos':(SCREENWIDTH/2,SCREENHEIGHT/2)}

    titleSurface = TITLE.render(title['text'],True,title['color'])
    titleRect = titleSurface.get_rect()
    titleRect.center = title['pos']

    # options
    playSurface = FONT.render('play',True,W)
    playRect = playSurface.get_rect()
    playRect.center = (SCREENWIDTH/2-50,SCREENHEIGHT/2+75)

    infoSurface = FONT.render('info',True,W)
    infoRect = infoSurface.get_rect()
    infoRect.center = (SCREENWIDTH/2+50,SCREENHEIGHT/2+75)
    
    playColor = W
    infoColor = W
    
    while True:

        #EVENT HANDLING
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                if playRect.collidepoint(pygame.mouse.get_pos()):
                    scene1()
                if infoRect.collidepoint(pygame.mouse.get_pos()):
                    info()
                
        #GAME STATE

        # object color changes upon mouse hover.
        if playRect.collidepoint(pygame.mouse.get_pos()):
            playColor = (155,155,255)
        else:
            playColor = W
            
        if infoRect.collidepoint(pygame.mouse.get_pos()):
            infoColor = (155,155,255)
        else:
            infoColor = W
            
        
        #DRAW SCREEN
            
        SCREEN.fill(BG)

        titleSurface = TITLE.render(title['text'],True,title['color'])
        titleRect = titleSurface.get_rect()
        titleRect.center = title['pos']

        playSurface = FONT.render('play',True,playColor)
        playRect = playSurface.get_rect()
        playRect.center = (SCREENWIDTH/2-50,SCREENHEIGHT/2+75)

        infoSurface = FONT.render('info',True,infoColor)
        infoRect = infoSurface.get_rect()
        infoRect.center = (SCREENWIDTH/2+50,SCREENHEIGHT/2+75)
        
        SCREEN.blit(titleSurface,titleRect)
        SCREEN.blit(playSurface,playRect)
        SCREEN.blit(infoSurface,infoRect)

        pygame.draw.circle(SCREEN,W,(int(SCREENWIDTH/2),int(SCREENHEIGHT/2+75)),4)
        pygame.display.update()
        CLOCK.tick(60)

def info():

    #VARIABLE CREATION
    
    d = ['press SPACE to advance','click on KEY OBJECTS to make a decision']

    backSurface = FONT.render('back',True,W)
    backRect = backSurface.get_rect()
    backRect.center = (50,750)

    backColor = W
    
    while True:

        #EVENT HANDLING
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                if backRect.collidepoint(pygame.mouse.get_pos()):
                    menu()
                
        #GAME STATE
                    
        # object color changes upon mouse hover.          
        if backRect.collidepoint(pygame.mouse.get_pos()):
            backColor = (100,100,255)
        else:
            backColor = W
        
        #DRAW SCREEN
            
        SCREEN.fill(BG)

        backSurface = FONT.render('back',True,backColor)
        backRect = backSurface.get_rect()
        backRect.center = (50,50)

        d0Surface = FONT.render(d[0],True,W)
        d0Rect = d0Surface.get_rect()
        d0Rect.center = (SCREENWIDTH/2,100)

        d1Surface = FONT.render(d[1],True,W)
        d1Rect = d1Surface.get_rect()
        d1Rect.center = (SCREENWIDTH/2,150)

        SCREEN.blit(backSurface,backRect)
        SCREEN.blit(d0Surface,d0Rect)
        SCREEN.blit(d1Surface,d1Rect)

        pygame.display.update()
        CLOCK.tick(60)
        
def scene1(): #introduction: setting and exposition

    # play music
    pygame.mixer.music.load(MUSICPATH)
    pygame.mixer.music.play(loops=-1)
    
    #VARIABLE CREATION
    
    # scene text
    d1 = 'The trees tower over you, their leaves withered and their fruit rotting.'
    d2 = 'Dark shadows loom out at you, shaping black teeth and claws in the light'
    d3 = 'of the moon.'
    d4 = 'You have been walking for a day and half a night, but the winding forest'
    d5 = 'path has not yet yielded an exit.'
    d6 = '. . .'
    d7 = 'You trudge on.'
    d = [d1,d2,d3,d4,d5,d6,d7]

    # text box
    t = Textbox()
    
    # text scroll
    runText = True
    textScroll = '' 
    letterIndex = -1
    line = 0
    
    # scene visuals
    a1 = Trapezoid(300,450,200,210,550,380) 
    a2 = Trapezoid(360,385,80,315,430,170)
    a3 = Trapezoid(375,372,50,370,375,60)
    a = [a1,a2,a3] #list of trapezoids 

    # animation
    playAnimation = False
    darken = False
    darkValue = 0
    step = 0

    while True:
        
        #EVENT HANDLING
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:

                # advance the story.
                if event.key == K_SPACE:

                    # determine whether a line should currently be running. do not advance if True.
                    if not runText:
                        
                        # if scene lines have all been run through, play animation.
                        if line >= len(d)-1: 
                            playAnimation = True
                            darken = True

                        # otherwise, reset text scroll variables and advance to the next scene line.
                        else:
                            runText = True
                            textScroll = ''
                            letterIndex = -1
                            line += 1
                
        #GAME STATE

        # text scroll
        # determine whether a line should currently be running. scroll text if True.
        if runText:

            #stop scrolling if line is finished
            if letterIndex >= len(d[line])-1:
                runText = False

            else:
                letterIndex += 1
                textScroll += d[line][letterIndex]

        # animation
        # color change: white -> black -> white
        if playAnimation:
            if darken:
                darkValue += 5

                # when animation is finished running, advance to next scene.
                if step > len(a)-1:
                    darken = False
                    playAnimation = False
                    scene2()
                else:
                    if darkValue < 256:
                        a[step].color = (darkValue,darkValue,darkValue)
                    else:
                        step += 1
                        darkValue = 0
                
        # DRAW SCREEN
        
        SCREEN.fill(BG)

        # text box
        t.drawBox()

        # text scroll
        t.drawText(textScroll)
        if runText:
            time.sleep(0.04)

        # scene visuals + animation
        for trapezoid in a:
            trapezoid.draw()

        pygame.display.update()
        CLOCK.tick(60)

def scene2(): #decision 1: fork in the path

    #VARIABLE CREATION
    
    # scene text
    d1 = 'The path narrows, then forks into two.'
    d2 = 'One path leads to the left, and one to the right.'
    d3 = 'Which do you take?'
    d = [d1,d2,d3]
    
    # text box
    t = Textbox()
    
    # text scroll
    runText = True
    textScroll = '' 
    letterIndex = -1
    line = 0
    
    # scene visuals
    a1 = Trapezoid(300,450,200,210,550,380) 
    a2 = Trapezoid(360,385,80,315,430,170)
    a3 = Trapezoid(240,385,100,190,430,100)
    a4 = Trapezoid(460,385,100,510,430,100)
    a = [a1,a2,a3,a4] #list of trapezoids 

    # animation
    playAnimation = False
    
    lighten = False
    lightValue = 0

    darken = False
    darkValue = 0

    makeDecision = False
    
    while True:
        
        #EVENT HANDLING
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:

                # advance the story.
                if event.key == K_SPACE:

                    # determine whether a line should currently be running. do not advance if True.
                    if not runText:
                        
                        # if scene lines have all been run through, advance to next scene.
                        if line >= len(d)-1: 
                            playAnimation = True
                            if not makeDecision:
                                darken = True

                        # otherwise, reset text scroll variables and advance to the next scene line.
                        else:
                            runText = True
                            textScroll = ''
                            letterIndex = -1
                            line += 1

            # advance the story.                    
            if event.type == MOUSEBUTTONUP:
                if makeDecision:
                    if a3.rect.collidepoint(pygame.mouse.get_pos()) or a4.rect.collidepoint(pygame.mouse.get_pos()):
                        scene3()
                
        #GAME STATE

        # text scroll
        # determine whether a line should currently be running. scroll text if True.
        if runText:

            #stop scrolling if line is finished
            if letterIndex >= len(d[line])-1:
                runText = False

            else:
                letterIndex += 1
                textScroll += d[line][letterIndex]

        # animation
        # color change: white -> blue -> white
        if playAnimation:
            if darken:
                darkValue += 10
                if darkValue < 256:
                    a3.color = (255-darkValue,255-darkValue,255)
                    a4.color = (255-darkValue,255-darkValue,255)
                else:
                    darken = False
                    lighten = True

            if lighten:
                lightValue += 10
                if lightValue < 256:
                    a3.color = (lightValue,lightValue,255)
                    a4.color = (lightValue,lightValue,255)
                else:
                    lighten = False
                    playAnimation = False
                    makeDecision = True

        # object color changes upon mouse hover.
        if makeDecision:
            if a3.rect.collidepoint(pygame.mouse.get_pos()):
                a3.color = (155,155,255)
            elif a4.rect.collidepoint(pygame.mouse.get_pos()):
                a4.color = (155,155,255)
            else:
                a3.color = W
                a4.color = W
                
        # DRAW SCREEN
        
        SCREEN.fill(BG)

        # text box
        t.drawBox()

        # text scroll
        t.drawText(textScroll)
        if runText:
            time.sleep(0.04)
        
        # scene visuals
        for trapezoid in a:
            trapezoid.draw()

        pygame.display.update()
        CLOCK.tick(60)

def scene3(): #walk frames

    #VARIABLE CREATION
    
    # scene text
    d1 = 'You make your decision.'
    d2 = 'Your feet ache, but you lift them all the same.'
    d3 = '. . .'
    d4 = 'You are tired.'
    d = [d1,d2,d3,d4]

    # text box
    t = Textbox()
    
    # text scroll
    runText = True
    textScroll = '' 
    letterIndex = -1
    line = 0
    
    # scene visuals
    a1 = Trapezoid(300,450,200,210,550,380) 
    a2 = Trapezoid(360,385,80,315,430,170)
    a3 = Trapezoid(375,372,50,370,375,60)
    a = [a1,a2,a3] #list of trapezoids 

    # animation
    playAnimation = False
    darken = False
    darkValue = 0
    step = 0
    
    while True:
        
        #EVENT HANDLING
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:

                # advance the story.
                if event.key == K_SPACE:

                    # determine whether a line should currently be running. do not advance if True.
                    if not runText:
                        
                        # if scene lines have all been run through, play animation.
                        if line >= len(d)-1: 
                            playAnimation = True
                            darken = True

                        # otherwise, reset text scroll variables and advance to the next scene line.
                        else:
                            runText = True
                            textScroll = ''
                            letterIndex = -1
                            line += 1
                
        #GAME STATE

        # text scroll
        # determine whether a line should currently be running. scroll text if True.
        if runText:

            #stop scrolling if line is finished
            if letterIndex >= len(d[line])-1:
                runText = False

            else:
                letterIndex += 1
                textScroll += d[line][letterIndex]

        # animation
        # color change: white -> black -> white
        if playAnimation:
            if darken:
                darkValue += 5

                # when animation is finished running, advance to next scene.
                if step > len(a)-1:
                    darken = False
                    playAnimation = False
                    scene4()
                else:
                    if darkValue < 256:
                        a[step].color = (darkValue,darkValue,darkValue)
                    else:
                        step += 1
                        darkValue = 0
           
        # DRAW SCREEN
        
        SCREEN.fill(BG)

        # text box
        t.drawBox()

        # text scroll
        t.drawText(textScroll)
        if runText:
            time.sleep(0.04)

        # scene visuals + animation
        for trapezoid in a:
            trapezoid.draw()

        pygame.display.update()
        CLOCK.tick(60)

def scene4(): #close eyes

    #VARIABLE CREATION
    
    # scene text
    d1 = 'Hours pass.'
    d2 = 'Your eyelids grow heavy, and you struggle to keep them open.'
    d3 = 'Weary, you close your eyes for just a second.'
    d = [d1,d2,d3]

    # text box
    t = Textbox()
    
    # text scroll
    runText = True
    textScroll = '' 
    letterIndex = -1
    line = 0
    
    # scene visuals
    a1 = Trapezoid(300,450,200,210,550,380) 
    a2 = Trapezoid(360,385,80,315,430,170)
    a3 = Trapezoid(375,372,50,370,375,60)
    a = [a1,a2,a3] #list of trapezoids 

    # animation
    playAnimation = False

    lighten = False
    darken = False
    
    lightValue = 0
    darkValue = 0
    step = 0

    counter = 0
    
    makeDecision = False
    decision = random.randint(1,2)

    while True:
        
        #EVENT HANDLING
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:

                # advance the story.
                if event.key == K_SPACE:

                    # determine whether a line should currently be running. do not advance if True.
                    if not runText:
                        
                        # if scene lines have all been run through, play animation.
                        if line >= len(d)-1: 
                            playAnimation = True
                            darken = True

                        # otherwise, reset text scroll variables and advance to the next scene line.
                        else:
                            runText = True
                            textScroll = ''
                            letterIndex = -1
                            line += 1
                
        #GAME STATE

        # text scroll
        # determine whether a line should currently be running. scroll text if True.
        if runText:

            #stop scrolling if line is finished
            if letterIndex >= len(d[line])-1:
                runText = False

            else:
                letterIndex += 1
                textScroll += d[line][letterIndex]

        # animation
        # color change: white -> black -> white -> black -> white -> black
        if playAnimation:

            if darken:
                darkValue += 5
                if darkValue < 256:
                    for step in a:
                        step.color = (255-darkValue,255-darkValue,255-darkValue)
                else:
                    darken = False
                    if counter >= 2:
                        time.sleep(1)

                        # when animation is finished running, advance to next scene.
                        # 50/50 chance good choice/bad choice
                        if decision == 1:
                            scene5()
                        elif decision == 2:
                            scene6()
                    else:
                        lighten = True
                    
            elif lighten:
                if counter == 0:
                    lightValue += 15
                elif counter == 1:
                    lightValue += 2
                    
                if lightValue < 256:
                    for step in a:
                        step.color = (lightValue,lightValue,lightValue)
                else:
                    counter += 1
                    lighten = False
                    darken = True
                    lightValue = 0
                    darkValue = 0

        # DRAW SCREEN
        
        SCREEN.fill(BG)

        # text box
        t.drawBox()

        # text scroll
        t.drawText(textScroll)
        if runText:
            time.sleep(0.04)

        # scene visuals + animation
        for trapezoid in a:
            trapezoid.draw()
            
        pygame.display.update()
        CLOCK.tick(60)

def scene5(): #decision 2: wisp

    #VARIABLE CREATION
    
    # scene text
    d1 = 'When you open them again, a bright light hovers before your vision.'
    d2 = 'Bewildered, you blink hard in an attempt to dispel it.'
    d3 = 'Your head hurts. The light is still there.'
    d4 = 'Surely, you tell yourself, it is an effect of the fatigue.'
    d5 = 'A mere hallucination.'
    d6 = 'Even as you reassure yourself, the light bobs once, then floats off the path.'
    d7 = 'A few feet in, it stops again and flickers, as if compelling you to follow.'
    d8 = 'Do you follow the wisp off the path?'
    d = [d1,d2,d3,d4,d5,d6,d7,d8]

    # text box
    t = Textbox()
    
    # text scroll
    runText = True
    textScroll = '' 
    letterIndex = -1
    line = 0
    
    # scene visuals
    a1 = Trapezoid(300,450,200,210,550,380) 
    a2 = Trapezoid(360,385,80,315,430,170)
    a3 = Trapezoid(375,372,50,370,375,60)
    a = [a1,a2,a3] #list of trapezoids 

    # animation
    playAnimation = False
    lighten = False
    darken = False
    
    lightValue = 0
    darkValue = 0
    
    step = 0
    counter = 0
    
    makeDecision = False

    r1 = 10
    r2 = 20
    r3 = 50
    r = [r1,r2,r3] #wisp radii
    
    expandWisp = False
    compressWisp = False
    
    sizeChange = 0
    color = (230,230,230)

    nextScene = False
    
    while True:
        
        #EVENT HANDLING
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:

                # advance the story.
                if event.key == K_SPACE:

                    # determine whether a line should currently be running. do not advance if True.
                    if not runText:
                        
                        # if scene lines have all been run through, play animation.
                        if line >= len(d)-1: 
                            playAnimation = True
                            if not makeDecision:
                                expandWisp = True

                        # otherwise, reset text scroll variables and advance to the next scene line.
                        else:
                            runText = True
                            textScroll = ''
                            letterIndex = -1
                            line += 1

            # advance the story.
            if event.type == MOUSEBUTTONUP:
                if makeDecision:
                    if pygame.Rect(400-r1-5,230-r1,r1+5,r1+5).collidepoint(pygame.mouse.get_pos()):
                        counter = 0
                        makeDecision = False
                        playAnimation = True
                        expandWisp = True
                        nextScene = True
                    elif a1.rect.collidepoint(pygame.mouse.get_pos()):
                        makeDecision = False
                        playAnimation = True
                        darken = True
                        
        #GAME STATE

        # text scroll
        # determine whether a line should currently be running. scroll text if True.
        if runText:

            #stop scrolling if line is finished
            if letterIndex >= len(d[line])-1:
                runText = False

            else:
                letterIndex += 1
                textScroll += d[line][letterIndex]

        # animation
        # 1. wisp blink: expand -> compress -> expand -> compress -> expand
        # 2. color change: white -> black -> white
        if playAnimation:
            if expandWisp:
                if counter >= 2:
                    if sizeChange < 0:
                        sizeChange += 1
                    else:
                        expandWisp = False
                        compressWisp = False
                        playAnimation = False
                        
                        # when animation is finished running, advance to next scene.
                        if nextScene:
                            scene7()
                        else:
                            makeDecision = True
                else:
                    if sizeChange < 15:
                        sizeChange += 1
                    else:
                        expandWisp = False
                        compressWisp = True
                        
            elif compressWisp:
                if sizeChange > 0:
                    sizeChange -= 1
                else:
                    compressWisp = False
                    expandWisp = True
                    counter += 1
                    color = (230+2*sizeChange,230+2*sizeChange,230+2*sizeChange)

            if darken:
                darkValue += 5
                if step > len(a)-1:
                    darken = False
                    playAnimation = False
                    scene6()
                else:
                    if darkValue < 256:
                        a[step].color = (darkValue,darkValue,darkValue)
                    else:
                        step += 1
                        darkValue = 0

        # object color changes upon mouse hover.          
        if makeDecision:
            if pygame.Rect(400-r1-5,230-r1,r1+5,r1+5).collidepoint(pygame.mouse.get_pos()):
                color = (155,155,255)
            else:
                color = (230,230,230)
            if a1.rect.collidepoint(pygame.mouse.get_pos()):
                a1.color = (155,155,255)
            else:
                a1.color = W
            
                
        # DRAW SCREEN
        
        SCREEN.fill(BG)

        # text box
        t.drawBox()

        # text scroll
        t.drawText(textScroll)
        if runText:
            time.sleep(0.04)

        # scene visuals + animation
        for trapezoid in a:
            trapezoid.draw()

        # wisp
        pygame.draw.circle(SCREEN,(25+2*sizeChange,25+2*sizeChange,25+2*sizeChange),(400,230),r3+sizeChange//4)
        pygame.draw.circle(SCREEN,(100+2*sizeChange,100+2*sizeChange,100+2*sizeChange),(400,230),r2+sizeChange//4)
        pygame.draw.circle(SCREEN,color,(400,230),r1+sizeChange//4)

        pygame.display.update()
        CLOCK.tick(60)

def scene6(): #bad path choice -> game over: death via unknown creatures

    #VARIABLE CREATION
    
    # scene text
    d1 = 'When you open them again, the forest is pitch dark around you.'
    d2 = 'You look wildly about, but it is as if the moon itself has been extinguisjed.'
    d3 = 'There is no light, no shadow.'
    d4 = 'Only darkness.'
    d5 = 'Your heart stutters in its rhythm, beats quicker.'
    d6 = 'Fear clutches you tightly in its grip.'
    d7 = 'It consumes you.'
    d8 = 'You cannot breathe.'
    d9 = '...'
    d9 = 'A low growl. The click of sharp teeth against one another in the darkness.'
    d10 = 'They approach.'
    d11 = 'You scramble,'
    d12 = 'stumble,'
    d13 = 'fall.'
    d14 = 'You scream.'
    d15 = 'A red flash of pain, blinding, and then--'
    d = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15]

    # text box
    t = Textbox()
    
    # text scroll
    runText = True
    textScroll = '' 
    letterIndex = -1
    line = 0

    # animation
    playAnimation = False
    lighten = False
    darken = False

    lightValue = 0
    darkValue = 0
    step = 0

    color = BG
    
    while True:
        
        #EVENT HANDLING
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:

                # advance the story.
                if event.key == K_SPACE:

                    # determine whether a line should currently be running. do not advance if True.
                    if not runText:
                        
                        # if scene lines have all been run through, play animation.
                        if line >= len(d)-1: 
                            playAnimation = True
                            lighten = True

                        # otherwise, reset text scroll variables and advance to the next scene line.
                        else:
                            runText = True
                            textScroll = ''
                            letterIndex = -1
                            line += 1
                
        #GAME STATE

        # text scroll
        # determine whether a line should currently be running. scroll text if True.
        if runText:

            #stop scrolling if line is finished
            if letterIndex >= len(d[line])-1:
                runText = False

            else:
                letterIndex += 1
                textScroll += d[line][letterIndex]

        # animation
        # color change: black -> red -> black
        if playAnimation:
            if lighten:
                lightValue += 20
                if lightValue < 256:
                    color = (lightValue,0,0)
                else:
                    time.sleep(0.5)
                    lighten = False
                    darken = True
            elif darken:
                darkValue += 10
                if darkValue < 256:
                    color = (255-darkValue,0,0)
                else:
                    darken = False
                    time.sleep(1)
                    
                    # game over 
                    gameOver()
                
        # DRAW SCREEN
        
        SCREEN.fill(color)

        # text box
        t.drawBox()

        # text scroll
        t.drawText(textScroll)
        if runText:
            time.sleep(0.04)

        # scene visuals + animation
        pygame.display.update()
        CLOCK.tick(60)

def scene7(): #good path choice: advance story
    
    #VARIABLE CREATION
    
    # scene text
    d1 = 'How long have you been walking now?'
    d2 = 'Days, weeks, months, years?'
    d3 = 'An eternity, and then some.'
    d4 = 'Time slips through your fingers like sand in a sieve.'
    d = [d1,d2,d3,d4]

    # text box
    t = Textbox()
    
    # text scroll
    runText = True
    textScroll = '' 
    letterIndex = -1
    line = 0
    
    # scene visuals
    a1 = Trapezoid(300,450,200,210,550,380) 
    a2 = Trapezoid(360,385,80,315,430,170)
    a3 = Trapezoid(375,372,50,370,375,60)
    a = [a1,a2,a3] #list of trapezoids 

    # animation
    playAnimation = False
    
    darken = False
    darkValue = 0
    step = 0

    decision = random.randint(1,2)
    
    while True:
        
        #EVENT HANDLING
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:

                # advance the story.
                if event.key == K_SPACE:

                    # determine whether a line should currently be running. do not advance if True.
                    if not runText:
                        
                        # if scene lines have all been run through, play animation.
                        if line >= len(d)-1: 
                            playAnimation = True
                            darken = True

                        # otherwise, reset text scroll variables and advance to the next scene line.
                        else:
                            runText = True
                            textScroll = ''
                            letterIndex = -1
                            line += 1
                
        #GAME STATE

        # text scroll
        # determine whether a line should currently be running. scroll text if True.
        if runText:

            #stop scrolling if line is finished
            if letterIndex >= len(d[line])-1:
                runText = False

            else:
                letterIndex += 1
                textScroll += d[line][letterIndex]

        # animation
        # color change: white -> black -> white
        if playAnimation:
            if darken:
                darkValue += 5
                if step > len(a)-1:
                    darken = False
                    playAnimation = False
                    
                    # when animation is finished running, advance to next scene.
                    # 50/50 chance good choice/bad choice
                    if decision == 1:
                        scene8()
                    if decision == 2:
                        scene9()
                else:
                    if darkValue < 256:
                        a[step].color = (darkValue,darkValue,darkValue)
                    else:
                        step += 1
                        darkValue = 0
                
        # DRAW SCREEN
        
        SCREEN.fill(BG)

        # text box
        t.drawBox()

        # text scroll
        t.drawText(textScroll)
        if runText:
            time.sleep(0.04)

        # scene visuals + animation
        for trapezoid in a:
            trapezoid.draw()

        pygame.display.update()
        CLOCK.tick(60)

def scene8(): #good wisp choice -> game over: sunrise

    #VARIABLE CREATION
    
    # scene text
    d1 = 'Still, you walk, and the darkness starts to lift.'
    d2 = 'The trees thin.'
    d3 = 'You look up, and watch the sunlight filter through the branches.'
    d4 = 'You lift your face and let it wash over you.'
    d5 = 'In the distance, the sun rises, bathing the world in gold.'
    
    d = [d1,d2,d3,d4,d5]

    # text box
    t = Textbox()
    
    # text scroll
    runText = True
    textScroll = '' 
    letterIndex = -1
    line = 0
    
    # scene visuals
    a1 = Trapezoid(300,450,200,210,550,380) 
    a2 = Trapezoid(360,385,80,315,430,170)
    a3 = Trapezoid(375,372,50,370,375,60)
    a = [a1,a2,a3] #list of trapezoids
    
    # animation
    playAnimation = False
    lighten = False
    darken = False

    lightValue = 0
    darkValue = 0
    step = 0

    color = BG

    gradient = [(0,0,0),(26, 20, 0),(51, 39, 0),(77, 59, 0),(102, 78, 0),(128, 98, 0),(153, 117, 0),(179, 137, 0),(204, 156, 0),(230, 176, 0),(255, 196, 0),(255, 201, 26),(255, 207, 51),(255, 213, 77),(255, 219, 102),(255, 225, 128),(255, 231, 153),(255, 237, 179),(255, 243, 204),(255, 249, 230),(255,255,255)]
    shade = 0
    
    while True:
        
        #EVENT HANDLING
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:

                # advance the story.
                if event.key == K_SPACE:

                    # determine whether a line should currently be running. do not advance if True.
                    if not runText:
                        
                        # if scene lines have all been run through, play animation.
                        if line >= len(d)-1: 
                            playAnimation = True
                            lighten = True

                        # otherwise, reset text scroll variables and advance to the next scene line.
                        else:
                            runText = True
                            textScroll = ''
                            letterIndex = -1
                            line += 1
                
        #GAME STATE

        # text scroll
        # determine whether a line should currently be running. scroll text if True.
        if runText:

            #stop scrolling if line is finished
            if letterIndex >= len(d[line])-1:
                runText = False

            else:
                letterIndex += 1
                textScroll += d[line][letterIndex]

        # animation
        # color change: black -> gold -> white
        if playAnimation:
            if lighten:
                if shade > len(gradient)-1:
                    lighten = False
                    time.sleep(1)

                    # game over
                    gameOver()
                else:
                    color = gradient[shade]
                    shade += 1
                
        # DRAW SCREEN
        
        SCREEN.fill(color)
        if lighten:
            time.sleep(0.04)

        # text box
        t.drawBox()

        # text scroll
        t.drawText(textScroll)
        if runText:
            time.sleep(0.04)

        # scene visuals + animation
        for trapezoid in a:
            trapezoid.draw()
            
        pygame.display.update()
        CLOCK.tick(60)

def scene9(): #bad wisp choice -> game over: no escape

    #VARIABLE CREATION
    
    # scene text
    d1 = 'The forest darkens around you.'
    d2 = 'You walk, knowing that you will see no light of day.'
    d3 = 'You walk, knowing that death is coming for you.'
    
    d = [d1,d2,d3]

    # text box
    t = Textbox()
    
    # text scroll
    runText = True
    textScroll = '' 
    letterIndex = -1
    line = 0
    
    # scene visuals
    a1 = Trapezoid(300,450,200,210,550,380) 
    a2 = Trapezoid(360,385,80,315,430,170)
    a3 = Trapezoid(375,372,50,370,375,60)
    a = [a1,a2,a3] #list of trapezoids
    
    # animation
    playAnimation = False
    darken = False

    darkValue = 0
    
    while True:
        
        #EVENT HANDLING
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:

                # advance the story.
                if event.key == K_SPACE:

                    # determine whether a line should currently be running. do not advance if True.
                    if not runText:
                        
                        # if scene lines have all been run through, play animation.
                        if line >= len(d)-1: 
                            playAnimation = True
                            darken = True

                        # otherwise, reset text scroll variables and advance to the next scene line.
                        else:
                            runText = True
                            textScroll = ''
                            letterIndex = -1
                            line += 1
                
        #GAME STATE

        # text scroll
        # determine whether a line should currently be running. scroll text if True.
        if runText:

            #stop scrolling if line is finished
            if letterIndex >= len(d[line])-1:
                runText = False

            else:
                letterIndex += 1
                textScroll += d[line][letterIndex]

        # animation
        # color change: white -> black
        if playAnimation:
            if darken:
                darkValue += 10
                if darkValue < 256:
                    for step in a:
                        step.color = (255-darkValue,255-darkValue,255-darkValue)
                else:
                    time.sleep(0.5)
                    darken = False
                    gameOver()
                
        # DRAW SCREEN
        
        SCREEN.fill(BG)

        # text box
        t.drawBox()

        # text scroll
        t.drawText(textScroll)
        if runText:
            time.sleep(0.04)

        # scene visuals + animation
        for trapezoid in a:
            trapezoid.draw()
            
        pygame.display.update()
        CLOCK.tick(60)

def gameOver():
    
    pygame.mixer.music.load(TITLEPATH)
    pygame.mixer.music.play(loops=-1)
    
    #VARIABLE CREATION
    
    d = ['Your story is over. Would you like to start a new one?']

    yesSurface = FONT.render('yes',True,W)
    yesRect = yesSurface.get_rect()
    yesRect.center = (SCREENWIDTH/2-50,SCREENHEIGHT/2+125)

    noSurface = FONT.render('no',True,W)
    noRect = noSurface.get_rect()
    noRect.center = (SCREENWIDTH/2+50,SCREENHEIGHT/2+125)

    yesColor = W
    noColor = W
    
    while True:

        #EVENT HANDLING
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                if yesRect.collidepoint(pygame.mouse.get_pos()):
                    menu()
                if noRect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                
        #GAME STATE
                    
        if yesRect.collidepoint(pygame.mouse.get_pos()):
            yesColor = (100,100,255)
        else:
            yesColor = W
        if noRect.collidepoint(pygame.mouse.get_pos()):
            noColor = (100,100,255)
        else:
            noColor = W
        
        #DRAW SCREEN
            
        SCREEN.fill(BG)

        endSurface = TITLE.render('THE END',True,W)
        endRect = endSurface.get_rect()
        endRect.center = (SCREENWIDTH/2,SCREENHEIGHT/2)

        d0Surface = FONT.render(d[0],True,W)
        d0Rect = d0Surface.get_rect()
        d0Rect.center = (SCREENWIDTH/2,SCREENHEIGHT/2+50)

        yesSurface = FONT.render('yes',True,yesColor)
        yesRect = yesSurface.get_rect()
        yesRect.center = (SCREENWIDTH/2-50,SCREENHEIGHT/2+125)

        noSurface = FONT.render('no',True,noColor)
        noRect = noSurface.get_rect()
        noRect.center = (SCREENWIDTH/2+50,SCREENHEIGHT/2+125)

        SCREEN.blit(endSurface,endRect)
        SCREEN.blit(d0Surface,d0Rect)
        SCREEN.blit(yesSurface,yesRect)
        SCREEN.blit(noSurface,noRect)

        pygame.draw.circle(SCREEN,W,(int(SCREENWIDTH/2),int(SCREENHEIGHT/2+125)),4)
        pygame.display.update()
        CLOCK.tick(60)
        
    
def main():
    menu()
    
    while True: 
            
        #EVENT HANDLING
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()

main()
