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

tag_arg = sys.argv[1]
clip_arg = sys.argv[2]

cur=conn.cursor()

try:
	cur.execute("INSERT INTO tags (tag) values (%s)",[tag_arg])
except:
	print "Tag exists!"
	cur.execute("ROLLBACK")

cur=conn.cursor()
cur.execute("SELECT tag_key FROM tags WHERE tag = %s",[tag_arg])

insert_tag = cur.fetchone()[0]

cur.execute("SELECT clip_key FROM clips WHERE youtube_clip = %s",[clip_arg])

insert_clip = cur.fetchone()[0]

cur.execute("INSERT INTO tagmap (tag_key,clip_key) values (%s,%s)",[insert_tag,insert_clip])

conn.commit()
