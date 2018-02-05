#!/usr/bin/env python

# Copyright (c) 2018
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
	if len( sys.argv ) == 3:
		o = g1on.O( sys.argv[1] )
		o.write( g1on.build_tuner_mode_request( sys.argv[2] ) )
		o.close()
	else:
		print( 'Usage: %s MIDIDEVICEFILENAME ONorOFF' % (sys.argv[0]) )

