#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='wpride1' user='wpride1' host='localhost' password='123'")
except:
    print "I am unable to connect to the database"

cur=conn.cursor()

cur.execute("""SELECT * from tags""")

rows=cur.fetchall()

for row in rows:
	print "	", row[0]
