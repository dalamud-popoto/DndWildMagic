import tkinter as tk
from random import randint as rand
from utils.wild_magic_utils import barbarian_table

def roll_dice():
    dice = rand(1,8)
    magic_effect["text"] = barbarian_table[str(dice)]
    dice_value["text"] = f"{dice}"
    return 



if __name__ == "__main__":

    window = tk.Tk()


    window.rowconfigure(2,minsize=400,weight=1)
    window.columnconfigure([0,1,2],minsize=300,weight=1)

    message = tk.Label(master=window,text = 'Check your Wild Magic effect!')
    message.grid(row=0,column=1)

    button = tk.Button(master=window,text='Roll',
    width=10, height=3,command=roll_dice )
    button.grid(row=1,column=0)

    dice_value = tk.Message(master=window,text='0')
    dice_value.grid(row=1,column=1)

    magic_effect = tk.Message(master=window,text='-')
    magic_effect.grid(row=1,column=2)
    window.mainloop() 