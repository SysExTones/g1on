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
	argc = len( sys.argv )
	if argc >= 2:
		patchnumber = -1
		if argc == 3:
			if sys.argv[2] == 'all':
				patchnumber = -100
			elif sys.argv[2].isdigit():
				patchnumber = int( sys.argv[2] )
		o = g1on.O( sys.argv[1] )
		if patchnumber == -1:
			o.write( g1on.build_current_patch_number_request() )
			o.write( g1on.build_current_patch_request() )
		elif patchnumber == -100:
			for loop in range( 100 ):
				o.write( g1on.build_patch_request( loop ) )
		else:
			o.write( g1on.build_patch_request( patchnumber ) )
		o.close()
	else:
		print( 'Usage: %s MIDIDEVICEFILENAME [patchnumber OR all]' % (sys.argv[0]) )

