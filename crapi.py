import json, requests, sys, random
MAX_LEVEL=14
def check_tag(tag):
    check_url = requests.get(f"https://api.clashroyale.com/v1/players/%23{tag}", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
    if "notFound" not in json.dumps(check_url.json(), indent = 2):
        return(True)
    print(f'{tag} is not a valid tag')
class crapi(object):
    def __init__(self, tag):
        self.tag = tag
        self.r=requests.get(f"https://api.clashroyale.com/v1/players/%23{tag}", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
        self.c=r=requests.get(f"https://api.clashroyale.com/v1/players/%23{tag}/upcomingchests", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
        self.stats = json.dumps(self.r.json(), indent = 2)
        self.chests = json.dumps(self.c.json(), indent = 2).split('\n')
    def get_info(self, index):
        if (index==21 or index==22):
            if (len(["69" for x in self.stats.split('\n')[20:22] if "clan" in x.strip(" ")])>0):
                return (((self.stats.split('\n')).pop(index)).strip()).split(':')[1].strip()[:-1].strip('"')
            else:
                return "No Clan"
        stat = (((self.stats.split('\n')).pop(index)).strip()).split(':')[1].strip()[:-1].strip('"')
        return(stat)
    def developer_tools(self):
        try:
            open('raw.txt', 'r')
        except FileNotFoundError:
            with open('raw.txt', 'w') as raw:
                raw.write(self.stats)
    def name(self):
        return(self.get_info(2))
    def level(self):
        return(self.get_info(3))
    def clan(self):
        return(self.get_info(22), self.get_info(21))
    def trophies(self):
        return(self.get_info(5))
    def wins(self):
        return(self.get_info(6))
    def chest_cycle(self):
        list_test = []
        self.exclude = [32, 123, 91, 58, 34]
        string = ''
        chest_dictionary = []
        for x in range(0, len(self.chests), 2):
            try:
                list_test.append((self.chests[x]+self.chests[x+1]).strip(','))
            except IndexError:
                print(f'{tag} is not a valid tag')
                sys.exit()
        for x in range(len(list_test)):
            for i in list_test[x]:
                if ord(i) in self.exclude: 
                    pass
                else:
                    string += i
        string = string.split('}')
        for x in range(len(string)-2):
            chest_dictionary.append([int(string[x].split('name')[0].strip('index items')), string[x].split('name')[1]])
        return(dict(chest_dictionary))
    def cards(self):
        card_collection = self.stats.split('],')[2]+self.stats.split('],')[3]#you put player_info.stats.split here but i think it should be self.stats.split
        favourite_card = self.stats.split('],')[4]
        card_list = {}
        best32cards=[]
        bestamount=20
        cards = ''
        self.exclude = [32, 123, 91, 58, 34, 10, 44]
        card_levels = []
        for x in range(len(card_collection)):
            for i in card_collection[x]:
                if ord(i) in self.exclude: 
                    pass
                else:
                    cards += i
        #############################
        cards = list(filter(None, cards.split('}'))) 
        if ("currentDeck" in cards):
            cards.remove("currentDeck")
        for x in range(len(cards)):         
            card_name = cards[x].split('id')[0].split('name')[1]
            card_id = cards[x].split('id')[1].split('level')[0]
            card_level = cards[x].split('level')[1].split('maxLevel')[0].split("s")[0]
            card_max_level = cards[x].split('maxLevel')[1].split('count')[0]
            card_quantity = cards[x].split('count')[1].split('iconUrl')[0]
            card_url = cards[x].split('medium')[1]

            card_level=str(MAX_LEVEL-int(card_max_level)+int(card_level))
            rarity=str(card_max_level)
            card_max_level=str(MAX_LEVEL)
            if ("RamR" in card_name):
                card_name="RamRider"
            elif ("HogR" in card_name):
                card_name="HogRider"
            card_list[card_name] = [card_id, card_level, card_max_level, card_quantity, rarity, card_url]
        for x in card_list.keys():
            card_levels.append(MAX_LEVEL-int(card_list[x][2])+int(card_list[x][1].split('s')[0]))#, card_list[x])#why is this here?
            if ("RamR" in x):
                best32cards.append(["RamRider",card_levels[-1]])
            elif ("HogR" in x):
                best32cards.append(["HogRider",card_levels[-1]])
            else:
                best32cards.append([x,card_levels[-1]])
        #################################
        card_levels = sorted(card_levels, reverse=True)
        amount = 20
        top_32_average = (round(sum(card_levels[0:bestamount])/bestamount, 2))
        average = (round(sum(card_levels)/len(card_levels), 2))
        raw = {k: v for k, v in sorted(card_list.items(), key=lambda item: int(item[1][1]),reverse=True)}
        card_list=dict(raw)
        maxed_cards=([best32cards[x] for x in range(len(best32cards)) if best32cards[x][1]==MAX_LEVEL])
        if (len(maxed_cards)>bestamount):
            random.shuffle(maxed_cards)
            sortedbest32cards=maxed_cards[:bestamount]        
        else:
            best32cards.sort(key=lambda x:x[1])
            sortedbest32cards=best32cards[::-1][:bestamount]
        return(card_levels, top_32_average, average, card_list,set([x[0] for x in sortedbest32cards]))
    #def create_deck(self): #add a custom url generator for app
    def get_current_deck(self):
        raw_current_deck = self.stats.split('currentDeck')[1].split('currentFavouriteCard')[0]
        less_raw_current_deck = ''
        self.exclude = [32, 123, 91, 58, 34, 10, 44]
        card_list = self.cards()[3]
        current_deck = {}
        current_deck_01=[]
        for x in range(len(raw_current_deck)):
            for i in raw_current_deck[x]:
                if ord(i) in self.exclude: 
                    pass
                else:
                    less_raw_current_deck += i
        less_raw_current_deck = less_raw_current_deck.split('}}')[0:-1]
        ######################
        for x in range(len(less_raw_current_deck)):
            card_name = less_raw_current_deck[x].split('name')[1].split('id')[0]
            if ("RamR" in card_name):
                card_name="RamRider"
            elif ("HogR" in card_name):
                card_name="HogRider"
            current_deck[card_name] = card_list[card_name]
            current_deck_01.append([card_name,MAX_LEVEL-int(card_list[card_name][2])+int(card_list[card_name][1].split("s")[0])])
        ######################
        return(current_deck_01)
    def get_current_deck_url(self):
        return(generate_url(convert_id(self.get_current_deck()[0])))
def convert_id(dictionary):
    converted_ids = []
    for x in dictionary:
        converted_ids.append(dictionary[x][0])
    return(converted_ids)
def generate_url(card_ids):
    url = 'https://link.clashroyale.com/deck/en?deck='
    for x in range(len(card_ids)):
        url += str(card_ids[x])+';'
    return(url)
def change_format(inp, index):
    new_dict = {}
    for x in inp.keys():
        new_dict[x] = inp[x][index]
    return(new_dict)
if __name__ == "__main__":
    tag = '8QCJRCL' 
    #tag = '2QJCJPR0J'
    if check_tag(tag) == True:
        player_info = crapi(tag)
        player_info.developer_tools()
        change_format(player_info.cards()[3], 3)
