import sqlite3
import urllib
import re
import string

combi = dict()

# Open the output database and create empty tables
conn = sqlite3.connect('hairy.sqlite')
conn.text_factory = str
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Students ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Students 
    (id INTEGER PRIMARY KEY, hair TEXT, eye TEXT, sex TEXT, freq INTEGER)''')

# Open the csv file

fhand = open('HairEyeColor.csv')
for line in fhand:
        #create empty list
        row = list()
        newrow = list()
        #get each line sec
        line = line.rstrip()
        print line
        #get rid of comma
        delimiter = ','
        row = line.split(delimiter)
        print row[0]
        #get rid of header lines
        if row[0] == '""': continue
        print row[0]
        #get rid of ""
        for i in row:
                i = i.translate(None, string.punctuation)
                newrow.append(i)
        print newrow
        print newrow[1]
        # write stuff row per row to dbase
        cur.execute('INSERT INTO Students (id, hair, eye, sex, freq) VALUES ( ?, ?, ?, ?, ? )', (newrow[0], newrow[1], newrow[2], newrow[3], newrow[4]))
        conn.commit()


cur.close()

