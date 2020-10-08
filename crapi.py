import json, requests, sys
class error(Exception):
    pass
def check_tag(tag):
    check_url = requests.get(f"https://api.clashroyale.com/v1/players/%2C{tag}", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
    if "notFound" not in json.dumps(check_url.json(), indent = 2):
        return(True)
    print(f'{tag} is not a valid tag') #work of exception
class crapi(object):
    def __init__(self, tag):
        self.tag = tag
        self.r=requests.get(f"https://api.clashroyale.com/v1/players/%2C{tag}", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
        #self.cs=requests.get(f"https://api.clashroyale.com/v1/cards", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
        self.c=r=requests.get(f"https://api.clashroyale.com/v1/players/%2C{tag}/upcomingchests", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
        self.stats = json.dumps(self.r.json(), indent = 2)
        #self.cards = json.dumps(self.cs.json(), indent = 2)
        self.chests = json.dumps(self.c.json(), indent = 2).split('\n')
        print(f'Welcome {self.name()}!')
    def get_info(self, index):
        #try:
        stat = (((self.stats.split('\n')).pop(index)).strip()).split(':')[1].strip()[:-1].strip('"')
        #except IndexError:
            #sys.exit()
        return(stat)
    def developer_tools(self):
        '''
        try:
            stat = ((self.stats.split('\n')).pop(index))#.strip()).split(':')[1].strip()[:-1].strip('"')
        except IndexError:
            print(f'{tag} is not a valid tag')
            sys.exit()
        '''
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
        return(self.get_info(22))
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
        card_collection = player_info.stats.split('],')[2]+player_info.stats.split('],')[3]
        favourite_card = player_info.stats.split('],')[4]
        card_list = {}#format: name: [id, lvl, max lvl, quantity, image url]
        cards = ''
        self.exclude = [32, 123, 91, 58, 34, 10, 44]
        card_levels = []
        #use chest cycle json interpreter
        #print(card_collection)
        for x in range(len(card_collection)):
            for i in card_collection[x]:
                if ord(i) in self.exclude: 
                    pass
                else:
                    cards += i
        cards = list(filter(None, cards.split('}'))) 
        #string = string[0:2]
        for x in range(len(cards)):
            card_name = cards[x].split('id')[0].split('name')[1]
            card_id = cards[x].split('id')[1].split('level')[0]
            card_level = cards[x].split('level')[1].split('maxLevel')[0]
            card_max_level = cards[x].split('maxLevel')[1].split('count')[0]
            card_quantity = cards[x].split('count')[1].split('iconUrl')[0]
            card_url = cards[x].split('medium')[1]
            #print(string_name, string_id, string_level, string_max_level, string_quantity, string_url)
            #make dictionary
            card_list[card_name] = [card_id, card_level, card_max_level, card_quantity, card_url]
        #print(card_list)
        #print(string) 
        #lists = [1,4,52,2,6]
        #print(sorted(lists))
        for x in card_list.keys():
            card_levels.append(13-int(card_list[x][2])+int(card_list[x][1].split('s')[0]))
            #print(card_list[x])
            #print(sorted(card_list[x]))
        card_levels = sorted(card_levels, reverse=True)
        #print(card_levels)
        #print(round(sum(card_levels[0:32])/32, 2))
        print({k: v for k, v in sorted(card_list.items(), key=lambda item: item[1])})
        '''
        ##################################
        list_test = []
        self.exclude = [32, 123, 91, 58, 34]
        string = ''
        chest_dictionary = []
        for x in range(0, len(card_collection), 2):
            try:
                list_test.append((card_collection[x]+card_collection[x+1]).strip(','))
            except IndexError:
                print(f'{self.tag} is not a valid tag')
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
        ##########################################
        '''
        #return(card_list)
    #def create_deck(self): #add a custom url generator for app
def generate_url(card_ids):
    url = 'https://link.clashroyale.com/deck/en?deck='
    for x in range(len(card_ids)):
        url += str(card_ids[x])+';'
    return(url)
if __name__ == "__main__":
    #if check_tag('JU0GQ8') == True:
        #player_info = crapi('JU0GQ8')
    tagz = '882J2GPL'
    if check_tag(tagz) == True:
        player_info = crapi(tagz)
        #print(player_info.clan())
        player_info.developer_tools()
        import random
        def choose_random_time():
            return(f'{str(random.randint(0,1))}:{str(random.randint(0,5))}{str(random.randint(0,9))}:00')
        #print(choose_random_time())
        #print(generate_url([29039, 2309409, 3240402343j, 2034930294, 30482042834309j]))
        #print(player_info.chest_cycle())
        print(player_info.cards())
        #print(player_info.)
        #print(f'Welcome {player_info.name()} at {player_info.trophies()}')







































'''
if __name__ == "__main__" and not 69:
    import json, requests, sys
    try:
        tag = open("tag.txt", 'r').read()
    except FileNotFoundError:
        tag = input('What is your tag? ')
        open("tag.txt", 'w').write(tag)
    tag = 'JU0GQ8'
    r=requests.get(f"https://api.clashroyale.com/v1/players/%2C{tag}", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
    stats = json.dumps(r.json(), indent = 2)
    def get_stat(index):
        try:
            stat = (((stats.split('\n')).pop(index)).strip()).split(':')[1].strip()[:-1].strip('"')
        except IndexError:
            print(f'{tag} is not a valid tag')
            sys.exit()
        return(stat)
    print(f'Welcome {get_stat(2)}!')
    c=r=requests.get(f"https://api.clashroyale.com/v1/players/%2C{tag}/upcomingchests", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
    chests = json.dumps(c.json(), indent = 2).split('\n')
    list_test = []
    for x in range(0, len(chests), 2):
        list_test.append((chests[x]+chests[x+1]).strip(','))
    exclude = [32, 123, 91, 58, 34]
    string = ''
    for x in range(len(list_test)):
        for i in list_test[x]:
            if ord(i) in exclude: 
                pass
            else:
                string += i
    string = string.split('}')
    chest_dictionary = []
    for x in range(len(string)-2):
        chest_dictionary.append([int(string[x].split('name')[0].strip('index items')), string[x].split('name')[1]])
    print(dict(chest_dictionary))if __name__ == "__main__" and not 69:
    import json, requests, sys
    try:
        tag = open("tag.txt", 'r').read()
    except FileNotFoundError:
        tag = input('What is your tag? ')
        open("tag.txt", 'w').write(tag)
    tag = 'JU0GQ8'
    r=requests.get(f"https://api.clashroyale.com/v1/players/%2C{tag}", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
    stats = json.dumps(r.json(), indent = 2)
    def get_stat(index):
        try:
            stat = (((stats.split('\n')).pop(index)).strip()).split(':')[1].strip()[:-1].strip('"')
        except IndexError:
            print(f'{tag} is not a valid tag')
            sys.exit()
        return(stat)
    print(f'Welcome {get_stat(2)}!')
    c=r=requests.get(f"https://api.clashroyale.com/v1/players/%2C{tag}/upcomingchests", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
    chests = json.dumps(c.json(), indent = 2).split('\n')
    list_test = []
    for x in range(0, len(chests), 2):
        list_test.append((chests[x]+chests[x+1]).strip(','))
    exclude = [32, 123, 91, 58, 34]
    string = ''
    for x in range(len(list_test)):
        for i in list_test[x]:
            if ord(i) in exclude: 
                pass
            else:
                string += i
    string = string.split('}')
    chest_dictionary = []
    for x in range(len(string)-2):
        chest_dictionary.append([int(string[x].split('name')[0].strip('index items')), string[x].split('name')[1]])
    print(dict(chest_dictionary))if __name__ == "__main__" and not 69:
    import json, requests, sys
    try:
        tag = open("tag.txt", 'r').read()
    except FileNotFoundError:
        tag = input('What is your tag? ')
        open("tag.txt", 'w').write(tag)
    tag = 'JU0GQ8'
    r=requests.get(f"https://api.clashroyale.com/v1/players/%2C{tag}", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
    stats = json.dumps(r.json(), indent = 2)
    def get_stat(index):
        try:
            stat = (((stats.split('\n')).pop(index)).strip()).split(':')[1].strip()[:-1].strip('"')
        except IndexError:
            print(f'{tag} is not a valid tag')
            sys.exit()
        return(stat)
    print(f'Welcome {get_stat(2)}!')
    c=r=requests.get(f"https://api.clashroyale.com/v1/players/%2C{tag}/upcomingchests", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
    chests = json.dumps(c.json(), indent = 2).split('\n')
    list_test = []
    for x in range(0, len(chests), 2):
        list_test.append((chests[x]+chests[x+1]).strip(','))
    exclude = [32, 123, 91, 58, 34]
    string = ''
    for x in range(len(list_test)):
        for i in list_test[x]:
            if ord(i) in exclude: 
                pass
            else:
                string += i
    string = string.split('}')
    chest_dictionary = []
    for x in range(len(string)-2):
        chest_dictionary.append([int(string[x].split('name')[0].strip('index items')), string[x].split('name')[1]])
    print(dict(chest_dictionary))
'''




'''

def get_stat(index):
    try:
        stat = (((stats.split('\n')).pop(index)).strip()).split(':')[1].strip()[:-1].strip('"')
    except IndexError:
        print(f'{tag} is not a valid tag')
        sys.exit()
    return(stat)

def chest_cycle(tags):
    tag = tags
    r=requests.get(f"https://api.clashroyale.com/v1/players/%2C{tag}", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
    stats = json.dumps(r.json(), indent = 2)
    
    #print(f'Welcome {get_stat(2)}!')
    c=r=requests.get(f"https://api.clashroyale.com/v1/players/%2C{tag}/upcomingchests", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
    chests = json.dumps(c.json(), indent = 2).split('\n')
    list_test = []
    for x in range(0, len(chests), 2):
        try:
            list_test.append((chests[x]+chests[x+1]).strip(','))
        except IndexError:
            print(f'{tag} is not a valid tag')
            sys.exit()
    exclude = [32, 123, 91, 58, 34]
    string = ''
    for x in range(len(list_test)):
        for i in list_test[x]:
            if ord(i) in exclude: 
                pass
            else:
                string += i
    string = string.split('}')
    chest_dictionary = []
    for x in range(len(string)-2):
        chest_dictionary.append([int(string[x].split('name')[0].strip('index items')), string[x].split('name')[1]])
    return(dict(chest_dictionary))
'''
'''
#r=requests.get(f"https://api.clashroyale.com/v1/players/%2C8QCJRCL", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":20})
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)
#print(type(decoded_hand))
#c = requests.get('https://jsonplaceholder.typicode.com/todos')
#print(json.dumps(c.json()))
'''