import json, requests, sys, random
from crapi import *
class search_clan(object):
    def __init__(self, clan_tag):
        self.clan_tag = clan_tag
        self.clan_info_raw = self.r=requests.get(f"https://api.clashroyale.com/v1/clans/%2C{self.clan_tag}/members", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE3NWMzMWZjLTM1NmQtNDY2My1iOTYzLTZmNWJhOTIwODdjZSIsImlhdCI6MTYwMTg0MTM2Miwic3ViIjoiZGV2ZWxvcGVyLzdmMjFhZGVkLTAwMTMtNDZmNC03YTMzLTYzZGJmMzAxNGFiZSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC45OC4xMTAuMTgzIl0sInR5cGUiOiJjbGllbnQifV19.b9Y4o4fVacELs-tC1CnppLZmkXFYJOcpDalBVtJT8felvE_DbT72FzW_ZRjquURZOawATea7LJRsGJbcWt-FFg"}, params = {"limit":50})
        self.clan_info = json.dumps(self.clan_info_raw.json(), indent=2)
    def clean_data(self):
        clan_info = self.clan_info.strip(']').split('items')[1].split('paging')[0]
        exclude = [32, 123, 91, 58, 34, 10, 44]
        string = ''
        clan_members = []
        for x in range(len(clan_info)):
            for i in clan_info[x]:
                if ord(i) in exclude: 
                    pass
                else:
                    string += i
        string = string.split('}')
        for x in range(0, len(string)-1, 2):
            clan_members.append([string[x].split('role')[0].split('name')[0].split('#')[1], string[x].split('role')[0].split('name')[1]])
        return(clan_members)
    def dev_stuff(self):
        try:
            with open("raw_c.txt", 'r') as r:
                test = r.read()
        except FileNotFoundError:
            with open("raw_c.txt", 'w') as r:
                r.write(self.clean_data())
    def get_members(self):
        return(self.clean_data())
    def search_card(self, dictionary, card, card_data, card_data_2):
        for x in dictionary.keys():
            if x == str(card):
                if card_data[x] == '13':
                    return(-1)
                elif card_data[x] == '9' and card_data_2[x] == '5':
                    return(str(int(dictionary[x])-1))
                else: 
                    return(dictionary[x])
        #print(f'{card} Can not be Found Inside of the Data')
        return('0')
    def get_members_card_info(self, card):
        card_amounts = {}
        for x in range(len(self.get_members())):
            player_object = crapi(self.get_members()[x][0])
            card_amounts[player_object.name()[0:15]] = self.search_card(change_format(player_object.cards()[3], 3), card, change_format(player_object.cards()[3], 1), change_format(player_object.cards()[3], 4))
        return(card_amounts)
    def get_card_amounts(self, card):
        return(self.get_members_card_info(card))
if __name__ == "__main__":
    testing = crapi('8QCJRCL')
    test = search_clan(testing.clan()[1].strip('#'))
    print(test.get_card_amounts('Arrows'))
