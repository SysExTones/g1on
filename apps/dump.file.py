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


def display_patch( patch ):
	print( patch.to_text() )
	print( '' )
	print( g1on.build_debug_count_header( 128 ) )
	print( '' )
	print( patch.to_scrambled_hex_text() )
	print( '' )
	print( patch.to_hex_text() )
	print( '' )
	print( g1on.build_debug_count_header( 21 ) )
	print( '' )
	for effect in patch.get_scrambled_effects( 5 ):
		print( g1on.to_hex( effect ) )
	print( '' )
	for effect in patch.get_effects( 5 ):
		print( effect.to_hex_text() )



if __name__ == '__main__':
	if len( sys.argv ) > 1:
		for fn in sys.argv[1:]:
			display_patch( g1on.PatchInputFile( fn ) )
	else:
		print( 'Usage: %s g1onPATCHFILES' % (sys.argv[0]) )


