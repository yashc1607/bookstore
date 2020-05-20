# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:08:44 2020

@author: yash
"""

import psycopg2


def create():
    conn = psycopg2.connect("dbname='lb' user='postgres' password='password'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE book(id SERIAL PRIMARY KEY,title TEXT,author TEXT,year INTEGER, isbn INTEGER)")

    conn.commit()
    conn.close()

def insert(itm,author,quantt,prc):
    conn = psycopg2.connect("dbname=lb user=postgres password=imbatman")
    cur = conn.cursor()
    query="INSERT INTO book (title,author,year,isbn) VALUES (%s,%s,%s,%s)"
    data=(itm,author,quantt,prc)
    #if cur.execute("INSERT INTO book (title,year,author,isbn) VALUES (%s,%s,%s,%s)",(itm,author,quantt,prc)):
    cur.execute(query,data)
    conn.commit()
    
        
    conn.close()

    
def view():
    conn = psycopg2.connect("dbname=lb user=postgres password=imbatman")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    #print(rows)
    conn.close()
    return rows
    
def search(title="",author="",year=0,isbn=0):
    conn = psycopg2.connect("dbname=lb user=postgres password=imbatman")
    cur = conn.cursor()
    q="SELECT * FROM book WHERE title=%s OR author=%s OR year=%s OR isbn=%s"
    cur.execute(q,(title,author,year,isbn))
    rows=cur.fetchall()
    #print(rows)
    conn.close()
    return rows

def update(id,title,author,year,isbn):
    conn = psycopg2.connect("dbname=lb user=postgres password=imbatman")
    cur = conn.cursor()
    up_q="UPDATE book set year=%s,isbn=%s,title=%s,author=%s WHERE id=%s"
    cur.execute(up_q,(year,isbn,title,author,id))
    conn.commit()
    conn.close()
    

def delete(id):
    conn = psycopg2.connect("dbname=lb user=postgres password=imbatman")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=%s",(id,))
    conn.commit()
    conn.close()
    


#create()
#insert('aad','bc',252,123)
#print(search(author='bb'))

#update("aa","bb",25,12,1)
#title="lgh"
#delete(5)

#view()
    
"""
conn = psycopg2.connect("dbname=lb user=postgres password=imbatman")
cur = conn.cursor()
cur.execute("DROP TABLE book")
conn.commit()"""

"""
conn = psycopg2.connect("dbname=lb user=postgres password=imbatman")
cur = conn.cursor()
cur.execute("ALTER TABLE book ADD COLUMN id SERIAL PRIMARY KEY")
conn.commit()"""




