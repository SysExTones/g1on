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


def process_data( filename, prefix, postfix ):
	i = g1on.BI( sys.argv[1] )
	while i:
		try:
			i.fill()
			if i.has_non_sysex():
				nonsysex = i.get_non_sysex()
			if i.has_sysex():
				sysex = i.get_sysex()
				if g1on.is_patch( sysex ):
					data = g1on.get_patch( sysex )
					patchnumber = data[0]
					patch = data[3:131]
					g1on.PatchOutputFile( '%s.%02i.%s' % (prefix, patchnumber, postfix), patch )
					g1on.PatchOutputTextFile( '%s.%02i.%s.txt' % (prefix, patchnumber, postfix), patch )
		except IOError as e:
			if e.errno != 11:
				print( e )
				i.close()
				i = None



if __name__ == '__main__':
	argc = len( sys.argv )
	if argc >= 2:
		prefix = 'patch'
		if argc >= 3:
			prefix = sys.argv[2]
		postfix = 'g1on'
		if argc >= 4:
			postfix = sys.argv[3]
		process_data( sys.argv[1], prefix, postfix )
	else:
		print( 'Usage: %s MIDIDEVICEFILENAME [PATCHFILEPREFIX] [PATCHFILEPOSTFIX]' % (sys.argv[0]) )

