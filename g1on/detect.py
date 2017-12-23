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


def is_command( command, value ):
	return command[:len( value )] == value


def is_id( command ):
	return is_command( command, _g1on.ZOOM_G1ON_ID )


def is_current_patch( command ):
	return is_command( command, _g1on.ZOOM_G1ON_CURRENT_PATCH_ID )


def is_patch( command ):
	return is_command( command, _g1on.ZOOM_G1ON_PATCH_ID )


def is_patch_change( command ):
	return is_command( command, _g1on.ZOOM_G1ON_PATCH_CHANGE_ID )

