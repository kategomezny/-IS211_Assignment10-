#!/usr/bin/python

# -*- coding: utf-8 -*-

"""Connects and query the data"""



import sqlite3 as lite



con = lite.connect('pets.db')





while True:

        person_ID= raw_input("Please enter your ID number or enter -1 to exit:")

        if person_ID == '-1':

            print 'Exiting Database Query.'

            raise SystemExit



    

        cur = con.cursor() 

        

        

        cur.execute( "SELECT person.first_name || ' ' || person.last_name|| ', '|| person.age\

                    ||' years old and owns ' FROM person WHERE person.id=" + person_ID)

        results =  cur.fetchone()

        print results

        

        

        

        cur.execute( "SELECT  pet.name || ', a ' || pet.breed || ', that is ' || pet.age || ' years old'\

                FROM person INNER JOIN person_pet ON (person.id = person_pet.person_id) \

                INNER JOIN pet ON (person_pet.pet_id = pet.id) WHERE person.id=" + person_ID)

        results =  cur.fetchall()

        print results


