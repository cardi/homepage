#!/usr/bin/env python3

#
# homepage - a default portal for your web browser
#
# Written in 2018 by Calvin Ardi <calvin@isi.edu>
#
# To the extent possible under law, the author(s) have dedicated all
# copyright and related and neighboring rights to this software to the
# public domain worldwide. This software is distributed without any
# warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication
# along with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
#

#
# usage: ./generate.py input.yaml
# outputs HTML chunks to stdout
#

import sys, select
import yaml

if __name__ == '__main__':

  # grab yaml from stdin, filename, or use default
  filename = None
  stdin = None
  if select.select([sys.stdin,],[],[],0.0)[0]:
    stdin = sys.stdin.read()
  elif len(sys.argv) > 1:
    # not checking or sanitizing input
    filename = sys.argv[1]
  else:
    filename = 'index.yaml'

  # try loading the file from stdin or filename
  if stdin:
    data = yaml.safe_load(stdin)
  elif filename:
    try:
      with open(filename) as f:
        # assuming valid yaml
        data = yaml.safe_load(f)
    except (NameError, IOError, FileNotFoundError) as e:
      print("error loading file: %s" % e, file=sys.stderr)
      sys.exit(1)

  # build index.yaml and print to stdout
  numCategory = 0
  for category in data:
    print('<div class="box %d">' % numCategory)
    print('<a nohref><h3>%s</h3></a>' % category)
    # iterate through arrays of dictionaries
    for entry in data[category]:
      # entry is a dict {"name": "url"}
      for urls in entry:
        print('<a href="%s">%s</a><br>' % (entry[urls], urls))
    print('</div>')
    numCategory = numCategory + 1
