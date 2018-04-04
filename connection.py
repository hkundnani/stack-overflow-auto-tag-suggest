# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 15:53:45 2018

@author: Ankita
"""

#Make connection with postgesql

import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import datetime as dt
#
#try:
#    conn = psycopg2.connect("dbname='stackoverflow' user='' host='localhost' password=''")
#    cur = conn.cursor()
#    
#    print("Connection created")
#    cur.execute("select count(id) from posts limit 5")
#    print("selected ids")
#    print(cur.rowcount)
#    row = cur.fetchone()
#    while row is not None:
#        print(row)
#        row = cur.fetchone()
#    cur.close()
#    conn.close()
#except (Exception, psycopg2.DatabaseError) as error:
#        print(error)
try: 
    engine = create_engine('postgresql://Ankita@localhost:5432/stackoverflow')
    print("Connection Established")
    #df = pd.read_sql_query('select id, body, title, tags from "posts" where post_type_id = 1 ',con=engine)
    start = dt.datetime.now()

    def generator(engine, chunk_size, offset):
        i =0
        while True:
                p_sql = "select id, body, title, tags from posts where post_type_id = 1 limit %d offset %d" % (chunk_size, offset)
                df = pd.read_sql_query(p_sql, engine)
                print("Chunk number"+str( i))
                # don't yield an empty data frame
                if not df.shape[0]:
                    break
                yield df
    
                # don't make an unnecessary database query
                if df.shape[0] < chunk_size:
                    break
    
                offset += chunk_size
                i = i+1
                print('{} {}'.format((dt.datetime.now() - start).seconds, i*chunk_size))

                
        print("selection successfull")
    
        
        
    df_final = pd.concat(generator(engine, 100000, 0))
    df_final.to_csv("required_data.csv", encoding='utf-8', index=False)
except (Exception) as error:
    print(error)
