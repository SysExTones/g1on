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


def to_hex( data, offset=0, length=None ):
	retval = ''
	if data:
		if length is not None:
			retval = convert_bytes_to_hex_string( data[offset:offset + length] )
		else:
			retval = convert_bytes_to_hex_string( data[offset:] )
	return retval


def convert_bytes_to_hex_string( data ):
	return ' '.join( ['%02x' % (b) for b in data] )


def convert_from_midi_to_string( data ):
	low = ord( ' ' )
	high = ord( '~' )
	if 0 in data:
		data = data[:data.index( 0 )]
	return ''.join( [chr( x ) for x in data if x >= low and x <= high] )


def build_debug_count_header( count ):
	header = ''
	for loop in range( count ):
		if header:
			header = '%s %02i' % (header, loop % 100)
		else:
			header = '%02i' % (loop % 100)
	return header

