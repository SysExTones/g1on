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


import os as _os
import select as _select
import fcntl as _fcntl

import g1on as _g1on


class IO( object ):
	
	name = None
	mode = ''
	f = None
	
	def __init__( self, name=None, mode=None ):
		self.open( name, mode )
	
	def open( self, name=None, mode=None ):
		self.close()
		if name:
			self.name = name
		if mode:
			self.mode = mode
		if self.name and self.mode:
			self.f = open( self.name, self.mode, 0 )
		return self.f
	
	def close( self ):
		if self.f:
			self.f.close()
			self.f = None


class I( IO ):
	
	timeout = 0.3
	
	def __init__( self, name=None, mode='rb', timeout=0.3 ):
		self.timeout = timeout
		super( I, self ).__init__( name, mode )
	
	def open( self, name=None, mode=None ):
		super( I, self ).open( name, mode )
		if self.f:
			flags = _fcntl.fcntl( self.f, _fcntl.F_GETFL ) | _os.O_NONBLOCK
			_fcntl.fcntl( self.f, _fcntl.F_SETFL, flags )
		return self.f
	
	def read( self ):
		retval = []
		if self.f:
			if _select.select( [self.f], [], [], self.timeout ):
				b = self.f.read()
				if b:
					if isinstance( b, str ):
						retval = [ord( c ) for c in b]
					else:
						retval = b
		return retval
	
	def is_open( self ):
		return self.f != None


class O( IO ):
	
	def __init__( self, name=None, mode='wb' ):
		super( O, self ).__init__( name, mode )
	
	def write( self, data ):
		if self.f:
			self.f.write( data )


class BI( I ):
	
	data = None
	
	def __init__( self, name=None, mode='rb', timeout=0.3 ):
		self.data = []
		super( BI, self ).__init__( name, mode, timeout )
	
	def fill( self ):
		if self.f:
			self.data += self.read()
	
	def has_data( self ):
		return self.data and len( self.data ) > 0
	
	def has_non_sysex( self ):
		retval = False
		if self.has_data() and self.data[0] != _g1on.SYSEX_START:
			retval = True
		return retval
	
	def has_sysex( self ):
		retval = False
		if self.has_data() and _g1on.SYSEX_START in self.data and _g1on.SYSEX_STOP in self.data:
			retval = True
		return retval
	
	def get_non_sysex( self ):
		retval = []
		if self.has_non_sysex():
			for loop in range( len( self.data ) ):
				if self.data[loop] not in [_g1on.SYSEX_START]:
					retval.append( self.data[loop] )
		if retval:
			self.data = self.data[len( retval ):]
		return retval
	
	def get_sysex( self ):
		retval = []
		if self.has_sysex():
			retval = self.data[:self.data.index( _g1on.SYSEX_STOP ) + 1]
		if retval:
			self.data = self.data[len( retval ):]
		return retval

