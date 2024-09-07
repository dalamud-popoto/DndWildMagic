# Wild Surge - Roll from the Wild Magic table

This code is based on the Wild Magic tables from *Dungeons & Dragons 5e*.

Both Wild Magic tables are sourced from http://dnd5e.wikidot.com/. If you want to update the tables, run the script `get_wild_magic.py` from the `utils` folder.

There are to options for rolling the dice:

* Use the **GUI**: This version only has the Barbarian table implemented. Run `gui_barbarian_wild_surge.py` to use it.
 
* Use the **webapp**: Extremly simple interface, but it has options for both the Barbarian and Sorcerer tables. Use the following command to run the web app: 
```
python -m flask run
```


**Warning**: This code was created as part of my training with Python. Json versions of the Wild Magic tables are provided in case the source website changes after the creation of this code.