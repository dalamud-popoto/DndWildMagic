import requests as r 
import bs4
from random import randint as rand
import json
url_barbarian = 'http://dnd5e.wikidot.com/barbarian:wild-magic'
url_sorcerer = 'http://dnd5e.wikidot.com/sorcerer:wild-magic'

def get_wild_magic_table(url,is_barbarian=True):
    """This function retrieves the requested barbarian table from dnd5e"""
    res = r.get(url)
    res.raise_for_status()


    magic_soup = bs4.BeautifulSoup(res.text,features="html.parser")

    wild_magic_raw = magic_soup.select('table > tr > td')

    if is_barbarian:
        wild_magic_table = {wild_magic_raw[i].getText():wild_magic_raw[i+1].getText() for i in range(0,len(wild_magic_raw),2)}
    else: 
        wild_magic_table = {}
        for i in range(0,len(wild_magic_raw),2):
            dice_values = [ int(x) for x in wild_magic_raw[i].getText().split('-')]
            wild_magic_table[dice_values[0]] = wild_magic_raw[i+1].getText()
            wild_magic_table[dice_values[1]] = wild_magic_raw[i+1].getText()

    return wild_magic_table



if __name__ == "__main__":

    barbarian_table = get_wild_magic_table(url_barbarian,is_barbarian=True)
    with open('barbarian_table.json','w') as f:
        json.dump(barbarian_table,f)

    sorcerer_table = get_wild_magic_table(url_sorcerer,is_barbarian=False)

    with open('sorcerer_table.json','w') as f:
        json.dump(sorcerer_table,f)