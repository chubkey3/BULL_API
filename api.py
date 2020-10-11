import pygame, random, json, requests, sys, win32clipboard
from crapi import *
import whatplayer,textbox
class GOLMBUTTON(object):
    def __init__(self,wernmrnwenreuwjndfjonbiudfbnjkrensdfoinweornweiornoskdnmvkcnbjklcvnbjkdrkrhjbgerjkltnrjbtidjnbiubndriutnodrngidnfgjkdnbjkcvnkbjndkjrbtjkrnbtjkebriktjberkjbntkjebnrtreter,rect,color,font,text="",textcolor=(0,0,0)):
        self.playplaykinggolemwolf=wernmrnwenreuwjndfjonbiudfbnjkrensdfoinweornweiornoskdnmvkcnbjklcvnbjkdrkrhjbgerjkltnrjbtidjnbiubndriutnodrngidnfgjkdnbjkcvnkbjndkjrbtjkrnbtjkebriktjberkjbntkjebnrtreter#don't worry, you can refer to this as playplaykinggolemwolf not what it actually is
        self.rect=rect#actually a normal variable name
        self.hahaidontcarethatyourhousesoldormadeyoulotsofmoney_iusedtarasgadgetstillcouldnotfindwhoasked=color
        self.text=text
        self.font=font
        self.hahaidontcarethatyourhousesoldormadeyoulotsofmonfy_iusedtarasgadgetstillcouldnotfindwhoasked=textcolor
    def display(self):#honestly a very simple function but so hard to read... it's all your fault "senior engineer", totally done by accident and/or lack of a creative mind
        pygame.draw.rect(self.playplaykinggolemwolf,self.hahaidontcarethatyourhousesoldormadeyoulotsofmoney_iusedtarasgadgetstillcouldnotfindwhoasked,self.rect)
        displaytextoutline(self.playplaykinggolemwolf,self.text,self.rect.center,self.font,color=self.hahaidontcarethatyourhousesoldormadeyoulotsofmonfy_iusedtarasgadgetstillcouldnotfindwhoasked)
    def click(self,mouse):
        if (mouse[0]>=self.rect.left and mouse[0]<=self.rect.right and mouse[1]>=self.rect.top and mouse[1]<=self.rect.bottom):#is that another giant if statment i see?!!??1!!??1!
            return True
        return False

class text_input_box(GOLMBUTTON):
    def __init__(self,surface,rect,color,font):
        super().__init__(surface,rect,color,font)
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
        elif (key==pygame.K_LCTRL):
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            self.text = data[0:11]
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

def displayprofile(surface,position,playername,stats):
    xsize=350
    ysize=550
    stat_separation=60
    stats_names=["King Level","Total Donations","Wins","Highest Trophies"]
    stats_index=["level","donations","wins","trophies"]

    #main background
    pygame.draw.rect(surface,(142,155,229),pygame.Rect(position[0]-3,position[1]-3,xsize+6,ysize+6))
    pygame.draw.rect(surface,(0,0,64),pygame.Rect(position[0],position[1],xsize,ysize))

    #lines
    pygame.draw.line(surface,(142,155,229),(position[0],position[1]+60),(position[0]+xsize,position[1]+60),3)
    pygame.draw.line(surface,(142,155,229),(position[0]+stat_separation,position[1]+80),(position[0]+stat_separation,position[1]+80+min(len(stats_names),len(stats_index))*stat_separation),3)
    for x in range(min(len(stats_names),len(stats_index))+1):
        pygame.draw.line(surface,(142,155,229),(position[0],position[1]+80+stat_separation*(x)),(position[0]+xsize,position[1]+80+stat_separation*(x)),3)
    
    #player name
    displaytextoutline(surface,playername,(position[0]+int(xsize/2),position[1]+30),KINGFONT,color=(255,3,204))

    #stats
    for x in range(min(len(stats_names),len(stats_index))):
        displaytextoutline(surface,stats_names[x],(position[0]+stat_separation+int((xsize-stat_separation)/2),position[1]+80+x*stat_separation+3),PESTFONT,color=(255,3,204),align=(0,-1))
        displaytextoutline(surface,str(stats[stats_index[x]]),(position[0]+stat_separation+int((xsize-stat_separation)/2),position[1]+80+x*stat_separation+max(0,int(stat_separation/2+PESTFONT.size(stats_names[x])[1]/2))),KINGFONT,color=(255,3,204),align=(0,0))
        if (stats_index[x]=="level"):
            surface.blit(kinglevel,(position[0],position[1]+80+x*stat_separation))
        elif (stats_index[x]=="donations"):
            surface.blit(donations,(position[0],position[1]+80+x*stat_separation))
        elif (stats_index[x]=="wins"):
            surface.blit(wins,(position[0],position[1]+80+x*stat_separation))
        elif (stats_index[x]=="trophies"):
            league=calculateleague(stats[stats_index[x]])
            if (league>-1):
                surface.blit(leagueimages,(position[0],position[1]+80+x*stat_separation),area=pygame.Rect(league*(leagueimages.get_width()//10),0,stat_separation,stat_separation))
    displaytext(surface,"Battle Deck",(position[0]+int(xsize/2),position[1]+80+min(len(stats_names),len(stats_index))*stat_separation+3),PESTFONT,color=(255,3,204),align=(0,-1))
    
    #battle deck
    for x in range(2):
        for y in range(len(current_deck_02)//2):
            displaycard(screen,current_deck_02[y+len(current_deck_02)//2*x][0],(position[0]+25+y*80,position[1]+ysize-200+x*90))
            pygame.draw.circle(screen,(142,155,229),(position[0]+25+30+y*80,position[1]+ysize-200+72+x*90),10)
            displaytextoutline(surface,str(current_deck_02[y+len(current_deck_02)//2*x][1]),(position[0]+25+30+y*80,position[1]+ysize-200+72+x*90),CARDFONT,color=(255,3,204))
    displaytextoutline(surface,"Average Card Level: "+str(getdecklevel(current_deck_02)),(position[0]+int(xsize/2),position[1]+ysize-3),PESTFONT,color=(255,3,204),align=(0,1))

def displaycard(surface,nospacename,position):
    index=(whatplayer.cardnames.index(nospacename))
    xarea=(index%cardimagedimensions[0]*cardimage.get_width()//cardimagedimensions[0])
    yarea=(index//cardimagedimensions[1]*cardimage.get_height()//cardimagedimensions[1])
    surface.blit(cardimage,position,area=pygame.Rect(xarea,yarea,cardimage.get_width()//cardimagedimensions[0],cardimage.get_height()//cardimagedimensions[1]))

def getdecklevel(currentdeck):
    total=0

    for x in range(len(currentdeck)):
        total+=currentdeck[x][1]
    total/=max(1,len(currentdeck))

    if (((total*100)%10)%1==0.5):
        lastdigit=int((total*100)%10)
        if (lastdigit%2==0):
            total=(int(total*100)/100)
        elif (lastdigit%2==1):
            total=(int(total*100+1)/100)
    else:
        total=round(total,2)

    GOLMTOTAL=str(total)+"0"*(2-len(str(total).split(".")[1]))
    return GOLMTOTAL

def calculateleague(trophies):
    if (trophies<4000):
        return -1
    elif (trophies<7000):
        league_01=((trophies-4000)//1000)*3
        league_02=trophies%1000
        if (league_02<300):
            return league_01
        elif (league_02<600):
            return league_01+1
        elif (league_02<1000):
            return league_01+2
    else:
        return 9

pygame.init()
pygame.font.init()
pygame.mixer.init()
screenx=1280
screeny=900
menu="main"
screen = pygame.display.set_mode((screenx,screeny))
pygame.display.set_caption("Brawl Ball > Heist > Siege > Gem Grab > Bounty > THE KING")
clock = pygame.time.Clock()
CARDFONT = pygame.font.Font("KINGFONT.ttf",12)
PESTFONT = pygame.font.Font("KINGFONT.ttf",20)
KINGFONT = pygame.font.Font("KINGFONT.ttf",36)
GOLMFONT = pygame.font.Font("KINGFONT.ttf",48)
RVGRFONT = pygame.font.Font("KINGFONT.ttf",60)
cardstoupgrade=[2,4,10,20,50,100,200,400,800,1000,2000,5000,6969]

chest_images={
    "SilverChest":pygame.transform.scale(pygame.image.load("SilverChest.png"),(120,120)),
    "GoldenChest":pygame.transform.scale(pygame.image.load("GoldenChest.png"),(120,120)),
    "GiantChest":pygame.transform.scale(pygame.image.load("GiantChest.png"),(160,160)),
    "MagicalChest":pygame.transform.scale(pygame.image.load("MagicalChest.png"),(160,160)),
    "EpicChest":pygame.transform.scale(pygame.image.load("EpicChest.png"),(160,160)),
    "LegendaryChest":pygame.transform.scale(pygame.image.load("LegendaryChest.png"),(160,160)),
    "MegaLightningChest":pygame.transform.scale(pygame.image.load("MegaLightningChest.png"),(160,160)),
    }
cardimage=pygame.transform.scale(pygame.image.load("allcards_01_10x10.png"),(600,720))
cardimagedimensions=[10,10]
displayonthatprofilescreengapbetweencards=[20,40]
startypositionofcardsonscreen=100
individualcardsize=[cardimage.get_width()//cardimagedimensions[0],cardimage.get_height()//cardimagedimensions[1]]

leagueimages=pygame.transform.scale(pygame.image.load("league_badges.png"),(600,60))
kinglevel=pygame.transform.scale(pygame.image.load("kinglevel.png"),(60,60))
donations=pygame.transform.scale(pygame.image.load("donations.png"),(60,60))
wins=pygame.transform.scale(pygame.image.load("wins.png"),(60,60))


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

player_loaded=False
playername="BULL API"
cards=[]
collection={}
current_deck_02=[]
playerstats={"level":0,"trophies":0,"donations":0,"wins":0}
playertypetext=""

annoyusertime=0.0
cardscroll=0
maxcardscroll=cardimage.get_height()+displayonthatprofilescreengapbetweencards[1]*(cardimagedimensions[1])-screen.get_height()+startypositionofcardsonscreen

profilebutton=GOLMBUTTON(screen,pygame.Rect(0,0,400,450),(156,80,243),KINGFONT)
chestbutton=GOLMBUTTON(screen,pygame.Rect(0,450,400,450),(156,80,243),KINGFONT)
decksbutton=GOLMBUTTON(screen,pygame.Rect(880,0,400,450),(156,80,243),KINGFONT)
backbutton=GOLMBUTTON(screen,pygame.Rect(50,50,150,50),(240,80,49),KINGFONT,"Go Back",textcolor=(85,255,85))
backbutton_01=GOLMBUTTON(screen,pygame.Rect(0,0,100,30),(240,80,49),PESTFONT,"Go Back",textcolor=(85,255,85))
loadbutton=GOLMBUTTON(screen,pygame.Rect(565,300,150,40),(255,3,204),KINGFONT,"Load!",textcolor=(240,80,49))
playertag=text_input_box(screen,pygame.Rect(530,200,260,70),(142,155,229),KINGFONT)

menu_names=["main","chests","decks","rg", "profile"]
background_files=["backround.png","chestbackround.png","ELIXIR_GOLM.png","error_02.png", "Clash-Royale-overview-min.jpg"]
backgrounds={}
for x in range(len(menu_names)):
    backgrounds[menu_names[x]]=pygame.Surface((screen.get_width(),screen.get_height()),pygame.SRCALPHA)
    backgrounds[menu_names[x]].blit(pygame.transform.scale(pygame.image.load(background_files[x]),(1280,900)),(0,0))
BULL=pygame.transform.scale(pygame.image.load("BUL_API.png"),(400,400))

description_03=textbox.ravager(screen,"",pygame.Rect(25,675,350,200),PESTFONT,color=(0,0,64),textcolor=(142,155,229),scrollvalue=40)
description_03label=GOLMBUTTON(screen,pygame.Rect(25,635,350,30),(240,80,49),PESTFONT,"Rate My Profile!",textcolor=(85,255,85))

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
                    elif (profilebutton.click(pygame.mouse.get_pos())):
                        menu="profile"
                        cardscroll=0
                    elif (loadbutton.click(pygame.mouse.get_pos())):
                        if (check_tag(playertag.text)):
                            player_loaded=True#some information is not available if the player is not loaded
                            #all this information is defined when a player is loaded
                            player_info=crapi(playertag.text)
                            if (player_info.name()!=""):
                                playername=player_info.name()
                                chestcycle=player_info.chest_cycle()
                                cards=player_info.cards()
                                collection={x:[int(cards[3][x][y]) for y in range(1,5)] for x in cards[3]}
                                current_deck_02=(player_info.get_current_deck())
                                playerstats["level"]=int(player_info.level())
                                playerstats["trophies"]=int(player_info.trophies())
                                playerstats["donations"]=int(player_info.get_info(17))
                                playerstats["wins"]=int(player_info.wins())
                            #-------------------------------------------------------
                            description_03.changetext("")
                            #print (whatplayer.getplayertype(set([current_deck_02[x][0] for x in range(len(current_deck_02))]),3,"32"))
                        elif (playertag.text!=""):
                            menu="rg"
                            annoyusertime=4.5
                            kingmad_sound.play()
                        playertag.clicked=False
                        playertag.text=""
                        #make it load the player tag here
                    elif (playertag.click(pygame.mouse.get_pos())):
                        if (playertag.clicked):
                            playertag.clicked=False
                        else:
                            playertag.clicked=True
                
                elif (menu=="profile"):
                    if (description_03label.click(pygame.mouse.get_pos())):
                        if (len(cards)>4):
                            BULL_PLAYER=(whatplayer.getplayertype(cards[4]))
                            playertypetext+="Profile rating \\n Scroll down to view all \\n \\n "
                            playertypetext+="Donations \\n "+whatplayer.do_i_donate_alot(playerstats["donations"])+" \\n \\n "
                            playertypetext+="Ladder Performance \\n "+whatplayer.am_i_overleveled(playerstats["trophies"],current_deck_02)+" \\n \\n "
                            playertypetext+="Three ways to describe you as a player:"
                            for a in range(len(BULL_PLAYER)):
                                for b in range(len(BULL_PLAYER[a])):
                                    playertypetext+=(" \\n "+BULL_PLAYER[a][b])
                                if (a<len(BULL_PLAYER)-1):
                                    playertypetext+=" \\n "
                            description_03.changetext(playertypetext)
                            playertypetext=""
                        else:
                            description_03.changetext("Cannot determine information for that player tag.")

                if ((backbutton.click(pygame.mouse.get_pos()) and (menu=="chests" or menu=="decks")) or (backbutton_01.click(pygame.mouse.get_pos()) and menu=="profile")):
                    menu="main"
            
            if (event.button==4):
                if (menu=="profile"):
                    description_03.scroll("up",pygame.mouse.get_pos())

                    if (pygame.mouse.get_pos()[0]>=400 and pygame.mouse.get_pos()[1]>=startypositionofcardsonscreen):
                        cardscroll-=40
                        if (cardscroll<0):
                            cardscroll=0
            elif (event.button==5):
                if (menu=="profile"):
                    description_03.scroll("down",pygame.mouse.get_pos())

                    if (pygame.mouse.get_pos()[0]>=400 and pygame.mouse.get_pos()[1]>=startypositionofcardsonscreen):#hard coded???
                        cardscroll+=40
                        if (cardscroll>maxcardscroll):
                            cardscroll=maxcardscroll
            
        if event.type==pygame.KEYDOWN:
            if (playertag.clicked):
                playertag.addcharacter(event.key)
    
    #-----------------------------------
    screen.fill(0)

    if (menu in backgrounds.keys()):
        screen.blit(backgrounds[menu],(0,0))
    
    if (menu!="main"):
        playertag.clicked=False
    
    if (menu=="main"):
        screen.blit(BULL,(440,480))

        #best programmer ever designs state-of-the-art wall of text never seen before form of very elegant coding
        displaytextoutline(screen,"BULL API",(640,50),RVGRFONT,color=(212,91,208))
        displaytextoutline(screen,"Enter Player Tag",(640,200),KINGFONT,color=(255,3,204),align=(0,1))
        displaytextoutline(screen,"View your",(200,225),GOLMFONT,color=(212,91,208),align=(0,1))
        displaytextoutline(screen,"profile",(200,225),GOLMFONT,color=(212,91,208),align=(0,-1))
        displaytextoutline(screen,"View your",(200,675),GOLMFONT,color=(212,91,208),align=(0,1))
        displaytextoutline(screen,"upcoming chests",(200,675),GOLMFONT,color=(212,91,208),align=(0,-1))
        displaytextoutline(screen,"View popular",(1080,225),GOLMFONT,color=(212,91,208),align=(0,1))
        displaytextoutline(screen,"decks",(1080,225),GOLMFONT,color=(212,91,208),align=(0,-1))
        displaytextoutline(screen,"Coming",(1080,675),GOLMFONT,color=(212,91,208),align=(0,1))
        displaytextoutline(screen,"soon",(1080,675),GOLMFONT,color=(212,91,208),align=(0,-1))
        displaytextoutline(screen,"Current Player",(640,410),KINGFONT,color=(156,80,243),align=(0,1))
        displaytextoutline(screen,playername,(640,410),GOLMFONT,color=(156,80,243),align=(0,-1))
        
        #woah watch out there you are copying the patented very brilliant idea of text wall designed by mastermind programmer BULL_API
        pygame.draw.line(screen,(0,0,0),(0,450),(400,450),14)
        pygame.draw.line(screen,(0,207,255),(0,450),(400,450),10)
        pygame.draw.line(screen,(0,0,0),(880,450),(1280,450),14)
        pygame.draw.line(screen,(0,207,255),(880,450),(1280,450),10)
        pygame.draw.line(screen,(0,0,0),(400,0),(400,900),14)
        pygame.draw.line(screen,(0,207,255),(400,0),(400,900),10)
        pygame.draw.line(screen,(0,0,0),(880,0),(880,900),14)
        pygame.draw.line(screen,(0,207,255),(880,0),(880,900),10)

        pygame.draw.rect(screen,(71,78,115),pygame.Rect(490,200,40,70))
        displaytextoutline(screen,"#",(510,235),GOLMFONT,color=(212,91,208))

        playertag.display()
        loadbutton.display()
    elif (menu=="chests"):
        displaychests(screen,(100,100),chestcycle)
        backbutton.display()
    elif (menu=="decks"):
        backbutton.display()
    elif (menu=="profile"):
        displaytextoutline(screen,"Card Collection",(840,45),RVGRFONT,color=(129,214,61))
        #for x in range(len(whatplayer.cardnames)):
        KING_GOLM=0
        for x in collection.keys():
            #x and y coordinates for displaying each individual card
            displayx_01=450+(individualcardsize[0]+displayonthatprofilescreengapbetweencards[0])*(KING_GOLM%10)
            displayy_01=startypositionofcardsonscreen+(individualcardsize[1]+displayonthatprofilescreengapbetweencards[1])*(KING_GOLM//10)-cardscroll
            #if the card's position+scroll values is still on the screen:
            if (displayy_01>=startypositionofcardsonscreen and displayy_01<=900-individualcardsize[1]):
                displaycard(screen,x,(displayx_01,displayy_01))
                
                #only attempt to display amount of cards if there is a valid tag
                if (player_loaded):
                    if (x in whatplayer.cardnames):
                        GOLEMRECT1=pygame.Rect(displayx_01-5,displayy_01+individualcardsize[1],individualcardsize[0]+10,displayonthatprofilescreengapbetweencards[1]-10)
                        #pygame.draw.rect(screen,(0,0,64),GOLEMRECT1)
                        currentlevel=13-collection[x][1]+collection[x][0]
                        rarity=collection[x][3]
                        cardprogress=collection[x][2]
                        cardstonext=cardstoupgrade[currentlevel-1-(13-rarity)]

                        if (cardstonext>=1000):
                            GOLMSTRING1=str(cardstonext//1000)+"k"#make the label smaller
                        else:
                            GOLMSTRING1=str(cardstonext)#totally unnecessary variable
                        
                        if (cardprogress>=cardstonext or not currentlevel<13):
                            GOLMCOLOR1=(0,255,0)
                        else:
                            GOLMCOLOR1=(0,207,255)
                        
                        GOLMCOLOR2=(255,255,255)
                        if (rarity==13):
                            GOLMCOLOR2=(160,160,160)
                        elif (rarity==11):
                            GOLMCOLOR2=(255,190,95)
                        elif (rarity==8):
                            GOLMCOLOR2=(200,135,246)
                        elif (rarity==5):
                            GOLMCOLOR2=(135,220,200)


                        displaytextoutline(screen,"Level "+str(currentlevel),GOLEMRECT1.center,CARDFONT,color=GOLMCOLOR2,align=(0,1))
                        if (currentlevel<13):
                            displaytextoutline(screen,str(cardprogress)+"/"+GOLMSTRING1,GOLEMRECT1.center,CARDFONT,color=GOLMCOLOR1,align=(0,-1))
                        else:
                            displaytextoutline(screen,"(Maxed)",GOLEMRECT1.center,CARDFONT,color=GOLMCOLOR1,align=(0,-1))
            KING_GOLM+=1

        
        
        backbutton_01.display()
        pygame.draw.rect(screen,(255,3,204),pygame.Rect(100,0,300,30))
        displaytextoutline(screen,"Player Profile",(250,15),PESTFONT,color=(129,214,61))

        for x in (description_03,description_03label):
            x.display()
        
        displayprofile(screen,(25,50),playername,playerstats)
        
        pygame.draw.line(screen,(0,0,0),(400,startypositionofcardsonscreen-10),(1280,startypositionofcardsonscreen-10),14)
        pygame.draw.line(screen,(0,207,255),(400,startypositionofcardsonscreen-10),(1280,startypositionofcardsonscreen-10),10)
        pygame.draw.line(screen,(0,0,0),(400,0),(400,900),14)
        pygame.draw.line(screen,(0,207,255),(400,0),(400,900),10)
    elif (menu=="rg"):
        print ("invalid player tag enjoy the screen")

    
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

