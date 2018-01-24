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
# usage: ./convert.py bookmarks.html
# input: bookmarks.html (exported from your web browser) via stdin or
#   filename
# outputs: YAML-formatted bookmarks to stdout
# 
# example bookmarks structure (bookmarks.html):
# 
#   - Bookmarks Menu:
#     - folder:
#       - nested-folder:
#         - apple: apple.com
#       - google: google.com
#     - folder-2:
#       - example: example.com
#     - yahoo: yahoo.com
# 
# example YAML output:
# 
#   - Bookmarks Menu:
#     - yahoo: yahoo.com
#   - folder:
#     - google: google.com
#   - nested-folder:
#     - apple: apple.com
#   - folder-2:
#     - example: example.com
#

from bs4 import BeautifulSoup
import sys, select
import yaml

if __name__ == '__main__':

  # grab bookmarks from stdin, filename, or use default
  filename = None
  stdin = None
  if select.select([sys.stdin,],[],[],0.0)[0]:
    stdin = sys.stdin.read()
  elif len(sys.argv) > 1:
    # not checking or sanitizing input
    filename = sys.argv[1]
  else:
    filename = 'bookmarks.html'

  # try loading the file from stdin or filename
  if stdin:
    soup = BeautifulSoup(stdin, "html5lib")
  elif filename:
    try:
      with open(filename, encoding='utf8') as f:
        # assuming valid yaml
        soup = BeautifulSoup(f, "html5lib")
    except (NameError, IOError, FileNotFoundError) as e:
      print("error loading file: %s" % e, file=sys.stderr)
      sys.exit(1)
  else:
    # should never get here
    sys.exit(1)
 
  # process our bookmarks file 
  default_folder_name = soup.find('h1').text # "Bookmarks Menu"
  output = []

  for a in soup.find_all('a'):
    folder = None
    parent_tag = a.parent.parent.parent.parent.name
    if parent_tag == "html":
      folder = default_folder_name
    elif parent_tag == "dl":
      # XXX: if there are multiple folders with the same name (but in
      # different parts of the hierarchy), this script puts all of those
      # bookmarks in to the same folder.
      folder = a.parent.parent.parent.parent.dt.h3.text

    entry = dict({a.text: a['href']})

    b = list(filter(lambda x: folder in x.keys(), output))
    if b: 
      # folder exists => append our entry
      b[0][folder].append(entry)
    else:
      # folder doesn't exist => create a new entry
      output.append( dict({folder: [ entry ] }) )

  print(yaml.dump(output, default_flow_style=False).strip())
