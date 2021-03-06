#!/usr/bin/python

"""
reducer.py - take hadoop output and simplify results
- art rhyno <http://projectconifer.ca/>

(c) Copyright GNU General Public License (GPL)
"""

import sys

# input comes from STDIN for hadoop processing
for line in sys.stdin:
    line = line.strip()
    if len(line) > 0:
       try:
          char_cnt, filename, word, x0, y0, x1, y1 = line.split('\t', 7)
          x0 = int(x0)
          y0 = int(y0)
          x1 = int(x1)
          y1 = int(y1)

          print "%s %s %d %d %d %d" % (filename,word,x0,y0,x1,y1)
       except:
          line  = ''
