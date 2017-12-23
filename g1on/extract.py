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


def get_command_data( command, value ):
	return command[len( value ):-1]


def get_id( command ):
	return get_command_data( command, _g1on.ZOOM_G1ON_ID )


def get_current_patch( command ):
	return get_command_data( command, _g1on.ZOOM_G1ON_CURRENT_PATCH_ID )


def get_patch( command ):
	return get_command_data( command, _g1on.ZOOM_G1ON_PATCH_ID )


def get_patch_change( command ):
	return get_command_data( command, _g1on.ZOOM_G1ON_PATCH_CHANGE_ID )
