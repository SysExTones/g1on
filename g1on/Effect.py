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


import g1on as _g1on


class Effect( object ):
	
	effect = None
	
	def __init__( self, name=None, active=True, effect=None ):
		if effect:
			self.effect = effect[:]
		else:
			if name:
				self.fabricate( name, active )
			else:
				self.fabricate()
	
	def fabricate( self, name, active=True ):
		self.effect = [0x00 for i in range( 21 )]
		if name:
			lookup = None
			if 'iteritems' in dir( {} ): # FIX: kludge because Python3 broke Python2
				lookup = dict( (v,k) for k,v in _g1on.ZOOM_G1ON_EFFECTS.iteritems() )
			else:
				lookup = dict( (v,k) for k,v in _g1on.ZOOM_G1ON_EFFECTS.items() )
			tag = lookup[name]
			self.effect[0] = tag[0]
			self.effect[1] = tag[1]
			self.effect[2] = tag[2]
			self.effect[4] = tag[3]
			self.set_bypassed( active )
	
	def is_bypassed( self ):
		return (self.effect[1] & 0x01) == 0x00
	
	def set_bypassed( self, active=0x00 ):
		self.effect[1] &= 0xfe
		state = 0x01
		if active == 0x00:
			state = 0x00
		self.effect[1] |= state
	
	def get_name( self ):
		retval = ''
		tag = (
			self.effect[0] & 0x40,
			self.effect[1] & 0x7a,
			self.effect[2] & 0x07,
			self.effect[4] & 0x1e,
		)
		if tag in _g1on.ZOOM_G1ON_EFFECTS:
			retval = _g1on.ZOOM_G1ON_EFFECTS[tag]
		return retval
	
	def get_param( self, index ):
		retval = None
		funcname = 'get_%s_param_%i' % (self.get_name(), index)
		func = _g1on.get_func( funcname )
		if func:
			retval = func( self.effect )
		#else:
			#print( '%s missing' % (funcname) )
		return retval
	
	def get_params( self ):
		retval = []
		for loop in range( 9 ):
			param = self.get_param( loop )
			if param is not None:
				retval.append( param )
		return retval
	
	def set_param( self, index, value ):
		funcname = 'set_%s_param_%i' % (self.get_name(), index)
		func = _g1on.get_func( funcname )
		if func:
			self.effect = func( self.effect, value )
		else:
			print( '%s missing' % (funcname) )
	
	def set_params( self, params ):
		if params:
			for loop in range( len( params ) ):
				self.set_param( loop, params[loop] )
	
	def to_text( self ):
		retval = ''
		bypassed = ''
		if self.is_bypassed():
			bypassed = ' (bypassed)'
		retval = '%s%s%s\t' % (retval, self.get_name(), bypassed)
		sep = ''
		for param in self.get_params():
			retval = '%s%s%i' % (retval, sep, param)
			sep = ', '
		return retval
	
	def to_hex_text( self ):
		return _g1on.to_hex( self.effect )

