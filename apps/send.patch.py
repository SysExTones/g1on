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


import os
import sys

import g1on


def is_binary_patch_file( filename ):
	retval = False
	if os.path.exists( filename ) and os.path.getsize( filename ) == 128:
		i = open( filename, 'rb' )
		d = i.read( 128 )
		if d[120] == '\0' and d[127] == '\0':
			retval = True
	return retval


def is_text_patch_file( filename ):
	retval = False
	if os.path.exists( filename ):
		i = open( filename, 'rt' )
		d = '\n'.join( i.readlines() )
		if '\t' in d and '\0' not in d:
			retval = True
	return retval


def send_patch( midifilename, patchfilename ):
	i = None
	if is_binary_patch_file( patchfilename ):
		i = g1on.PatchInputFile( patchfilename )
	elif is_text_patch_file( patchfilename ):
		i = g1on.PatchInputTextFile( patchfilename )
	if i:
		o = g1on.O( midifilename )
		o.write( g1on.build_patch_change( i.patch ) )
		o.close()



if __name__ == '__main__':
	argc = len( sys.argv )
	if argc >= 2:
		midifilename = sys.argv[1]
		for patchfilename in sys.argv[2:]:
			send_patch( midifilename, patchfilename )
	else:
		print( 'Usage: %s MIDIDEVICEFILENAME PATCHFILESTOSEND' % (sys.argv[0]) )

