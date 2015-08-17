import pygame, sys
from pygame.locals import *
class chessPiece(pygame.sprite.Sprite):
    def __init__(self,team,piecetype, name,default_pos,fillcolor):
        self.team = team
        self.piecetype = piecetype
        self.name = name
        self.defpos = default_pos
        self.fillcolor = fillcolor
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(self.team + self.piecetype +'.png')
        self.defrect = self.image.get_rect()
        self.rect = self.image.get_rect()
    def update(self, pos, is_moving):
        self.pos = pos
        self.defrect.center = self.defpos
        self.is_moving = is_moving
        self.rect.center = self.pos
        if self.is_moving:
            print self.defrect
            Main.DISPLAYSURF.fill(self.fillcolor, self.defrect)
    size = 50
class Main:
    def __init__(self):
        pygame.init()
        FPS = 30
        fpsclock = pygame.time.Clock()
        #create display surface
        Main.DISPLAYSURF = pygame.display.set_mode((1000,800))
        #init mouse status variables
        self.mouse_pressed = False
        self.mouse_down = False
        self.mouse_released = False
        self.target = None
        #window title
        pygame.display.set_caption('Chess')
        #define chess square colors
        self.blackSpace = pygame.Color(0,0,0,128)
        self.whiteSpace = pygame.Color(255,255,255,128)
        #column must start at 1 for proper coloring of spaces
        #0 mod 2 is 0, so square 1 (a8) would be black when it should be white
        self.drawboard(0,1)
        #WORKS AND IS NOT A HACK
        #WHOO
        #create 64 squares
        #each piece sprite must be in a separate group so they can be drawn separately
        #we create dicts to hold these groups so they can have individual names
        self.pawnsdict = {}
        self.makepawns()
        self.piecesdict = {}
        self.makepieces()
        self.alldict = dict(self.pawnsdict, **self.piecesdict)
        while True:
            self.mousepos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_pressed = True
                    self.mouse_down = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_released = True
                    self.mouse_down = False
            #if mouse is pressed and no sprite is being dragged
            #check all sprites to see if the mouse is inside them
            #if it is, set that sprite as target
            if self.mouse_pressed == True and self.target == None:
                for name,spritegroup in self.alldict.iteritems():
                    sprite = spritegroup.sprite
                    if (self.mousepos[0]>=(sprite.pos[0]-sprite.size) and
                        self.mousepos[0]<=(sprite.pos[0]+sprite.size) and
                        self.mousepos[1]>=(sprite.pos[1]-sprite.size) and
                        self.mousepos[1]<=(sprite.pos[1]+sprite.size)):
                        self.target=sprite
            #if m1 is held down and there is a target sprite
            #constantly update its group's position to the mouse's
            if self.mouse_down and  self.target is not None:
                #self.target.pos = self.mousepos
                self.targetgroup = self.target.groups()
                self.targetgroup[0].update(self.mousepos, True)
                pygame.display.flip()
            #when the mouse is released, draw the sprite in its new position
            #reset target to none
            if self.mouse_released:
                self.targetgroup[0].draw(Main.DISPLAYSURF)
                self.target = None
                self.mouse_pressed = False
                self.mouse_released = False
            pygame.display.update()
            fpsclock.tick(FPS)
    def drawboard(self,row,col):
        self.row = row
        self.col = col
        for x in range (1, 65):
            #on even rows, even squares are white
            #on odd rows, odd squares are white
            #the first row is an 'even row' because we start counting at 0
            #and 0 is treated as even using mod
            if self.row%2 == 0 and self.col%2 == 0:
                self.spacecolor = self.blackSpace
            elif self.row%2 == 0 and self.col%2 !=0:
                self.spacecolor = self.whiteSpace
            elif self.row%2 !=0 and self.col%2 ==0:
                self.spacecolor = self.whiteSpace
            elif self.row%2 !=0 and self.col%2 !=0:
                self.spacecolor = self.blackSpace
            #calculate x and y coordinates for top left corners of squares
            #for purposes of this calculation, first column needs to be
            #treated as zero
            self.cornerx = ((self.col-1)*125) 
            self.cornery = self.row*100
            #draw calculated rectangles
            pygame.draw.rect(Main.DISPLAYSURF, self.spacecolor,
                            (self.cornerx,self.cornery,125,100))
            #once we reach the 8th col, set variables to first column on the next row
            if self.col == 8:
                self.col = 1
                self.row +=1
            #if we haven't yet, just increment column for the next square
            else:
                self.col +=1
    def makepawns(self):
        for x in range (0,16):
            self.pawnsdict["pawn"+str(x)]= pygame.sprite.GroupSingle()
            if x < 8:
                self.pawncolor = "black"
                self.pawnpos = (50 + 125*x, 150)
                if x %2 == 0:
                    self.fillcolor = (0,0,0)
                else:
                    self.fillcolor = (255,255,255)
            elif x >= 8:
                self.pawncolor = "white"
                self.pawnpos = (50+125*(x-8), 600)
                if x %2 != 0:
                    self.fillcolor = (0,0,0)
                else:
                    self.fillcolor = (255,255,255)
            self.ind_pawn_name = "pawn" + str(x)
            self.pawn = chessPiece(self.pawncolor, "pawn",
                                   self.ind_pawn_name, self.pawnpos, self.fillcolor)
            self.pawnsdict["pawn"+str(x)].add(self.pawn)
            self.pawnsdict["pawn"+str(x)].update(self.pawnpos, False)
            self.pawnsdict["pawn"+str(x)].draw(Main.DISPLAYSURF)
            pygame.display.flip()
    def makepieces(self):
        for x in range (0,16):
            self.piecesdict["piece"+str(x)] = pygame.sprite.GroupSingle()
            if x < 8:
                self.piececolor = "black"
                self.piecepos = (50+125*x, 50)
                if x %2 != 0:
                    self.fillcolor = (0,0,0)
                else:
                    self.fillcolor = (255,255,255)
            elif x >= 8:
                self.piececolor = "white"
                self.piecepos = (50+125*(x-8), 700)
                if x %2 == 0:
                    self.fillcolor = (0,0,0)
                else:
                    self.fillcolor = (255,255,255)
            rooks = [0,7,8,15]
            knights = [1,6,9,14]
            bishops = [2,5,10,13]
            kings = [3,11]
            queens = [4,12]
            if x in rooks:
                self.piecename = "rook"
            elif x in knights:
                self.piecename = "knight"
            elif x in bishops:
                self.piecename = "bishop"
            elif x in kings:
                self.piecename = "king"
            elif x in queens:
                self.piecename = "queen"
            self.ind_piece_name = self.piecename + str(x)
            self.piece = chessPiece(self.piececolor, self.piecename,
                                    self.ind_piece_name,self.piecepos,
                                    self.fillcolor)
            self.piecesdict["piece"+str(x)].add(self.piece)
            self.piecesdict["piece"+str(x)].update(self.piecepos, False)
            self.piecesdict["piece"+str(x)].draw(Main.DISPLAYSURF)
            pygame.display.flip()       
#mainloop
if __name__=="__main__":
    main = Main()
