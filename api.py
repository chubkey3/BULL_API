import pygame, random, json, requests, sys
from crapi import crapi
class GOLMBUTTON(object):
    def __init__(self,wernmrnwenreuwjndfjonbiudfbnjkrensdfoinweornweiornoskdnmvkcnbjklcvnbjkdrkrhjbgerjkltnrjbtidjnbiubndriutnodrngidnfgjkdnbjkcvnkbjndkjrbtjkrnbtjkebriktjberkjbntkjebnrtreter,rect,color,text="",textcolor=(0,0,0)):
        self.playplaykinggolemwolf=wernmrnwenreuwjndfjonbiudfbnjkrensdfoinweornweiornoskdnmvkcnbjklcvnbjkdrkrhjbgerjkltnrjbtidjnbiubndriutnodrngidnfgjkdnbjkcvnkbjndkjrbtjkrnbtjkebriktjberkjbntkjebnrtreter#don't worry, you can refer to this as playplaykinggolemwolf not what it actually is
        self.rect=rect#actually a normal variable name
        self.hahaidontcarethatyourhousesoldormadeyoulotsofmoney_iusedtarasgadgetstillcouldnotfindwhoasked=color
        self.text=text
        self.hahaidontcarethatyourhousesoldormadeyoulotsofmonfy_iusedtarasgadgetstillcouldnotfindwhoasked=textcolor
    def display(self):#honestly a very simple function but so hard to read... it's all your fault "senior engineer", totally done by accident and/or lack of a creative mind
        pygame.draw.rect(self.playplaykinggolemwolf,self.hahaidontcarethatyourhousesoldormadeyoulotsofmoney_iusedtarasgadgetstillcouldnotfindwhoasked,self.rect)
        displaytextoutline(self.playplaykinggolemwolf,self.text,self.rect.center,KINGFONT,color=self.hahaidontcarethatyourhousesoldormadeyoulotsofmonfy_iusedtarasgadgetstillcouldnotfindwhoasked)
    def click(self,mouse):
        if (mouse[0]>=self.rect.left and mouse[0]<=self.rect.right and mouse[1]>=self.rect.top and mouse[1]<=self.rect.bottom):#is that another giant if statment i see?!!??1!!??1!
            return True
        return False

class text_input_box(GOLMBUTTON):
    def __init__(self,surface,rect,color):
        super().__init__(surface,rect,color)
        self.clicked=False
    def display(self):
        if (self.clicked):
            pygame.draw.rect(self.playplaykinggolemwolf,(0,207,255),self.rect)
        else:
            pygame.draw.rect(self.playplaykinggolemwolf,self.hahaidontcarethatyourhousesoldormadeyoulotsofmoney_iusedtarasgadgetstillcouldnotfindwhoasked,self.rect)
        
        if (len(self.text)<8):
            displaytextoutline(self.playplaykinggolemwolf,self.text,self.rect.center,GOLMFONT,color=(212,91,208))
        else:
            displaytextoutline(self.playplaykinggolemwolf,self.text,self.rect.center,KINGFONT,color=(212,91,208))
    def addcharacter(self,key):
        if (len(self.text)<11):
            if (key==pygame.K_0):
                self.text+="0"
            elif (key==pygame.K_2):
                self.text+="2"
            elif (key==pygame.K_8):
                self.text+="8"
            elif (key==pygame.K_9):
                self.text+="9"
            elif (key==pygame.K_c):
                self.text+="C"
            elif (key==pygame.K_g):
                self.text+="G"
            elif (key==pygame.K_j):
                self.text+="J"
            elif (key==pygame.K_l):
                self.text+="L"
            elif (key==pygame.K_p):
                self.text+="P"
            elif (key==pygame.K_q):
                self.text+="Q"
            elif (key==pygame.K_r):
                self.text+="R"
            elif (key==pygame.K_u):
                self.text+="U"
            elif (key==pygame.K_v):
                self.text+="V"
            elif (key==pygame.K_y):
                self.text+="Y"
        if (key==pygame.K_BACKSPACE):
            if (len(self.text)>0):
                self.text=self.text[:-1]
        elif (key==pygame.K_RETURN):
            self.clicked=False
def displaytext(surface,text,position,font,color=(0,0,0),align=(0,0)):#better?
    display=font.render(text,True,color)
    rect=display.get_rect()
    rect.centerx=int(position[0]-rect.width*0.5*(align[0]))
    rect.centery=int(position[1]-rect.height*0.5*(align[1]))
    surface.blit(display,rect)

def displaytextoutline(surface,text,position,font,color=(0,0,0),outline_color=(0,0,0),align=(0,0)):
    size=max(1,(font.size(text)[1]*0.6*0.0625))#works best with KINGFONT.ttf
    outline=font.render(text,True,outline_color)
    rect=outline.get_rect()
    for a in range(-1,2):
        for b in range(-1,2):
            if (a!=0 or b!=0):
                rect.centerx=int(position[0]-rect.width*0.5*(align[0])+int(a*size))
                rect.centery=int(position[1]-rect.height*0.5*(align[1])+int(b*size))
                surface.blit(outline,rect)
    displaytext(surface,text,position,font,color,align=align)

def displaychests(surface,position,chests):
    displaytextoutline(surface,"Current Player:",(position[0]+360,position[1]+90),RVGRFONT,color=(129,214,61),align=(0,1))
    displaytextoutline(surface,playername,(position[0]+360,position[1]+90),RVGRFONT,color=(129,214,61),align=(0,-1))

    pygame.draw.rect(surface,(0,64,0),pygame.Rect(position[0]+720,position[1],360,180))
    pygame.draw.rect(surface,(0,0,0),pygame.Rect(position[0]+912,position[1]+12,156,156))
    pygame.draw.rect(surface,(28,28,0),pygame.Rect(position[0]+915,position[1]+15,150,150))
    if (chests[0] in chest_images):
        surface.blit(pygame.transform.scale(chest_images[chests[0]],(150,150)),(position[0]+915,position[1]+15))
    displaytextoutline(surface,"Next",(position[0]+810,position[1]+90),GOLMFONT,color=(129,214,61),align=(0,1))
    displaytextoutline(surface,"Chest",(position[0]+810,position[1]+90),GOLMFONT,color=(129,214,61),align=(0,-1))


    pygame.draw.rect(surface,(0,64,0),pygame.Rect(position[0],position[1]+210,1080,540))
    displaytextoutline(surface,"Your Upcoming Chests",(position[0]+540,position[1]+210+20),GOLMFONT,color=(129,214,61),align=(0,-1))
    counter=[0,0]

    for x in chests.keys():
        if (chests[x] in chest_images):
            if (x<=8 and x>0):
                pygame.draw.rect(surface,(0,0,0),pygame.Rect(position[0]+68+counter[0]*120,position[1]+210+103+KINGFONT.size(str(x))[1],104,104))
                pygame.draw.rect(surface,(14,16,23),pygame.Rect(position[0]+70+counter[0]*120,position[1]+210+105+KINGFONT.size(str(x))[1],100,100))
                if (chests[x] not in ["SilverChest","GoldenChest"]):
                    surface.blit(pygame.transform.scale(chest_images[chests[x]],(100,100)),(position[0]+70+counter[0]*120,position[1]+210+105+KINGFONT.size(str(x))[1]))
                else:
                    surface.blit(chest_images[chests[x]],(position[0]+70-10+counter[0]*120,position[1]+210+105-20+KINGFONT.size(str(x))[1]))
                displaytextoutline(surface,"+"+str(x),(position[0]+(counter[0]+1)*120,position[1]+210+100),KINGFONT,color=(142,155,229),align=(0,-1))
                counter[0]+=1
            #for x in range(min(len(futurechests),len(futurenumber))):
            elif (chests[x] not in ["SilverChest","GoldenChest"]):
                pygame.draw.rect(surface,(0,0,0),pygame.Rect(position[0]+73+counter[1]*192,position[1]+210+297+GOLMFONT.size(str(x))[1],166,166))
                pygame.draw.rect(surface,(26,0,20),pygame.Rect(position[0]+76+counter[1]*192,position[1]+210+300+GOLMFONT.size(str(x))[1],160,160))
                surface.blit(chest_images[chests[x]],(position[0]+76+counter[1]*192,position[1]+210+300+GOLMFONT.size(str(x))[1]))
                displaytextoutline(surface,"+"+str(x),(position[0]+60+96+counter[1]*192,position[1]+210+300),GOLMFONT,color=(255,3,204),align=(0,-1))
                counter[1]+=1





pygame.init()
pygame.font.init()
pygame.mixer.init()
screenx=1280
screeny=900
menu="main"
screen = pygame.display.set_mode((screenx,screeny))
pygame.display.set_caption("Brawl Ball > Heist > Siege > Gem Grab > Bounty > THE KING")
clock = pygame.time.Clock()
KINGFONT = pygame.font.Font("KINGFONT.ttf",36)
GOLMFONT = pygame.font.Font("KINGFONT.ttf",48)
RVGRFONT = pygame.font.Font("KINGFONT.ttf",60)

chest_images={
    "SilverChest":pygame.transform.scale(pygame.image.load("SilverChest.png"),(120,120)),
    "GoldenChest":pygame.transform.scale(pygame.image.load("GoldenChest.png"),(120,120)),
    "GiantChest":pygame.transform.scale(pygame.image.load("GiantChest.png"),(160,160)),
    "MagicalChest":pygame.transform.scale(pygame.image.load("MagicalChest.png"),(160,160)),
    "EpicChest":pygame.transform.scale(pygame.image.load("EpicChest.png"),(160,160)),
    "LegendaryChest":pygame.transform.scale(pygame.image.load("LegendaryChest.png"),(160,160)),
    "MegaLightningChest":pygame.transform.scale(pygame.image.load("MegaLightningChest.png"),(160,160)),
    }

chestcycle={
    0:"SilverChest",
    1:"SilverChest",
    2:"SilverChest",
    3:"GoldenChest",
    4:"SilverChest",
    5:"GoldenChest",
    6:"SilverChest",
    7:"SilverChest",
    8:"GoldenChest",
    12:"MagicalChest",
    28:"GiantChest",
    69:"EpicChest",
    420:"MegaLightningChest",
    999:"LegendaryChest",
    }

playername="BULL API"
annoyusertime=0.0

chestbutton=GOLMBUTTON(screen,pygame.Rect(0,0,400,900),(156,80,243))
decksbutton=GOLMBUTTON(screen,pygame.Rect(880,0,400,900),(156,80,243))
backbutton=GOLMBUTTON(screen,pygame.Rect(50,50,150,50),(240,80,49),"Go Back",textcolor=(85,255,85))
loadbutton=GOLMBUTTON(screen,pygame.Rect(565,300,150,40),(255,3,204),"Load!",textcolor=(240,80,49))
playertag=text_input_box(screen,pygame.Rect(530,200,260,70),(142,155,229))

royalebg=pygame.Surface((screen.get_width(),screen.get_height()),pygame.SRCALPHA)
royalebg.blit(pygame.transform.scale(pygame.image.load("backround.png"),(1280,900)),(0,0))
chestbg=pygame.Surface((screen.get_width(),screen.get_height()),pygame.SRCALPHA)
chestbg.blit(pygame.transform.scale(pygame.image.load("chestbackround.png"),(1280,900)),(0,0))
decksbg=pygame.Surface((screen.get_width(),screen.get_height()),pygame.SRCALPHA)
decksbg.blit(pygame.transform.scale(pygame.image.load("ELIXIR_GOLM.png"),(1280,900)),(0,0))
R_G=pygame.Surface((screen.get_width(),screen.get_height()),pygame.SRCALPHA)
R_G.blit(pygame.transform.scale(pygame.image.load("error_02.png"),(1280,900)),(0,0))
BULL=pygame.transform.scale(pygame.image.load("BUL_API.png"),(400,400))

kingmad_sound=pygame.mixer.Sound("king_mad_03.ogg")

#do not change information below\
done=False
# main program loop
while (done == False):
    #all event processing goes below
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True#User perssed close
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            if (event.button==1):
                if (menu=="main"):
                    if (chestbutton.click(pygame.mouse.get_pos())):
                        menu="chests"
                    elif (decksbutton.click(pygame.mouse.get_pos())):
                        menu="decks"
                    elif (loadbutton.click(pygame.mouse.get_pos())):
                        chestcycle_01=chest_cycle(playertag.text)
                        if (chestcycle_01!="Invalid tag"):
                            player_info = crapi(playertag.text)
                            chestcycle=dict(chestcycle_01)
                        elif (playertag.text!=""):
                            menu="rg"
                            annoyusertime=4.5
                            kingmad_sound.play()
                        playername=(get_stat(playertag.text,2))
                        playertag.clicked=False
                        playertag.text=""
                        #make it load the player tag here
                    elif (playertag.click(pygame.mouse.get_pos())):
                        if (playertag.clicked):
                            playertag.clicked=False
                        else:
                            playertag.clicked=True
                    
                elif (backbutton.click(pygame.mouse.get_pos()) and (menu=="chests" or menu=="decks")):
                    menu="main"
        if event.type==pygame.KEYDOWN:
            if (playertag.clicked):
                playertag.addcharacter(event.key)
    
    #-----------------------------------
    screen.fill(0)
    if (menu!="main"):
        playertag.clicked=False
    
    if (menu=="main"):
        screen.blit(royalebg,(0,0))
        screen.blit(BULL,(440,480))

        displaytextoutline(screen,"BULL API",(640,50),RVGRFONT,color=(212,91,208))
        displaytextoutline(screen,"Enter Player Tag",(640,200),KINGFONT,color=(255,3,204),align=(0,1))
        displaytextoutline(screen,"View your",(200,450),GOLMFONT,color=(212,91,208),align=(0,1))
        displaytextoutline(screen,"upcoming chests",(200,450),GOLMFONT,color=(212,91,208),align=(0,-1))
        displaytextoutline(screen,"View popular",(1080,450),GOLMFONT,color=(212,91,208),align=(0,1))
        displaytextoutline(screen,"decks",(1080,450),GOLMFONT,color=(212,91,208),align=(0,-1))
        displaytextoutline(screen,"Current Player",(640,410),KINGFONT,color=(156,80,243),align=(0,1))
        displaytextoutline(screen,playername,(640,410),GOLMFONT,color=(156,80,243),align=(0,-1))
        
        pygame.draw.line(screen,(0,0,0),(400,0),(400,900),14)
        pygame.draw.line(screen,(0,207,255),(400,0),(400,900),10)
        pygame.draw.line(screen,(0,0,0),(880,0),(880,900),14)
        pygame.draw.line(screen,(0,207,255),(880,0),(880,900),10)
        pygame.draw.rect(screen,(71,78,115),pygame.Rect(490,200,40,70))
        displaytextoutline(screen,"#",(510,235),GOLMFONT,color=(212,91,208))

        playertag.display()
        loadbutton.display()
    elif (menu=="chests"):
        screen.blit(chestbg,(0,0))
        displaychests(screen,(100,100),chestcycle)
        backbutton.display()
    elif (menu=="decks"):
        screen.blit(decksbg,(0,0))
        backbutton.display()
    elif (menu=="rg"):
        screen.blit(R_G,(0,0))

    
    #print (clock.get_rawtime())
    #-----------------------------------
    bulltime1=clock.get_time()/1000.0
    if (annoyusertime>0.0):
        annoyusertime-=bulltime1
        if (annoyusertime<=0.0):
            annoyusertime=0.0
            menu="main"
    #-----------------------------------
    pygame.display.flip()
    clock.tick(60)
    #-----------------------------------
pygame.quit()