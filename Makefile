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

M4=m4

index.html: index.yaml
	$(M4) -D_content='$(shell python3 generate.py)' index.m4 > index.html

.PHONY:	all clean

all: index.html

local:
	test ! -s Makefile.local || make --always-make -f Makefile.local

clean:
	rm -f index.html
