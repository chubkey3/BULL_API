import random

def getplayertype(best32,top=3,hahaidontcarethatyourhousesoldormadeyoulotsofmonfy_iusedtarasgadgetstillcouldnotfindwhoaskedwernmrnwenreuwjndfjonbiudfbnjkrensdfoinweornweiornoskdnmvkcnbjklcvnbjkdrkrhjbgerjkltnrjbtidjnbiubndriutnodrngidnfgjkdnbjkcvnkbjndkjrbtjkrnbtjkebriktjberkjbntkjebnrtreterdon_t_worry_you_can_refer_to_this_as_playplaykinggolemwolf_not_what_it_actually_is="32"):
    top=min(3,top)
    description=[]
    description_01=[]
    best32=set(best32)
    
    
    for x in range(len(playertypes)-1):
        types=0.0
        types_01=""
        for y in playertypes[x]:
            matching=(len(best32&playertypes[x][y])/len(best32))
            if (matching>types):
                types=float(matching)
                types_01=y
        description.append(types_01)
    
    f2pscore=(len(best32&playertypes[2]["f2p"])/len(best32))
    p2wscore=(len(best32&playertypes[2]["p2w"])/len(best32))
    if (p2wscore-f2pscore>0.2):
        description.append("p2w")
    else:
        description.append("f2p")

    for x in range(len(description)):
        BULL=[]
        if (description[x]=="meta"):
            BULL.append("The Meta Player")
            BULL.append(random.choice([
                "You prioritize upgrading cards that are stable in the meta.",
                "You never want to be found with a bunch of high-level cards that are useless in the meta.",
                "You are always looking on the top cards section of BULL API to see which cards to upgrade next.",
                "Gold is hard to come by so you upgrade the best cards you can.",
                "You had many meta cards upgraded a long time ago knowing they would still be viable three years later.",
            ]))
        elif (description[x]=="niche"):
            BULL.append("The Niche-Card Player")
            BULL.append(random.choice([
                "You prioritize upgrading cards that work well with certain decks.",
                "You know you will stick with certain decks so you upgraded cards that work well in those decks.",
                "You upgrade cards that may fit into multiple decks but usually don't have decks built around them.",
                "You are scared about meta cards getting nerfed so you upgrade strong but not broken cards.",
                "\"ELIXIR GOLM, ELIXIR GOLM, AND MORE ELIXIR GOLM, CAN I SEE ANYTHING ELSE?!\" - you",
            ]))
        elif (description[x]=="surprise"):
            BULL.append("The Surprise Player")
            BULL.append(random.choice([
                "You like to use cards that no one would expect to see often.",
                "You like to use an unexpected deck to always keep your opponent guessing.",
                "You are bored of conventional decks and want to try something new.",
                "Your win condition is your crazy, unexpected deck, not a specific card.",
                "The moment your opponent figures out your deck, you already took a tower.",
            ]))
        elif (description[x]=="toxic"):
            BULL.append("The Toxic Player")
            BULL.append(random.choice([
                "Your highest-leveled cards are the most annoying ones in the game.",
                "You probably flex ladder wins against tops and think you are good *cough* 234 and 36beast *cough*.",
                "You spend more time emoting than actually playing the game.",
                "You stay hydrated on your opponents' tears from your toxic deck.",
                "Your win condition is your opponent rage-quitting.",
            ]))
        elif (description[x]=="spells"):
            BULL.append("The Spell Master")
            BULL.append(random.choice([
                "You upgrade spells because they are versatile and stable in the meta.",
                "You upgrade spells because they are in almost every deck so that allows you to use many decks.",
                "You can never decide which spell to use so you just upgrade all of them.",
                "Bait deck matchups are literally free wins for you.",
                "Spell damage is uncounterable, therefore spell-cycling is the best way to win the game.",
            ]))
        elif (description[x]=="chip"):
            BULL.append("The Chip-Cycle Player")
            BULL.append(random.choice([
                "Your playstyle consists of trying to get damage a little bit at a time.",
                "You can reliably take down a tower but rather slowly.",
                "Your opponent's slow reaction time is your primary source of damage.",
                "Eventually, your opponent will not be able to keep up with your constant pressure.",
                "Your strategy: \"Go up, dash, die, repeat, 8 percent at a time.\" - mortis in heist",
            ]))
        elif (description[x]=="bridge"):
            BULL.append("The Aggressive Player")
            BULL.append(random.choice([
                "Your playstyle consists of making aggressive plays at the brige.",
                "You like to have the fights happen on your opponent's side of the arena.",
                "You play cards so rapidly that your elixir bar is usually at 0 or 1.",
                "You punish so often that you don't even let golem players drop their golem without losing.",
                "Who needs towers? All you do is base race and tower trade.",
            ]))
        elif (description[x]=="bait"):
            BULL.append("The Bait Player")
            BULL.append(random.choice([
                "Your playstyle consists of trying to make the opponent waste their spells.",
                "You only care about whether your opponent has their zap, log or fireball.",
                "You play passively, but when the opponent uses a spell, you instantly unload 10 elixir.",
                "You punish those random mid-ladder decks that somehow have multiple win conditions and no spells.",
                "\"HOW DOES HE ALREADY HAVE GOBLIN BARREL AGAIN? I THOUGHT HE JUST USED IT!!!\" - your opponent",
            ]))
        elif (description[x]=="beatdown"):
            BULL.append("The Beatdown Player")
            BULL.append(random.choice([
                "Your playstyle consists of overwhelming your opponent with large pushes.",
                "You aren't afraid to take tower damage because your push is more important.",
                "Your deck thrives in double and triple elixir time.",
                "Your pushes take the opponent's towers from full health to zero in seconds.",
                "If the opponent defends your push, you win by lagging their device with (elixir) golems.",
            ]))
        elif (description[x]=="defense"):
            BULL.append("The Defender")
            BULL.append(random.choice([
                "Your playstyle consists of defending then relying on counterpushes.",
                "You love making positive elixir trades on defense.",
                "Your finger is hovering over the screen, waiting for the opponent's hog rider.",
                "At least 3 out of 5 of your wins are from tiebreakers.",
                "Dealing damage to your tower is harder than looking for who asked.",
            ]))
        elif (description[x]=="p2w"):
            BULL.append("The Pay-To-Win-Player")
            BULL.append(random.choice([
                "You probably spent a lot of money on the game, upgrading all those legendaries.",
                "You upgrade legendaries because they look cool and are unique.",
                "You want to flex your legendaries more than actually use them.",
                "\"The best card is the credit card.\" - overused joke 2016",
                "Your GitHub repository made you a fortune and now you turned it into legendaries.",
            ]))
        elif (description[x]=="f2p"):
            BULL.append("The Free-To-Play Player")
            BULL.append(random.choice([
                "You upgraded many common cards because you are probably free-to-play.",
                "You think legendaries are so overrated and commons can do the job just as well.",
                "You can get more common cards upgraded in the time that it takes to upgrade a rare or epic.",
                "You just really wanted a max card and a common would be the easiest to get.",
                "Imagine spending money on legendaries instead of emotes.",
            ]))
        description_01.append(BULL)
    return description_01

def am_i_overleveled(score,currentdeck):
    total=0
    for x in range(len(currentdeck)):
        total+=currentdeck[x][1]
    total/=max(1,len(currentdeck))
    total=max(1,total)

    if (total<9):
        trophies=10*(2.5*(total-1))**2
    elif (total<11):
        trophies=2000*(3*total-23)/(total-7)
    elif (total<13):
        trophies=4000*(total-16)/(total-15)
    else:
        trophies=6000
    trophies=int(trophies)

    text="With the levels of your deck, you should be able to reach at least "+str(trophies)+" trophies. \\n "
    
    if (score-trophies<-200):
        text+=random.choice([
            "Instead of buying chests, cards, and gold, how about buying more skill!",
            "More people uninstall the game because of you than people who uninstall because of Clan Wars II!",
            "YOU ARE SO OVERLEVELED! PLEASE UNINSTALL FOR THE SAKE OF YOUR OPPONENTS!",
        ])
    elif (score-trophies<0):
        text+=random.choice([
            "You should be able to get quite a bit higher in trophies with those card levels.",
            "Your card levels are too high for your trophy range. You have some catching up to do.",
            "Don't be that overleveled player everyone dreads facing on ladder. Get to where you should be!",
        ])
    elif (score-trophies<200):
        text+=random.choice([
            "You are at an average trophy range for your card levels but they can definitely get you higher.",
            "You are not doing too poorly but with enough skill or time, you should climb in trophies.",
            "Consider playing more ladder. Those next few trophy road rewards shouldn't be too far away for you.",
        ])
    elif (score-trophies<400):
        text+=random.choice([
            "Good job, you are doing well on ladder with your card levels.",
            "You are definitely a competent player, reaching your highest trophies with those card levels.",
            "\"Skill > Levels\" scream that at every overleveled player you face on ladder.",
        ])
    elif (score-trophies<800):
        text+=random.choice([
            "Wow, you are far above the average trophy range for your card levels!",
            "You have proven that with enough skill, the level gap can be overcome.",
            "CERTIFIED LEVEL 13 EXTERMINATOR!!!",
        ])
    else:
        text+="Congratulations on getting this high on ladder, your skill level is very impressive!"

    return text

def do_i_donate_alot(donations):
    text=""
    if (donations<5000):
        text="You are incredibly selfish. Donate more, everyone else does so why shouldn't you?"
    elif (donations<15000):
        text="Get those donations up, there is no point keeping your king tower level low."
    elif (donations<50000):
        text="Keep donating, the extra experience, gold, and star points are definitely worth it."
    elif (donations<150000):
        text="Your donations are very helpful to your clanmates. May you be rewarded with legendaries."
    else:
        text="Way to go, you probably donate more cards than you collect!"
    return text

cardnames=[
    "Arrows",           #0          F2P, Spells                     
    "Minions",          #1          F2P, Chip                       
    "Archers",          #2          F2P                             
    "Knight",           #3          F2P                             
    "Fireball",         #4          Spells                          
    "MiniP.E.K.K.A",    #5          Defense                         
    "Musketeer",        #6          Smart                           
    "Giant",            #7          Beatdown                        
    "WallBreakers",     #8          Bridge                          
    "Prince",           #9          Beatdown                        
    "BabyDragon",       #10         Beatdown                        
    "SkeletonArmy",     #11         Bait, Ladder                    
    "SpearGoblins",     #12         F2P, Chip                       
    "Goblins",          #13         F2P, Chip, Off-meta             
    "GoblinHut",        #14         Chip, Toxic                     
    "HogRider",         #15         Bridge, Ladder                  
    "GoblinBarrel",     #16         Smart, Bait                     
    "Hunter",           #17         Defense                         
    "Bomber",           #18         F2P, Off-meta                   
    "Skeletons",        #19         F2P                             
    "Tombstone",        #20         Defense                         
    "Valkyrie",         #21         Ladder                          
    "GiantSkeleton",    #22         Defense, Surprise, Off-meta     
    "Witch",            #23         Toxic, Ladder
    "Cannon",           #24         F2P, Defense
    "Barbarians",       #25         F2P, Bait
    "BarbarianHut",     #26         Chip, Toxic
    "BattleRam",        #27         Bridge
    "BarbarianBarrel",  #28         Spells
    "Golem",            #29         Bridge, Beatdown, Ladder
    "Zap",              #30         F2P, Spells
    "MinionHorde",      #31         F2P, Bait, Ladder
    "InfernoTower",     #32         Bait, Defense, Toxic
    "MegaMinion",       #33         Beatdown
    "Lightning",        #34         Beatdown
    "P.E.K.K.A",        #35         Defense
    "Miner",            #36         P2W, Chip
    "LavaHound",        #37         P2W, Beatdown
    "Bats",             #38         F2P, Bait, Chip
    "FireSpirits",      #39         F2P, Chip, Off-meta
    "Furnace",          #40         Smart, Chip, Toxic
    "Wizard",           #41         Ladder
    "Tornado",          #42         Defense, Spells
    "Poison",           #43         Spells
    "MagicArcher",      #44         P2W, Bait
    "NightWitch",       #45         P2W, Beatdown
    "Mortar",           #46         F2P, Chip
    "SkeletonBarrel",   #47         F2P, Bait, Bridge
    "Rocket",           #48         Spells
    "FlyingMachine",    #49         Chip
    "X-Bow",            #50         Chip
    "Balloon",          #51         Beatdown
    "TheLog",           #52         P2W, Spells
    "InfernoDragon",    #53         P2W, Bait
    "RoyalRecruits",    #54         F2P, Surprise, Toxic
    "RoyalGiant",       #55         F2P, Bridge, Ladder
    "RoyalHogs",        #56         Bait, Bridge
    "ThreeMusketeers",  #57         Smart, Bait
    "DarkPrince",       #58         Beatdown
    "Guards",           #59         Defense
    "MegaKnight",       #60         P2W, Ladder
    "Princess",         #61         P2W, Bait
    "GiantSnowball",    #62         F2P, Spells
    "IceSpirit",        #63         F2P, Smart
    "ElixirCollector",  #64         Smart, Surprise
    "IceGolem",         #65         Smart
    "Freeze",           #66         Surprise, Toxic
    "Bowler",           #67         Defense
    "Lumberjack",       #68         P2W, Bridge, Beatdown
    "IceWizard",        #69 haha    P2W, Defense
    "Rascals",          #70         F2P, Bait
    "GoblinGang",       #71         F2P, Smart, Bait
    "Earthquake",       #72         Off-meta
    "DartGoblin",       #73         Bait
    "GoblinGiant",      #74         Beatdown, Surprise
    "Bandit",           #75         P2W, Bridge
    "Firecracker",      #76         F2P, Off-meta
    "EliteBarbarians",  #77         F2P, Bridge, Toxic, Ladder
    "HealSpirit",       #78         Bridge
    "BombTower",        #79         Defense
    "Rage",             #80         Surprise
    "ElectroGiant",     #81         Beatdown
    "CannonCart",       #82         Surprise, Off-meta
    "RamRider",         #83         P2W, Bridge
    "Fisherman",        #84         P2W
    "Tesla",            #85         F2P, Defense
    "ElixirGolem",      #86         Smart, Beatdown, Toxic
    "Zappies",          #87         Defense, Off-meta
    "Clone",            #88         Surprise, Toxic
    "ElectroDragon",    #89         Beatdown
    "ElectroWizard",    #90         P2W, Smart
    "Sparky",           #91         P2W, Bait, Beatdown
    "SkeletonDragons",  #92         F2P
    "RoyalDelivery",    #93         F2P, Spells
    "GoblinCage",       #94         Defense
    "BattleHealer",     #95         Surprise
    "Mirror",           #96         Surprise
    "Executioner",      #97         Defense
    "RoyalGhost",       #98         P2W
    "Graveyard",        #99         P2W
]

'''
playertypes={
    "offmeta":set([cardnames[x] for x in [13,18,22,39,72,76,82,87]]),
    "smart":set([cardnames[x] for x in [6,16,40,57,63,64,65,71,86,90]]),
    "surprise":set([cardnames[x] for x in [22,54,64,66,74,80,82,88,95,96]]),
    "toxic":set([cardnames[x] for x in [14,23,26,32,40,54,66,77,86,88]]),
    "spells":set([cardnames[x] for x in [0,4,28,30,42,43,48,52,62,93]]),
    "ladder":set([cardnames[x] for x in [11,15,21,23,29,31,41,55,60,77]]),
    "chip":set([cardnames[x] for x in [1,12,13,14,26,36,38,39,40,46,49,50]]),
    "bridge":set([cardnames[x] for x in [8,15,27,29,47,55,56,68,75,77,78,83]]),
    "defense":set([cardnames[x] for x in [5,17,20,22,24,32,35,42,59,67,69,79,85,87,94,97]]),
    "bait":set([cardnames[x] for x in [11,16,25,31,32,38,44,47,53,56,57,61,70,71,73,91]]),
    "beatdown":set([cardnames[x] for x in [7,9,10,29,33,34,37,45,51,58,68,74,81,86,89,91]]),
    "p2w":set([cardnames[x] for x in [36,37,44,45,52,53,60,61,68,69,75,83,84,90,91,98,99]]),
    "f2p":set([cardnames[x] for x in [0,1,2,3,12,13,18,19,24,25,30,31,38,39,46,47,54,55,62,63,70,71,76,77,85,92,93]]),
}
'''
playertypes=[
    {
        "meta":set([cardnames[x] for x in [3,4,6,7,10,15,16,19,27,28,29,30,33,35,36,37,42,43,46,47,48,50,51,52,55,56,57,63,65,68,83,85,90,99]]),
        "niche":set([cardnames[x] for x in [0,1,2,5,8,9,12,17,20,26,32,34,38,44,45,49,53,54,58,59,60,61,62,69,70,71,73,74,75,78,79,82,84,88,89,91,92,93,94,97,98]]),
        "surprise":set([cardnames[x] for x in [11,13,18,22,24,25,31,39,64,67,72,76,80,81,87,95,96]]),
        "toxic":set([cardnames[x] for x in [14,21,23,40,41,66,77,86]]),
    },

    {
        "chip":set([cardnames[x] for x in [1,3,13,14,18,19,25,26,36,39,40,49,63,65,76,92,99]]),
        "bridge":set([cardnames[x] for x in [8,15,27,46,50,51,54,55,56,68,75,77,78,82,83,98]]),
        "bait":set([cardnames[x] for x in [11,12,16,31,32,38,41,44,47,57,61,64,70,71,73,87]]),
        "beatdown":set([cardnames[x] for x in [5,7,9,10,20,23,29,33,37,45,58,74,81,86,89,91,95]]),
        "spells":set([cardnames[x] for x in [0,4,28,30,34,42,43,48,52,62,66,72,80,88,93,96]]),
        "defense":set([cardnames[x] for x in [2,6,17,21,22,24,35,53,59,60,67,69,79,84,85,90,94,97]]),
    },

    {
        "p2w":set([cardnames[x] for x in [8,9,10,11,16,17,22,23,28,29,34,35,36,37,42,43,44,45,50,51,52,53,58,59,60,61,66,67,68,69,74,75,80,81,82,83,84,88,89,90,91,96,97,98,99]]),
        "f2p":set([cardnames[x] for x in [0,1,2,3,4,5,6,7,12,13,14,15,18,19,20,21,24,25,26,27,30,31,32,33,38,39,40,41,46,47,48,49,54,55,56,57,62,63,64,65,70,71,72,73,76,77,78,79,85,86,87,92,93,94,95]]),
    },
]

if (__name__=="__main__"):
    BULL=list(cardnames)
    random.shuffle(BULL)
    print (BULL[:32])
    print (getplayertype(BULL[:32],3,"set"))
    #print (len(playertypes[1]))