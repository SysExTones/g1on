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


import g1on.CONSTANTS as _CONSTANTS


def build_patch_change_request( n ):
	return bytearray( _CONSTANTS.ZOOM_G1ON_PATCH_CHANGE_REQUEST + [n] )


def build_effect_parameter_change_request( slot, param, value ):
	return bytearray( _CONSTANTS.ZOOM_G1ON_PATCH_CHANGE_ID + [slot & 0x7f] + [param & 0x7f] + [(value & 0x7f), (value & 0x03f80) >> 7] + [_CONSTANTS.SYSEX_STOP] )


def build_effect_disable_request( slot ):
	return build_effect_parameter_change_request( slot, 0, 0 )


def build_effect_enable_request( slot ):
	return build_effect_parameter_change_request( slot, 0, 1 )


def build_effect_reset_request( slot ):
	return build_effect_parameter_change_request( slot, 1, 1 )


def build_identity_request():
	return bytearray( _CONSTANTS.ZOOM_G1ON_REQUEST_ID )


def build_editor_mode_request( mode='on' ):
	retval = bytearray( _CONSTANTS.ZOOM_G1ON_REQUEST_EDITOR_MODE_ON )
	if mode.lower() == 'off':
		retval = bytearray( _CONSTANTS.ZOOM_G1ON_REQUEST_EDITOR_MODE_OFF )
	return retval


def build_current_patch_number_request():
	return bytearray( _CONSTANTS.ZOOM_G1ON_REQUEST_CURRENT_PATCH_NUMBER )


def build_current_patch_request():
	return bytearray( _CONSTANTS.ZOOM_G1ON_REQUEST_CURRENT_PATCH )


def build_patch_request( patchnumber ):
	return bytearray( _CONSTANTS.ZOOM_G1ON_REQUEST_PATCH_BY_NUMBER_PREFIX + [_CONSTANTS.ZOOM_00, _CONSTANTS.ZOOM_00, patchnumber] + [_CONSTANTS.SYSEX_STOP] )


def build_patch_change( patch ):
	return bytearray( _CONSTANTS.ZOOM_G1ON_CURRENT_PATCH_ID + patch + [0xf7] )


def build_tuner_mode_request( mode='on' ):
	inertrequestneededforsomereason = build_identity_request()
	retval = inertrequestneededforsomereason + bytearray( _CONSTANTS.ZOOM_G1ON_TUNER_MODE_REQUEST_ON )
	if mode.lower() == 'off':
		retval = bytearray( _CONSTANTS.ZOOM_G1ON_TUNER_MODE_REQUEST_OFF ) + inertrequestneededforsomereason
	return retval

