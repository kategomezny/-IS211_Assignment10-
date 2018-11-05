#!/usr/bin/python

# -*- coding: utf-8 -*-

"""connects to the database in pets.db and

loads up the data  """





import sqlite3 as lite



list_person = (

    (1, 'James', 'Smith', 41),

    (2, 'Diana', 'Greene', 23),

    (3, 'Sara', 'White', 27),

    (4, 'William', 'Gibson', 23)

)



list_pet = (

    (1, 'Rusty', 'Dalmation', 4, 1),

    (2, 'Bella', 'Alaskan Malamute', 3, 0),

    (3, 'Max', 'Cocker Spaniel', 1, 0),

    (4, 'Rocky', 'Beagle', 7, 0),

    (5, 'Rufus', 'Cocker Spaniel', 1, 0),

    (6, 'Spot', 'Bloodhound', 2, 1)

)



list_person_pet = (

    (1, 1),

    (1, 2),

    (2, 3),

    (2, 4),

    (3, 5),

    (4, 6)

)

    

con = lite.connect('pets.db')



with con:

    

    cur = con.cursor()    

    

    cur.executemany("INSERT INTO person VALUES(?, ?, ?, ?)", list_person)

    cur.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", list_pet)

    cur.executemany("INSERT INTO person_pet VALUES(?, ?)", list_person_pet)
