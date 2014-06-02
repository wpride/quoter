#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2
import sys, getopt
from collections import defaultdict

try:
    conn = psycopg2.connect("dbname='wpride1' user='wpride1' host='localhost' password='123'")
except:
    print "I am unable to connect to the database"

countmap = defaultdict(int)

cur=conn.cursor()

iterargs = iter(sys.argv)
next(iterargs)

for elem in iterargs:
	print "elem: " +  elem

	cur.execute("SELECT tag_key FROM tags WHERE tag = %s",[elem])
	rows=cur.fetchall()
	t_key = rows[0]
	cur.execute("SELECT clip_key FROM tagmap WHERE tag_key = %s",[t_key])
	rows=cur.fetchall()
	for row in rows:
		print "	", row[0]
		countmap[row[0]] += 1

x = max(countmap.values())

cur.execute("SELECT youtube_clip FROM clips WHERE clip_key = %s",[x])
rows = cur.fetchall()

print "https://www.youtube.com/watch?v=" + rows[0][0]

#conn.commit()
