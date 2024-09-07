from random import randint as rand
import json



with open('barbarian_table.json','r') as f:
    barbarian_table = json.load(f)

with open('sorcerer_table.json','r') as f:
    sorcerer_table = json.load(f)



def roll_dice(job_table='barbarian'):
    """Function to roll the dice for the requested wild magic table"""
    if job_table == 'barbarian':
        dice = rand(1,8)
        dice_value = f"{dice}"        
        magic_effect = barbarian_table[str(dice)]
    elif job_table == 'sorcerer':
        dice = rand(0,99)
        dice_value = f"{dice}"    
        magic_effect = sorcerer_table[str(dice)]
    

    effect_result = {'dice': dice_value, 'magic_effect': magic_effect,'job': job_table}
    return effect_result
