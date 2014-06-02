#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2
import sys, getopt

try:
    conn = psycopg2.connect("dbname='wpride1' user='wpride1' host='localhost' password='123'")
except:
    print "I am unable to connect to the database"

clip_arg = sys.argv[1]

cur=conn.cursor()

cur.execute("INSERT INTO clips (youtube_clip) values (%s)",[clip_arg])

conn.commit()
