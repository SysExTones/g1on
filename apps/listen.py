#!/usr/bin/env python

# Copyright (c) 2017
#
# This project is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This project is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.


import sys

import g1on


if __name__ == '__main__':
	if len( sys.argv ) == 2:
		i = g1on.BI( sys.argv[1] )
		while i:
			try:
				i.fill()
				if i.has_non_sysex():
					nonsysex = i.get_non_sysex()
					print( g1on.to_hex( nonsysex ) )
				if i.has_sysex():
					sysex = i.get_sysex()
					print( g1on.to_hex( sysex ) )
			except IOError as e:
				if e.errno != 11:
					print( e )
					i.close()
					i = None
	else:
		print( 'Usage: %s MIDIDEVICEFILENAME' % (sys.argv[0]) )

