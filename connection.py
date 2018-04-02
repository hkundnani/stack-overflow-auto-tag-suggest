# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 15:53:45 2018

@author: Ankita
"""

#Make connection with postgesql

import psycopg2

try:
    conn = psycopg2.connect("dbname='stackoverflow' user='Ankita' host='localhost' password='aj1312AJ'")
    cur = conn.cursor()
    
    print("Connection created")
    cur.execute("select count(id) from posts limit 5")
    print("selected ids")
    print(cur.rowcount)
    row = cur.fetchone()
    while row is not None:
        print(row)
        row = cur.fetchone()
    cur.close()
    conn.close()
except (Exception, psycopg2.DatabaseError) as error:
        print(error)