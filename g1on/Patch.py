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

import g1on as _g1on


class Patch( object ):
	
	patch = None
	data = None
	
	def __init__( self, patch ):
		if patch:
			self.patch = patch[:]
			self.descramble_patch()
	
	def fabricate( self, name='', volume=0, effects=None, params=None, actives=None ):
		count = 0
		for e in effects:
			if e:
				count += 1
			else:
				break
		fabricatedeffects = None
		if effects and count > 0:
			fabricatedeffects = []
			for loop in range( count ):
				if actives and loop < len( actives ):
					fabricatedeffects.append( _g1on.Effect( effects[loop], actives[loop] ) )
				else:
					fabricatedeffects.append( _g1on.Effect( effects[loop], True ) )
		self.fabricate_patch_from_effects( name, volume, count, fabricatedeffects, params )
		self.scramble_effect_count()
	
	def fabricate_patch_from_effects( self, name, volume, count, effects=None, params=None ):
		self.data = [0x00 for i in range( 128 )]
		self.set_name( name )
		self.set_volume( volume )
		self.set_effect_count( count )
		fabricatedeffects = []
		for loop in range( count ):
			if params and params[loop]:
				effects[loop].set_params( params[loop] )
			else:
				effects[loop].set_params( None )
			fabricatedeffects.append( effects[loop] )
		for loop in range( count, 5 ):
			if loop < len( effects ):
				effects[loop].set_params( None )
				fabricatedeffects.append( effects[loop] )
			else:
				fabricatedeffects.append( _g1on.Effect( 'bypass', True ) )
		self.set_effects( fabricatedeffects[0], fabricatedeffects[1], fabricatedeffects[2], fabricatedeffects[3], fabricatedeffects[4] )
		self.scramble_patch()
	
	def get_name( self ):
		retval = []
		for c in self.data[116:]:
			if c != 0x00:
				retval.append( c )
		retval = _g1on.convert_from_midi_to_string( retval ).strip()
		return retval
	
	def set_name( self, name ):
		name = name[:10]
		index = 0
		offset = 0
		while index < len( name ):
			if offset == 4:
				offset += 1
			self.data[116 + offset] = ord( name[index] )
			index += 1
			offset += 1
		while index < 10:
			if offset == 4:
				offset += 1
			self.data[116 + offset] = ord( ' ' )
			index += 1
			offset += 1
	
	def get_volume( self ):
		return self.data[105]
	
	def set_volume( self, volume ):
		self.data[105] = volume
	
	def descramble_patch( self ):
		self.data = self.patch[:]
		self.descramble_effect_count()
		self.descramble_effects()
	
	def scramble_patch( self ):
		self.patch = self.data[:]
		self.scramble_effects()
		self.scramble_effect_count()

	def get_effect_count( self ):
		return self.data[103]
	
	def set_effect_count( self, count ):
		self.data[103] = count
	
	def descramble_effect_count( self ):
		count = 0
		if (self.data[96] & 0x01):
			if (self.data[103] & 0x20):
				count = 5
			else:
				count = 4
		else:
			if (self.data[103] & 0x60) == 0x60:
				count = 3
			elif (self.data[103] & 0x40):
				count = 2
			elif (self.data[103] & 0x20):
				count = 1
		self.data[96] &= 0xfe
		self.data[103] = count
		return count
	
	def scramble_effect_count( self ):
		count = self.get_effect_count()
		self.patch[96] &= 0xfe
		self.patch[103] &= 0x00
		if count in [4, 5]:
			self.patch[96] |= 0x01
		if count in [1, 5]:
			self.patch[103] |= 0x20
		elif count in [2]:
			self.patch[103] |= 0x40
		elif count in [3]:
			self.patch[103] |= 0x60
		return count
	
	def get_scrambled_effect( self, index ):
		return self.patch[_g1on.ZOOM_G1ON_EFFECT_LOCATIONS[index][0]:_g1on.ZOOM_G1ON_EFFECT_LOCATIONS[index][1]]
	
	def get_scrambled_effects( self, count=None ):
		retval = []
		if count is None:
			count = self.get_effect_count()
		for loop in range( count ):
			retval.append( self.get_scrambled_effect( loop ) )
		return retval
	
	def set_scrambled_effect( self, index, effect ):
		start = _g1on.ZOOM_G1ON_EFFECT_LOCATIONS[index][0]
		stop = _g1on.ZOOM_G1ON_EFFECT_LOCATIONS[index][1]
		self.patch[start:stop] = effect[:stop - start]
	
	def set_scrambled_effects( self, e1, e2, e3, e4, e5 ):
		if e1:
			self.set_scrambled_effect( 0, e1 )
		if e2:
			self.set_scrambled_effect( 1, e2 )
		if e3:
			self.set_scrambled_effect( 2, e3 )
		if e4:
			self.set_scrambled_effect( 3, e4 )
		if e5:
			self.set_scrambled_effect( 4, e5 )
	
	def get_effect( self, index ):
		#return self.data[_g1on.ZOOM_G1ON_EFFECT_LOCATIONS[index][0]:_g1on.ZOOM_G1ON_EFFECT_LOCATIONS[index][1]]
		return _g1on.Effect( effect=self.data[_g1on.ZOOM_G1ON_EFFECT_LOCATIONS[index][0]:_g1on.ZOOM_G1ON_EFFECT_LOCATIONS[index][1]] )
	
	def get_effects( self, count=None ):
		retval = []
		if count is None:
			count = self.get_effect_count()
		for loop in range( count ):
			retval.append( self.get_effect( loop ) )
		return retval
	
	def set_effect( self, index, effect ):
		start = _g1on.ZOOM_G1ON_EFFECT_LOCATIONS[index][0]
		stop = _g1on.ZOOM_G1ON_EFFECT_LOCATIONS[index][1]
		if type( effect ) is _g1on.Effect:
			self.data[start:stop] = effect.effect[:stop - start]
		else:
			self.data[start:stop] = effect[:stop - start]
	
	def set_effects( self, e1=None, e2=None, e3=None, e4=None, e5=None ):
		if e1:
			self.set_effect( 0, e1 )
		if e2:
			self.set_effect( 1, e2 )
		if e3:
			self.set_effect( 2, e3 )
		if e4:
			self.set_effect( 3, e4 )
		if e5:
			self.set_effect( 4, e5 )
	
	def descramble_effects( self ):
		(e1, e2, e3, e4, e5) = self.get_scrambled_effects( 5 )
		# shuffle bytes
		_g1on.move_byte( e2, 4, 8 )
		_g1on.move_byte( e2, 12, 16 )
		_g1on.move_byte( e2, 20, 17 )
		_g1on.move_byte( e2, 19, 20 )
		_g1on.move_byte( e3, 7, 8 )
		_g1on.move_byte( e3, 15, 16 )
		_g1on.move_byte( e4, 3, 8 )
		_g1on.move_byte( e4, 11, 16 )
		_g1on.move_byte( e4, 19, 17 )
		_g1on.move_byte( e4, 20, 19 )
		_g1on.move_byte( e5, 14, 16 )
		_g1on.move_byte( e5, 6, 8 )
		# swap bits
		_g1on.swap_bits( e2, 0x70, -3, 8, 0 )
		_g1on.swap_bits( e2, 0x07, 4, 8, 8 )
		_g1on.swap_bits( e2, 0x70, -3, 16, 8 )
		_g1on.swap_bits( e2, 0x02, 4, 16, 16 )
		_g1on.swap_bits( e3, 0x3f, 1, 8, 8 )
		_g1on.swap_bits( e3, 0x10, 1, 16, 16 )
		_g1on.exchange_bits( e2, e3, 0x07, 1, 17, 0 )
		_g1on.swap_bits( e4, 0x38, -2, 8, 0 )
		_g1on.swap_bits( e4, 0x03, 5, 8, 8 )
		_g1on.swap_bits( e4, 0x78, -2, 16, 8 )
		_g1on.swap_bits( e4, 0x01, 5, 16, 16 )
		_g1on.swap_bits( e5, 0x40, -5, 8, 0 )
		_g1on.swap_bits( e5, 0x1f, 2, 8, 8 )
		_g1on.swap_bits( e5, 0x08, 2, 16, 16 )
		_g1on.swap_bits( e5, 0x40, -5, 16, 8 )
		_g1on.exchange_bits( e4, e5, 0x03, 2, 17, 0 )
		# toggle effect type bit, if necessary
		if (e1[16] & 0x04):
			_g1on.exchange_bits( e1, e2, 0x04, 4, 16, 0 )
		if (e2[17] & 0x20):
			_g1on.exchange_bits( e2, e3, 0x20, 1, 17, 0 )
		if (e3[16] & 0x02):
			_g1on.exchange_bits( e3, e4, 0x02, 5, 16, 0 )
		if (e4[17] & 0x10):
			_g1on.exchange_bits( e4, e5, 0x10, 2, 17, 0 )
		self.set_effects( e1, e2, e3, e4, e5 )
	
	def scramble_effects( self ):
		(e1, e2, e3, e4, e5) = self.get_effects( 5 )
		e1 = e1.effect[:]
		e2 = e2.effect[:]
		e3 = e3.effect[:]
		e4 = e4.effect[:]
		e5 = e5.effect[:]
		# toggle effect type bit, if necessary
		if (e5[0] & 0x40):
			_g1on.exchange_bits( e5, e4, 0x40, -2, 0, 17 )
		if (e4[0] & 0x40):
			_g1on.exchange_bits( e4, e3, 0x40, -5, 0, 16 )
		if (e3[0] & 0x40):
			_g1on.exchange_bits( e3, e2, 0x40, -1, 0, 17 )
		if (e2[0] & 0x40):
			_g1on.exchange_bits( e2, e1, 0x40, -4, 0, 16 )
		# swap bits
		_g1on.exchange_bits( e5, e4, 0x0c, -2, 0, 17 )
		_g1on.swap_bits( e5, 0x02, 5, 8, 16 )
		_g1on.swap_bits( e5, 0x20, -2, 16, 16 )
		_g1on.swap_bits( e5, 0x7c, -2, 8, 8 )
		_g1on.swap_bits( e5, 0x02, 5, 0, 8 )
		_g1on.swap_bits( e4, 0x20, -5, 16, 16 )
		_g1on.swap_bits( e4, 0x1e, 2, 8, 16 )
		_g1on.swap_bits( e4, 0x60, -5, 8, 8 )
		_g1on.swap_bits( e4, 0x0e, 2, 0, 8 )
		_g1on.exchange_bits( e3, e2, 0x0e, -1, 0, 17 )
		_g1on.swap_bits( e3, 0x20, -1, 16, 16 )
		_g1on.swap_bits( e3, 0x7e, -1, 8, 8 )
		_g1on.swap_bits( e2, 0x20, -4, 16, 16 )
		_g1on.swap_bits( e2, 0x0e, 3, 8, 16 )
		_g1on.swap_bits( e2, 0x70, -4, 8, 8 )
		_g1on.swap_bits( e2, 0x0e, 3, 0, 8 )
		# shuffle bytes
		_g1on.move_byte( e5, 8, 6 )
		_g1on.move_byte( e5, 16, 14 )
		_g1on.move_byte( e4, 19, 20 )
		_g1on.move_byte( e4, 17, 19 )
		_g1on.move_byte( e4, 16, 11 )
		_g1on.move_byte( e4, 8, 3 )
		_g1on.move_byte( e3, 16, 15 )
		_g1on.move_byte( e3, 8, 7 )
		_g1on.move_byte( e2, 20, 19 )
		_g1on.move_byte( e2, 17, 20 )
		_g1on.move_byte( e2, 16, 12 )
		_g1on.move_byte( e2, 8, 4 )
		self.set_scrambled_effects( e1, e2, e3, e4, e5 )
	
	def to_text( self ):
		retval = '%s\t%i' % (self.get_name(), self.get_volume())
		for effect in self.get_effects():
			retval = '%s\n%s' % (retval, effect.to_text())
		return retval
	
	def to_hex_text( self ):
		return _g1on.to_hex( self.data )
	
	def to_scrambled_hex_text( self ):
		return _g1on.to_hex( self.patch )


class PatchInputFile( Patch ):
	
	filename = None
	
	def __init__( self, filename ):
		super( PatchInputFile, self ).__init__( self.read_from_file( filename ) )
	
	def read_from_file( self, filename ):
		retval = None
		if filename and _os.path.exists( filename ) and _os.path.getsize( filename ) == 128:
			self.filename = filename
			i = open( self.filename, 'rb' )
			retval = list( bytearray( i.read( 128 ) ) )
			i.close()
		return retval


class PatchInputTextFile( Patch ):
	
	filename = None
	
	def __init__( self, filename ):
		super( PatchInputTextFile, self ).__init__( self.read_from_file( filename ) )
	
	def extract_config( self, lines ):
		retval = []
		for line in lines:
			line = line.strip()
			if line and not line.startswith( '#' ):
				if '#' in line:
					line = line.split( '#', 1 )[0].strip()
				if line:
					retval.append( line )
		return retval
	
	def extract_effects( self, lines ):
		retval = []
		for line in lines:
			if '\t' in line:
				p = []
				(name, params) = line.split( '\t', 1 )
				for param in params.split( ',' ):
					p.append( int( param.strip() ) )
				retval.append( [name, p] )
		return retval
	
	def extract_effects_params_actives( self, texteffects ):
		name = texteffects[0][0]
		volume = int( texteffects[0][1][0] )
		bypassed = '(bypassed)'
		effects = []
		params = []
		actives = []
		for loop in range( 1, 6 ):
			e = None
			ep = None
			ea = True
			if len( texteffects ) > loop:
				e = texteffects[loop][0]
				ep = texteffects[loop][1]
				if bypassed in e:
					e = e.replace( bypassed, '' )
					e = e.strip()
					ea = False
			effects.append( e )
			params.append( ep )
			actives.append( ea )
		return (name, volume, effects, params, actives)
	
	def read_from_file( self, filename ):
		retval = None
		lines = None
		if filename and _os.path.exists( filename ):
			self.filename = filename
			i = open( self.filename, 'rt' )
			lines = i.readlines()
			i.close()
		if lines:
			texteffects = self.extract_effects( self.extract_config( lines ) )
			(name, volume, effects, params, actives) = self.extract_effects_params_actives( texteffects )
			self.fabricate( name, volume, effects, params, actives )
			retval = self.patch[:]
		return retval


class PatchOutputFile( Patch ):
	
	filename = None
	
	def __init__( self, filename, patch ):
		super( PatchOutputFile, self ).__init__( patch )
		self.write_to_file( filename )
	
	def write_to_file( self, filename ):
		if filename:
			self.filename = filename
			o = open( filename, 'wb' )
			o.write( bytearray( self.patch ) )
			o.close()


class PatchOutputTextFile( Patch ):
	
	filename = None
	
	def __init__( self, filename, patch ):
		super( PatchOutputTextFile, self ).__init__( patch )
		self.write_to_file( filename )
	
	def write_to_file( self, filename ):
		if filename:
			self.filename = filename
			o = open( filename, 'wt' )
			o.write( self.to_text() )
			o.write( '\n' )
			o.close()

