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


import inspect as _inspect
import sys as _sys


def get_max_150( d ):
	retval = d[9] & 0x7f
	if (d[8] & 0x40):
		retval |= (0x80)
	return retval


def set_max_150( d, v ):
	retval = d
	if d:
		retval = d[:]
		if v & 0x80:
			retval[8] |= 0x40
		retval[9] |= v & 0x7f
	return retval


def get_cab_sim( d ):
	retval = 0
	if (d[16] & 0x20):
		retval = (d[15] & 0x3f)
	return retval


def set_cab_sim( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[16] |= 0x20
		retval[15] |= (v & 0x3f)
	return retval




def get_comp_param_0( d ):
	return ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_comp_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_comp_param_1( d ):
	return ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_comp_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_comp_param_2( d ):
	return get_max_150( d )


def set_comp_param_2( d, v ):
	return set_max_150( d, v )


def get_comp_param_3( d ):
	return ((d[10] & 0x20) >> 5)


def set_comp_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[10] |= ((v & 0x01) << 5)
	return retval




def get_optcomp_param_0( d ):
	return ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_optcomp_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_optcomp_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_optcomp_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_optcomp_param_2( d ):
	return get_max_150( d )


def set_optcomp_param_2( d, v ):
	return set_max_150( d, v )




def get_160comp_param_0( d ):
	return ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_160comp_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_160comp_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_160comp_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_160comp_param_2( d ):
	return (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_160comp_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_160comp_param_3( d ):
	return ((d[10] & 0x20) >> 5)


def set_160comp_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_160comp_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_160comp_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_slowattck_param_0( d ):
	return ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_slowattck_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_slowattck_param_1( d ):
	return ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_slowattck_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_slowattck_param_2( d ):
	return get_max_150( d )


def set_slowattck_param_2( d, v ):
	return set_max_150( d, v )




def get_znr_param_0( d ):
	return ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_znr_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_znr_param_1( d ):
	return ((d[6] & 0x08) >> 3)


def set_znr_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_znr_param_2( d ):
	return get_max_150( d )


def set_znr_param_2( d, v ):
	return set_max_150( d, v )




def get_noisegate_param_0( d ):
	return ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_noisegate_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_noisegate_param_1( d ):
	return ((d[7] & 0x04) << 5) | ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_noisegate_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x80) >> 5)
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval




def get_graphiceq_param_0( d ):
	return ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_graphiceq_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_graphiceq_param_1( d ):
	return ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_graphiceq_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_graphiceq_param_2( d ):
	return (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_graphiceq_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_graphiceq_param_3( d ):
	return ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_graphiceq_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_graphiceq_param_4( d ):
	return ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_graphiceq_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_graphiceq_param_5( d ):
	return ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_graphiceq_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_graphiceq_param_6( d ):
	return ((d[14] & 0x10) << 3) | ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_graphiceq_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x80) >> 3)
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval




def get_paraeq_param_0( d ):
	return ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_paraeq_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_paraeq_param_1( d ):
	return ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_paraeq_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_paraeq_param_2( d ):
	return (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_paraeq_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_paraeq_param_3( d ):
	return ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_paraeq_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_paraeq_param_4( d ):
	return ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_paraeq_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_paraeq_param_5( d ):
	return ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_paraeq_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_paraeq_param_6( d ):
	return ((d[14] & 0x10) << 3) | ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_paraeq_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x80) >> 3)
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval




def get_exciter_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_exciter_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_exciter_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_exciter_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_exciter_param_2( d ):
	return get_max_150( d )


def set_exciter_param_2( d, v ):
	return set_max_150( d, v )




def get_autowah_param_0( d ):
	return ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_autowah_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_autowah_param_1( d ):
	return ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_autowah_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_autowah_param_2( d ):
	return get_max_150( d )


def set_autowah_param_2( d, v ):
	return set_max_150( d, v )




def get_cry_param_0( d ):
	return ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_cry_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_cry_param_1( d ):
	return ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_cry_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_cry_param_2( d ):
	return (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_cry_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_cry_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_cry_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_cry_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_cry_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_mfilter_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_mfilter_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_mfilter_param_1( d ):
	return ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_mfilter_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_mfilter_param_2( d ):
	return (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_mfilter_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_mfilter_param_3( d ):
	return ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_mfilter_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_mfilter_param_4( d ):
	return ((d[11] & 0x20) >> 5)


def set_mfilter_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_mfilter_param_5( d ):
	return ((d[12] & 0x20) >> 5)


def set_mfilter_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_mfilter_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_mfilter_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_mfilter_param_7( d ):
	return ((d[15] & 0x10) << 3) | ((d[15] & 0x08) << 3) | ((d[15] & 0x04) << 3) | ((d[15] & 0x02) << 3) | ((d[15] & 0x01) << 3) | ((d[8] & 0x02) << 1) | ((d[14] & 0x40) >> 5) | ((d[14] & 0x20) >> 5)


def set_mfilter_param_7( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[15] |= ((v & 0x80) >> 3)
		retval[15] |= ((v & 0x40) >> 3)
		retval[15] |= ((v & 0x20) >> 3)
		retval[15] |= ((v & 0x10) >> 3)
		retval[15] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) >> 1)
		retval[14] |= ((v & 0x02) << 5)
		retval[14] |= ((v & 0x01) << 5)
	return retval




def get_step_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_step_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_step_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_step_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_step_param_2( d ):
	return (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_step_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_step_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_step_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_step_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_step_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_seqfilter_param_0( d ):
	return ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_seqfilter_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_seqfilter_param_1( d ):
	return ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_seqfilter_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_seqfilter_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_seqfilter_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_seqfilter_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_seqfilter_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_seqfilter_param_4( d ):
	return ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_seqfilter_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_seqfilter_param_5( d ):
	return ((d[13] & 0x10) << 3) | ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_seqfilter_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x80) >> 3)
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_randomfilter_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_randomfilter_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_randomfilter_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_randomfilter_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_randomfilter_param_2( d ):
	return (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_randomfilter_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_randomfilter_param_3( d ):
	return ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_randomfilter_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_randomfilter_param_4( d ):
	return ((d[11] & 0x20) >> 5)


def set_randomfilter_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_randomfilter_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_randomfilter_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_randomfilter_param_6( d ):
	return ((d[14] & 0x10) << 3) | ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_randomfilter_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x80) >> 3)
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval




def get_fcycle_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_fcycle_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_fcycle_param_1( d ):
	return ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_fcycle_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_fcycle_param_2( d ):
	return get_max_150( d )


def set_fcycle_param_2( d, v ):
	return set_max_150( d, v )


def get_fcycle_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_fcycle_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_fcycle_param_4( d ):
	return ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_fcycle_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_booster_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_booster_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_booster_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_booster_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_booster_param_2( d ):
	return get_max_150( d )


def set_booster_param_2( d, v ):
	return set_max_150( d, v )




def get_overdrive_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_overdrive_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_overdrive_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_overdrive_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_overdrive_param_2( d ):
	return get_max_150( d )


def set_overdrive_param_2( d, v ):
	return set_max_150( d, v )




def get_tscream_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_tscream_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_tscream_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_tscream_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_tscream_param_2( d ):
	return get_max_150( d )


def set_tscream_param_2( d, v ):
	return set_max_150( d, v )




def get_governor_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_governor_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_governor_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_governor_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_governor_param_2( d ):
	return get_max_150( d )


def set_governor_param_2( d, v ):
	return set_max_150( d, v )




def get_distplus_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_distplus_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_distplus_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_distplus_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_distplus_param_2( d ):
	return get_max_150( d )


def set_distplus_param_2( d, v ):
	return set_max_150( d, v )




def get_dist1_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_dist1_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_dist1_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_dist1_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_dist1_param_2( d ):
	return get_max_150( d )


def set_dist1_param_2( d, v ):
	return set_max_150( d, v )




def get_squeak_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_squeak_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_squeak_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_squeak_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_squeak_param_2( d ):
	return get_max_150( d )


def set_squeak_param_2( d, v ):
	return set_max_150( d, v )




def get_fuzzsmile_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_fuzzsmile_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_fuzzsmile_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_fuzzsmile_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_fuzzsmile_param_2( d ):
	return get_max_150( d )


def set_fuzzsmile_param_2( d, v ):
	return set_max_150( d, v )




def get_greatmuff_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_greatmuff_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_greatmuff_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_greatmuff_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_greatmuff_param_2( d ):
	return get_max_150( d )


def set_greatmuff_param_2( d, v ):
	return set_max_150( d, v )




def get_metalwrld_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_metalwrld_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_metalwrld_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_metalwrld_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_metalwrld_param_2( d ):
	return get_max_150( d )


def set_metalwrld_param_2( d, v ):
	return set_max_150( d, v )




def get_hotbox_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_hotbox_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_hotbox_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_hotbox_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_hotbox_param_2( d ):
	return get_max_150( d )


def set_hotbox_param_2( d, v ):
	return set_max_150( d, v )




def get_zclean_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_zclean_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_zclean_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_zclean_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_zclean_param_2( d ):
	return get_max_150( d )


def set_zclean_param_2( d, v ):
	return set_max_150( d, v )




def get_zmp1_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_zmp1_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_zmp1_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_zmp1_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_zmp1_param_2( d ):
	return get_max_150( d )


def set_zmp1_param_2( d, v ):
	return set_max_150( d, v )




def get_zscream_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_zscream_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_zscream_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_zscream_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_zscream_param_2( d ):
	return get_max_150( d )


def set_zscream_param_2( d, v ):
	return set_max_150( d, v )




def get_zwild_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_zwild_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_zwild_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_zwild_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_zwild_param_2( d ):
	return get_max_150( d )


def set_zwild_param_2( d, v ):
	return set_max_150( d, v )




def get_leadzoom9002_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_leadzoom9002_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_leadzoom9002_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_leadzoom9002_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_leadzoom9002_param_2( d ):
	return get_max_150( d )


def set_leadzoom9002_param_2( d, v ):
	return set_max_150( d, v )




def get_extremedistortion_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_extremedistortion_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_extremedistortion_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_extremedistortion_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_extremedistortion_param_2( d ):
	return get_max_150( d )


def set_extremedistortion_param_2( d, v ):
	return set_max_150( d, v )




def get_acoustic_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_acoustic_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_acoustic_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_acoustic_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_acoustic_param_2( d ):
	return get_max_150( d )


def set_acoustic_param_2( d, v ):
	return set_max_150( d, v )




def get_fdcombo_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_fdcombo_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_fdcombo_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_fdcombo_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_fdcombo_param_2( d ):
	return get_max_150( d )


def set_fdcombo_param_2( d, v ):
	return set_max_150( d, v )


def get_fdcombo_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_fdcombo_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_fdcombo_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_fdcombo_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_fdcombo_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_fdcombo_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_fdcombo_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_fdcombo_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_fdcombo_param_7( d ):
	return get_cab_sim( d )


def set_fdcombo_param_7( d, v ):
	return set_cab_sim( d, v )


def get_fdcombo_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_fdcombo_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_deluxer_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_deluxer_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_deluxer_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_deluxer_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_deluxer_param_2( d ):
	return get_max_150( d )


def set_deluxer_param_2( d, v ):
	return set_max_150( d, v )


def get_deluxer_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_deluxer_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_deluxer_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_deluxer_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_deluxer_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_deluxer_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_deluxer_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_deluxer_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_deluxer_param_7( d ):
	return get_cab_sim( d )


def set_deluxer_param_7( d, v ):
	return set_cab_sim( d, v )


def get_deluxer_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_deluxer_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_fdvibro_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_fdvibro_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_fdvibro_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_fdvibro_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_fdvibro_param_2( d ):
	return get_max_150( d )


def set_fdvibro_param_2( d, v ):
	return set_max_150( d, v )


def get_fdvibro_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_fdvibro_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_fdvibro_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_fdvibro_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_fdvibro_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_fdvibro_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_fdvibro_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_fdvibro_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_fdvibro_param_7( d ):
	return get_cab_sim( d )


def set_fdvibro_param_7( d, v ):
	return set_cab_sim( d, v )


def get_fdvibro_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_fdvibro_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_usblues_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_usblues_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_usblues_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_usblues_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_usblues_param_2( d ):
	return get_max_150( d )


def set_usblues_param_2( d, v ):
	return set_max_150( d, v )


def get_usblues_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_usblues_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_usblues_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_usblues_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_usblues_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_usblues_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_usblues_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_usblues_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_usblues_param_7( d ):
	return get_cab_sim( d )


def set_usblues_param_7( d, v ):
	return set_cab_sim( d, v )


def get_usblues_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_usblues_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_vxcombo_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_vxcombo_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_vxcombo_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_vxcombo_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_vxcombo_param_2( d ):
	return get_max_150( d )


def set_vxcombo_param_2( d, v ):
	return set_max_150( d, v )


def get_vxcombo_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_vxcombo_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_vxcombo_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_vxcombo_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_vxcombo_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_vxcombo_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_vxcombo_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_vxcombo_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_vxcombo_param_7( d ):
	return get_cab_sim( d )


def set_vxcombo_param_7( d, v ):
	return set_cab_sim( d, v )


def get_vxcombo_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_vxcombo_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_vxjmi_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_vxjmi_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_vxjmi_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_vxjmi_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_vxjmi_param_2( d ):
	return get_max_150( d )


def set_vxjmi_param_2( d, v ):
	return set_max_150( d, v )


def get_vxjmi_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_vxjmi_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_vxjmi_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_vxjmi_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_vxjmi_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_vxjmi_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_vxjmi_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_vxjmi_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_vxjmi_param_7( d ):
	return get_cab_sim( d )


def set_vxjmi_param_7( d, v ):
	return set_cab_sim( d, v )


def get_vxjmi_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_vxjmi_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_bgcrunch_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_bgcrunch_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_bgcrunch_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_bgcrunch_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_bgcrunch_param_2( d ):
	return get_max_150( d )


def set_bgcrunch_param_2( d, v ):
	return set_max_150( d, v )


def get_bgcrunch_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_bgcrunch_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_bgcrunch_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_bgcrunch_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_bgcrunch_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_bgcrunch_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_bgcrunch_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_bgcrunch_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_bgcrunch_param_7( d ):
	return get_cab_sim( d )


def set_bgcrunch_param_7( d, v ):
	return set_cab_sim( d, v )


def get_bgcrunch_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_bgcrunch_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_match30_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_match30_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_match30_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_match30_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_match30_param_2( d ):
	return get_max_150( d )


def set_match30_param_2( d, v ):
	return set_max_150( d, v )


def get_match30_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_match30_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_match30_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_match30_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_match30_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_match30_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_match30_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_match30_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_match30_param_7( d ):
	return get_cab_sim( d )


def set_match30_param_7( d, v ):
	return set_cab_sim( d, v )


def get_match30_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_match30_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_cardrive_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_cardrive_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_cardrive_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_cardrive_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_cardrive_param_2( d ):
	return get_max_150( d )


def set_cardrive_param_2( d, v ):
	return set_max_150( d, v )


def get_cardrive_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_cardrive_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_cardrive_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_cardrive_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_cardrive_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_cardrive_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_cardrive_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_cardrive_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_cardrive_param_7( d ):
	return get_cab_sim( d )


def set_cardrive_param_7( d, v ):
	return set_cab_sim( d, v )


def get_cardrive_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_cardrive_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_twrock_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_twrock_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_twrock_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_twrock_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_twrock_param_2( d ):
	return get_max_150( d )


def set_twrock_param_2( d, v ):
	return set_max_150( d, v )


def get_twrock_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_twrock_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_twrock_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_twrock_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_twrock_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_twrock_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_twrock_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_twrock_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_twrock_param_7( d ):
	return get_cab_sim( d )


def set_twrock_param_7( d, v ):
	return set_cab_sim( d, v )


def get_twrock_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_twrock_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_tonecity_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_tonecity_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_tonecity_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_tonecity_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_tonecity_param_2( d ):
	return get_max_150( d )


def set_tonecity_param_2( d, v ):
	return set_max_150( d, v )


def get_tonecity_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_tonecity_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_tonecity_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_tonecity_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_tonecity_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_tonecity_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_tonecity_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_tonecity_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_tonecity_param_7( d ):
	return get_cab_sim( d )


def set_tonecity_param_7( d, v ):
	return set_cab_sim( d, v )


def get_tonecity_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_tonecity_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_hwstack_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_hwstack_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_hwstack_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_hwstack_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_hwstack_param_2( d ):
	return get_max_150( d )


def set_hwstack_param_2( d, v ):
	return set_max_150( d, v )


def get_hwstack_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_hwstack_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_hwstack_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_hwstack_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_hwstack_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_hwstack_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_hwstack_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_hwstack_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_hwstack_param_7( d ):
	return get_cab_sim( d )


def set_hwstack_param_7( d, v ):
	return set_cab_sim( d, v )


def get_hwstack_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_hwstack_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_tangerine_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_tangerine_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_tangerine_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_tangerine_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_tangerine_param_2( d ):
	return get_max_150( d )


def set_tangerine_param_2( d, v ):
	return set_max_150( d, v )


def get_tangerine_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_tangerine_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_tangerine_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_tangerine_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_tangerine_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_tangerine_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_tangerine_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_tangerine_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_tangerine_param_7( d ):
	return get_cab_sim( d )


def set_tangerine_param_7( d, v ):
	return set_cab_sim( d, v )


def get_tangerine_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_tangerine_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_bbreaker_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_bbreaker_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_bbreaker_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_bbreaker_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_bbreaker_param_2( d ):
	return get_max_150( d )


def set_bbreaker_param_2( d, v ):
	return set_max_150( d, v )


def get_bbreaker_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_bbreaker_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_bbreaker_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_bbreaker_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_bbreaker_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_bbreaker_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_bbreaker_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_bbreaker_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_bbreaker_param_7( d ):
	return get_cab_sim( d )


def set_bbreaker_param_7( d, v ):
	return set_cab_sim( d, v )


def get_bbreaker_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_bbreaker_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_mscrunch_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_mscrunch_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_mscrunch_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_mscrunch_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_mscrunch_param_2( d ):
	return get_max_150( d )


def set_mscrunch_param_2( d, v ):
	return set_max_150( d, v )


def get_mscrunch_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_mscrunch_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_mscrunch_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_mscrunch_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_mscrunch_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_mscrunch_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_mscrunch_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_mscrunch_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_mscrunch_param_7( d ):
	return get_cab_sim( d )


def set_mscrunch_param_7( d, v ):
	return set_cab_sim( d, v )


def get_mscrunch_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_mscrunch_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_ms1959_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_ms1959_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_ms1959_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_ms1959_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_ms1959_param_2( d ):
	return get_max_150( d )


def set_ms1959_param_2( d, v ):
	return set_max_150( d, v )


def get_ms1959_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_ms1959_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_ms1959_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_ms1959_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_ms1959_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_ms1959_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_ms1959_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_ms1959_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_ms1959_param_7( d ):
	return get_cab_sim( d )


def set_ms1959_param_7( d, v ):
	return set_cab_sim( d, v )


def get_ms1959_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_ms1959_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_msdrive_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_msdrive_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_msdrive_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_msdrive_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_msdrive_param_2( d ):
	return get_max_150( d )


def set_msdrive_param_2( d, v ):
	return set_max_150( d, v )


def get_msdrive_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_msdrive_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_msdrive_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_msdrive_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_msdrive_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_msdrive_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_msdrive_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_msdrive_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_msdrive_param_7( d ):
	return get_cab_sim( d )


def set_msdrive_param_7( d, v ):
	return set_cab_sim( d, v )


def get_msdrive_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_msdrive_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_bgndrv_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_bgndrv_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_bgndrv_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_bgndrv_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_bgndrv_param_2( d ):
	return get_max_150( d )


def set_bgndrv_param_2( d, v ):
	return set_max_150( d, v )


def get_bgndrv_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_bgndrv_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_bgndrv_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_bgndrv_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_bgndrv_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_bgndrv_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_bgndrv_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_bgndrv_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_bgndrv_param_7( d ):
	return get_cab_sim( d )


def set_bgndrv_param_7( d, v ):
	return set_cab_sim( d, v )


def get_bgndrv_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_bgndrv_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_bgdrive_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_bgdrive_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_bgdrive_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_bgdrive_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_bgdrive_param_2( d ):
	return get_max_150( d )


def set_bgdrive_param_2( d, v ):
	return set_max_150( d, v )


def get_bgdrive_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_bgdrive_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_bgdrive_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_bgdrive_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_bgdrive_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_bgdrive_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_bgdrive_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_bgdrive_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_bgdrive_param_7( d ):
	return get_cab_sim( d )


def set_bgdrive_param_7( d, v ):
	return set_cab_sim( d, v )


def get_bgdrive_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_bgdrive_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_dzdrive_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_dzdrive_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_dzdrive_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_dzdrive_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_dzdrive_param_2( d ):
	return get_max_150( d )


def set_dzdrive_param_2( d, v ):
	return set_max_150( d, v )


def get_dzdrive_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_dzdrive_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_dzdrive_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_dzdrive_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_dzdrive_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_dzdrive_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_dzdrive_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_dzdrive_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_dzdrive_param_7( d ):
	return get_cab_sim( d )


def set_dzdrive_param_7( d, v ):
	return set_cab_sim( d, v )


def get_dzdrive_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_dzdrive_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_alien_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_alien_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_alien_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_alien_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_alien_param_2( d ):
	return get_max_150( d )


def set_alien_param_2( d, v ):
	return set_max_150( d, v )


def get_alien_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_alien_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_alien_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_alien_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_alien_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_alien_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_alien_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_alien_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_alien_param_7( d ):
	return get_cab_sim( d )


def set_alien_param_7( d, v ):
	return set_cab_sim( d, v )


def get_alien_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_alien_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_revo1_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_revo1_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_revo1_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_revo1_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_revo1_param_2( d ):
	return get_max_150( d )


def set_revo1_param_2( d, v ):
	return set_max_150( d, v )


def get_revo1_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_revo1_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_revo1_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_revo1_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_revo1_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_revo1_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_revo1_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_revo1_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_revo1_param_7( d ):
	return get_cab_sim( d )


def set_revo1_param_7( d, v ):
	return set_cab_sim( d, v )


def get_revo1_param_8( d ):
	return ((d[19] & 0x08) >> 1) | ((d[19] & 0x04) >> 1) | ((d[19] & 0x02) >> 1)


def set_revo1_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x04) << 1)
		retval[19] |= ((v & 0x02) << 1)
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_tremelo_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_tremelo_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_tremelo_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_tremelo_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_tremelo_param_2( d ):
	return get_max_150( d )


def set_tremelo_param_2( d, v ):
	return set_max_150( d, v )


def get_tremelo_param_3( d ):
	return ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_tremelo_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval




def get_slicer_param_0( d ):
	return ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_slicer_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_slicer_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_slicer_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_slicer_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_slicer_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_slicer_param_3( d ):
	return ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_slicer_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_slicer_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_slicer_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_phaser_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_phaser_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_phaser_param_1( d ):
	return ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_phaser_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_phaser_param_2( d ):
	return get_max_150( d )


def set_phaser_param_2( d, v ):
	return set_max_150( d, v )




def get_duophase_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_duophase_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_duophase_param_1( d ):
	return ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_duophase_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_duophase_param_2( d ):
	return get_max_150( d )


def set_duophase_param_2( d, v ):
	return set_max_150( d, v )


def get_duophase_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_duophase_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_duophase_param_4( d ):
	return ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_duophase_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_duophase_param_5( d ):
	return ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_duophase_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_duophase_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_duophase_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_duophase_param_7( d ):
	return ((d[15] & 0x08) << 3) | ((d[15] & 0x04) << 3) | ((d[15] & 0x02) << 3) | ((d[15] & 0x01) << 3) | ((d[8] & 0x02) << 1) | ((d[14] & 0x40) >> 5) | ((d[14] & 0x20) >> 5)


def set_duophase_param_7( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[15] |= ((v & 0x40) >> 3)
		retval[15] |= ((v & 0x20) >> 3)
		retval[15] |= ((v & 0x10) >> 3)
		retval[15] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) >> 1)
		retval[14] |= ((v & 0x02) << 5)
		retval[14] |= ((v & 0x01) << 5)
	return retval




def get_vibrato_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_vibrato_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_vibrato_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_vibrato_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_vibrato_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_vibrato_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_vibrato_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_vibrato_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_vibrato_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_vibrato_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_thevibe_param_0( d ):
	return ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_thevibe_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_thevibe_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_thevibe_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_thevibe_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_thevibe_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_thevibe_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_thevibe_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_thevibe_param_4( d ):
	return ((d[11] & 0x20) >> 5)


def set_thevibe_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_thevibe_param_5( d ):
	return ((d[13] & 0x10) << 3) | ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_thevibe_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x80) >> 3)
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_detune_param_0( d ):
	return ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_detune_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_detune_param_1( d ):
	return ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_detune_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_detune_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_detune_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_detune_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_detune_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_detune_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_detune_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_chorus_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_chorus_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_chorus_param_1( d ):
	return ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_chorus_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_chorus_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_chorus_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_chorus_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_chorus_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_chorus_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_chorus_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_stereocho_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_stereocho_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_stereocho_param_1( d ):
	return ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_stereocho_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_stereocho_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_stereocho_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_stereocho_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_stereocho_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_stereocho_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_stereocho_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_ensemble_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_ensemble_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_ensemble_param_1( d ):
	return ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_ensemble_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_ensemble_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_ensemble_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_ensemble_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_ensemble_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_ensemble_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_ensemble_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_supercho_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_supercho_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_supercho_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_supercho_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_supercho_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_supercho_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_supercho_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_supercho_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_supercho_param_4( d ):
	return ((d[11] & 0x20) >> 5)


def set_supercho_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_coronatri_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_coronatri_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_coronatri_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_coronatri_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_coronatri_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_coronatri_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_coronatri_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[8] & 0x10) >> 2) | ((d[8] & 0x08) >> 1) | ((d[8] & 0x02) << 1) | ((d[8] & 0x01) << 2) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_coronatri_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_coronatri_param_4( d ):
	return ((d[11] & 0x20) >> 5)


def set_coronatri_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_flanger_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_flanger_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_flanger_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_flanger_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_flanger_param_2( d ):
	return (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_flanger_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_flanger_param_3( d ):
	return ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_flanger_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_flanger_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_flanger_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_flanger_param_5( d ):
	return ((d[13] & 0x10) << 3) | ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_flanger_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x80) >> 3)
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_vinflngr_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_vinflngr_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_vinflngr_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_vinflngr_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_vinflngr_param_2( d ):
	return (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_vinflngr_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_vinflngr_param_3( d ):
	return ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_vinflngr_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_vinflngr_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_vinflngr_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_vinflngr_param_5( d ):
	return ((d[13] & 0x10) << 3) | ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_vinflngr_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x80) >> 3)
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_octave_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_octave_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_octave_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_octave_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_octave_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_octave_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_octave_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_octave_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_octave_param_4( d ):
	return ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_octave_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_octave_param_5( d ):
	return ((d[13] & 0x10) << 3) | ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_octave_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x80) >> 3)
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_pitchshft_param_0( d ):
	return ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_pitchshft_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_pitchshft_param_1( d ):
	return ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_pitchshft_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_pitchshft_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_pitchshft_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_pitchshft_param_3( d ):
	return ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_pitchshft_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_pitchshft_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_pitchshft_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_monopitch_param_0( d ):
	return ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_monopitch_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_monopitch_param_1( d ):
	return ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_monopitch_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_monopitch_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_monopitch_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_monopitch_param_3( d ):
	return ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_monopitch_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_monopitch_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_monopitch_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_hps_param_0( d ):
	return ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_hps_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_hps_param_1( d ):
	return ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_hps_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_hps_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_hps_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_hps_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_hps_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_hps_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_hps_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_bendcho_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_bendcho_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_bendcho_param_1( d ):
	return ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_bendcho_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_bendcho_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_bendcho_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_bendcho_param_3( d ):
	return ((d[10] & 0x20) >> 5)


def set_bendcho_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_bendcho_param_4( d ):
	return ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_bendcho_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_bendcho_param_5( d ):
	return ((d[13] & 0x10) << 3) | ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_bendcho_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x80) >> 3)
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_ringmod_param_0( d ):
	return ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_ringmod_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_ringmod_param_1( d ):
	return ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_ringmod_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_ringmod_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_ringmod_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_ringmod_param_3( d ):
	return ((d[11] & 0x10) << 3) | ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_ringmod_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x80) >> 3)
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval




def get_rotocloset_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_rotocloset_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_rotocloset_param_1( d ):
	return ((d[6] & 0x08) >> 3)


def set_rotocloset_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_rotocloset_param_2( d ):
	return get_max_150( d )


def set_rotocloset_param_2( d, v ):
	return set_max_150( d, v )


def get_rotocloset_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_rotocloset_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval




def get_bitcrush_param_0( d ):
	return ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_bitcrush_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_bitcrush_param_1( d ):
	return ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_bitcrush_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_bitcrush_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_bitcrush_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_bitcrush_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_bitcrush_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_bitcrush_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_bitcrush_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval




def get_bomber_param_0( d ):
	return ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_bomber_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_bomber_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_bomber_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_bomber_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_bomber_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_bomber_param_3( d ):
	return ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_bomber_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_bomber_param_4( d ):
	return ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_bomber_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_bomber_param_5( d ):
	return ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_bomber_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_bomber_param_6( d ):
	return ((d[14] & 0x10) << 3) | ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_bomber_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x80) >> 3)
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval




def get_zorgan_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_zorgan_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_zorgan_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_zorgan_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_zorgan_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_zorgan_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_zorgan_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_zorgan_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_zorgan_param_4( d ):
	return ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_zorgan_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_zorgan_param_5( d ):
	return ((d[13] & 0x10) << 3) | ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_zorgan_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x80) >> 3)
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_delay_param_0( d ):
	return ((d[6] & 0x02) << 10) | ((d[6] & 0x01) << 10) | ((d[0] & 0x04) << 7) | ((d[5] & 0x40) << 2) | ((d[5] & 0x20) << 2) | ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_delay_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x800) >> 10)
		retval[6] |= ((v & 0x400) >> 10)
		retval[0] |= ((v & 0x200) >> 7)
		retval[5] |= ((v & 0x100) >> 2)
		retval[5] |= ((v & 0x80) >> 2)
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_delay_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_delay_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_delay_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_delay_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_delay_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_delay_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_delay_param_4( d ):
	return ((d[11] & 0x20) >> 5)


def set_delay_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_delay_param_5( d ):
	return ((d[13] & 0x10) << 3) | ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_delay_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x80) >> 3)
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_delay_param_6( d ):
	return ((d[13] & 0x20) >> 5)


def set_delay_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x01) << 5)
	return retval




def get_carbondelay_param_0( d ):
	return ((d[0] & 0x04) << 7) | ((d[5] & 0x40) << 2) | ((d[5] & 0x20) << 2) | ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_carbondelay_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[0] |= ((v & 0x200) >> 7)
		retval[5] |= ((v & 0x100) >> 2)
		retval[5] |= ((v & 0x80) >> 2)
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_carbondelay_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_carbondelay_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_carbondelay_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_carbondelay_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_carbondelay_param_3( d ):
	return ((d[10] & 0x20) >> 5)


def set_carbondelay_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_carbondelay_param_4( d ):
	return ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_carbondelay_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_carbondelay_param_5( d ):
	return ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_carbondelay_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_carbondelay_param_6( d ):
	return ((d[13] & 0x20) >> 5)


def set_carbondelay_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_carbondelay_param_7( d ):
	return ((d[15] & 0x01) << 3) | ((d[8] & 0x02) << 1) | ((d[14] & 0x40) >> 5) | ((d[14] & 0x20) >> 5)


def set_carbondelay_param_7( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[15] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) >> 1)
		retval[14] |= ((v & 0x02) << 5)
		retval[14] |= ((v & 0x01) << 5)
	return retval




def get_stompdly_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_stompdly_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_stompdly_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_stompdly_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_stompdly_param_2( d ):
	return ((d[10] & 0x02) << 8) | ((d[10] & 0x01) << 8) | ((d[8] & 0x40) << 1) | (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_stompdly_param_2( d, v ):
	return set_max_150( d, v )


def get_stompdly_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_stompdly_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_stompdly_param_4( d ):
	return ((d[11] & 0x20) >> 5)


def set_stompdly_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_stompdly_param_5( d ):
	return ((d[12] & 0x20) >> 5)


def set_stompdly_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_stompdly_param_6( d ):
	return ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_stompdly_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval




def get_tapeecho_param_0( d ):
	return ((d[6] & 0x01) << 10) | ((d[0] & 0x04) << 7) | ((d[5] & 0x40) << 2) | ((d[5] & 0x20) << 2) | ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_tapeecho_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x400) >> 10)
		retval[0] |= ((v & 0x200) >> 7)
		retval[5] |= ((v & 0x100) >> 2)
		retval[5] |= ((v & 0x80) >> 2)
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_tapeecho_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_tapeecho_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_tapeecho_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_tapeecho_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_tapeecho_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_tapeecho_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_tapeecho_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_tapeecho_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_tapeecho_param_5( d ):
	return ((d[12] & 0x20) >> 5)


def set_tapeecho_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_reversedelay_param_0( d ):
	return ((d[6] & 0x01) << 10) | ((d[0] & 0x04) << 7) | ((d[5] & 0x40) << 2) | ((d[5] & 0x20) << 2) | ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_reversedelay_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x400) >> 10)
		retval[0] |= ((v & 0x200) >> 7)
		retval[5] |= ((v & 0x100) >> 2)
		retval[5] |= ((v & 0x80) >> 2)
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_reversedelay_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_reversedelay_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_reversedelay_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_reversedelay_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_reversedelay_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_reversedelay_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_reversedelay_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_reversedelay_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_reversedelay_param_5( d ):
	return ((d[12] & 0x20) >> 5)


def set_reversedelay_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_multitapdelay_param_0( d ):
	return ((d[6] & 0x02) << 10) | ((d[6] & 0x01) << 10) | ((d[0] & 0x04) << 7) | ((d[5] & 0x40) << 2) | ((d[5] & 0x20) << 2) | ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_multitapdelay_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x800) >> 10)
		retval[6] |= ((v & 0x400) >> 10)
		retval[0] |= ((v & 0x200) >> 7)
		retval[5] |= ((v & 0x100) >> 2)
		retval[5] |= ((v & 0x80) >> 2)
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_multitapdelay_param_1( d ):
	return ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_multitapdelay_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_multitapdelay_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_multitapdelay_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_multitapdelay_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_multitapdelay_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_multitapdelay_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_multitapdelay_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_multitapdelay_param_5( d ):
	return ((d[12] & 0x20) >> 5)


def set_multitapdelay_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_filterdly_param_0( d ):
	return ((d[6] & 0x01) << 10) | ((d[0] & 0x04) << 7) | ((d[5] & 0x40) << 2) | ((d[5] & 0x20) << 2) | ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_filterdly_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x400) >> 10)
		retval[0] |= ((v & 0x200) >> 7)
		retval[5] |= ((v & 0x100) >> 2)
		retval[5] |= ((v & 0x80) >> 2)
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_filterdly_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_filterdly_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_filterdly_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_filterdly_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_filterdly_param_3( d ):
	return ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_filterdly_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_filterdly_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_filterdly_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_filterdly_param_5( d ):
	return ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_filterdly_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_filterdly_param_6( d ):
	return ((d[14] & 0x10) << 3) | ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_filterdly_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x80) >> 3)
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_filterdly_param_7( d ):
	return ((d[14] & 0x20) >> 5)


def set_filterdly_param_7( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x01) << 5)
	return retval




def get_pitchdelay_param_0( d ):
	return ((d[6] & 0x01) << 10) | ((d[0] & 0x04) << 7) | ((d[5] & 0x40) << 2) | ((d[5] & 0x20) << 2) | ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_pitchdelay_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x400) >> 10)
		retval[0] |= ((v & 0x200) >> 7)
		retval[5] |= ((v & 0x100) >> 2)
		retval[5] |= ((v & 0x80) >> 2)
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_pitchdelay_param_1( d ):
	return ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_pitchdelay_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_pitchdelay_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_pitchdelay_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_pitchdelay_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_pitchdelay_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_pitchdelay_param_4( d ):
	return ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_pitchdelay_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_pitchdelay_param_5( d ):
	return ((d[13] & 0x10) << 3) | ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_pitchdelay_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x80) >> 3)
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_pitchdelay_param_6( d ):
	return ((d[13] & 0x20) >> 5)


def set_pitchdelay_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x01) << 5)
	return retval




def get_stereodelay_param_0( d ):
	return ((d[6] & 0x01) << 10) | ((d[0] & 0x04) << 7) | ((d[5] & 0x40) << 2) | ((d[5] & 0x20) << 2) | ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_stereodelay_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x400) >> 10)
		retval[0] |= ((v & 0x200) >> 7)
		retval[5] |= ((v & 0x100) >> 2)
		retval[5] |= ((v & 0x80) >> 2)
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_stereodelay_param_1( d ):
	return ((d[7] & 0x20) << 5) | ((d[7] & 0x10) << 5) | ((d[7] & 0x08) << 5) | ((d[7] & 0x04) << 5) | ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_stereodelay_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x400) >> 5)
		retval[7] |= ((v & 0x200) >> 5)
		retval[7] |= ((v & 0x100) >> 5)
		retval[7] |= ((v & 0x80) >> 5)
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_stereodelay_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_stereodelay_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_stereodelay_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_stereodelay_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_stereodelay_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_stereodelay_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_stereodelay_param_5( d ):
	return ((d[13] & 0x10) << 3) | ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_stereodelay_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x80) >> 3)
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_stereodelay_param_6( d ):
	return ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_stereodelay_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_stereodelay_param_7( d ):
	return ((d[15] & 0x08) << 3) | ((d[15] & 0x04) << 3) | ((d[15] & 0x02) << 3) | ((d[15] & 0x01) << 3) | ((d[8] & 0x02) << 1) | ((d[14] & 0x40) >> 5) | ((d[14] & 0x20) >> 5)


def set_stereodelay_param_7( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[15] |= ((v & 0x40) >> 3)
		retval[15] |= ((v & 0x20) >> 3)
		retval[15] |= ((v & 0x10) >> 3)
		retval[15] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) >> 1)
		retval[14] |= ((v & 0x02) << 5)
		retval[14] |= ((v & 0x01) << 5)
	return retval


def get_stereodelay_param_8( d ):
	return ((d[19] & 0x02) >> 1)


def set_stereodelay_param_8( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[19] |= ((v & 0x01) << 1)
	return retval




def get_hdhall_param_0( d ):
	return ((d[5] & 0x20) << 2) | ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_hdhall_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x80) >> 2)
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_hdhall_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_hdhall_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_hdhall_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_hdhall_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_hdhall_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_hdhall_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_hdhall_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_hdhall_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_hdhall_param_5( d ):
	return ((d[12] & 0x20) >> 5)


def set_hdhall_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_hall_param_0( d ):
	return ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_hall_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_hall_param_1( d ):
	return ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_hall_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_hall_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_hall_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_hall_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_hall_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_hall_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_hall_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_hall_param_5( d ):
	return ((d[12] & 0x20) >> 5)


def set_hall_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_room_param_0( d ):
	return ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_room_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_room_param_1( d ):
	return ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_room_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_room_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_room_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_room_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_room_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_room_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_room_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_room_param_5( d ):
	return ((d[12] & 0x20) >> 5)


def set_room_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_tiledrm_param_0( d ):
	return ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_tiledrm_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_tiledrm_param_1( d ):
	return ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_tiledrm_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_tiledrm_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_tiledrm_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_tiledrm_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_tiledrm_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_tiledrm_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_tiledrm_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_tiledrm_param_5( d ):
	return ((d[12] & 0x20) >> 5)


def set_tiledrm_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_arenareverb_param_0( d ):
	return ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_arenareverb_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_arenareverb_param_1( d ):
	return ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_arenareverb_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_arenareverb_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_arenareverb_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_arenareverb_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_arenareverb_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_arenareverb_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_arenareverb_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_arenareverb_param_5( d ):
	return ((d[12] & 0x20) >> 5)


def set_arenareverb_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_plate_param_0( d ):
	return ((d[5] & 0x20) << 2) | ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_plate_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x80) >> 2)
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_plate_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_plate_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_plate_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_plate_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_plate_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_plate_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_plate_param_4( d ):
	return ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_plate_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_plate_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_plate_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_plate_param_6( d ):
	return ((d[13] & 0x20) >> 5)


def set_plate_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_plate_param_7( d ):
	return ((d[15] & 0x10) << 3) | ((d[15] & 0x08) << 3) | ((d[15] & 0x04) << 3) | ((d[15] & 0x02) << 3) | ((d[15] & 0x01) << 3) | ((d[8] & 0x02) << 1) | ((d[14] & 0x40) >> 5) | ((d[14] & 0x20) >> 5)


def set_plate_param_7( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[15] |= ((v & 0x80) >> 3)
		retval[15] |= ((v & 0x40) >> 3)
		retval[15] |= ((v & 0x20) >> 3)
		retval[15] |= ((v & 0x10) >> 3)
		retval[15] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) >> 1)
		retval[14] |= ((v & 0x02) << 5)
		retval[14] |= ((v & 0x01) << 5)
	return retval




def get_spring63_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_spring63_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_spring63_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_spring63_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_spring63_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_spring63_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_spring63_param_3( d ):
	return ((d[11] & 0x10) << 3) | ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_spring63_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x80) >> 3)
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval




def get_air_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_air_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_air_param_1( d ):
	return ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_air_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_air_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_air_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_air_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_air_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_air_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_air_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_air_param_5( d ):
	return ((d[12] & 0x20) >> 5)


def set_air_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_earlyreflection_param_0( d ):
	return ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_earlyreflection_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_earlyreflection_param_1( d ):
	return ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_earlyreflection_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_earlyreflection_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_earlyreflection_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_earlyreflection_param_3( d ):
	return ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_earlyreflection_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_earlyreflection_param_4( d ):
	return ((d[12] & 0x10) << 3) | ((d[12] & 0x08) << 3) | ((d[12] & 0x04) << 3) | ((d[12] & 0x02) << 3) | ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_earlyreflection_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x80) >> 3)
		retval[12] |= ((v & 0x40) >> 3)
		retval[12] |= ((v & 0x20) >> 3)
		retval[12] |= ((v & 0x10) >> 3)
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_earlyreflection_param_5( d ):
	return ((d[12] & 0x20) >> 5)


def set_earlyreflection_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x01) << 5)
	return retval




def get_modreverb_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_modreverb_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_modreverb_param_1( d ):
	return ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_modreverb_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_modreverb_param_2( d ):
	return (d[9] & 0x40) | (d[9] & 0x20) | (d[9] & 0x10) | (d[9] & 0x08) | (d[9] & 0x04) | (d[9] & 0x02) | (d[9] & 0x01)


def set_modreverb_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x40)
		retval[9] |= (v & 0x20)
		retval[9] |= (v & 0x10)
		retval[9] |= (v & 0x08)
		retval[9] |= (v & 0x04)
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_modreverb_param_3( d ):
	return ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_modreverb_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_modreverb_param_4( d ):
	return ((d[12] & 0x01) << 3) | ((d[8] & 0x10) >> 2) | ((d[11] & 0x40) >> 5) | ((d[11] & 0x20) >> 5)


def set_modreverb_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 2)
		retval[11] |= ((v & 0x02) << 5)
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_modreverb_param_5( d ):
	return ((d[13] & 0x08) << 3) | ((d[13] & 0x04) << 3) | ((d[13] & 0x02) << 3) | ((d[13] & 0x01) << 3) | ((d[8] & 0x08) >> 1) | ((d[12] & 0x40) >> 5) | ((d[12] & 0x20) >> 5)


def set_modreverb_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[13] |= ((v & 0x40) >> 3)
		retval[13] |= ((v & 0x20) >> 3)
		retval[13] |= ((v & 0x10) >> 3)
		retval[13] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 1)
		retval[12] |= ((v & 0x02) << 5)
		retval[12] |= ((v & 0x01) << 5)
	return retval


def get_modreverb_param_6( d ):
	return ((d[14] & 0x10) << 3) | ((d[14] & 0x08) << 3) | ((d[14] & 0x04) << 3) | ((d[14] & 0x02) << 3) | ((d[14] & 0x01) << 3) | (d[8] & 0x04) | ((d[13] & 0x40) >> 5) | ((d[13] & 0x20) >> 5)


def set_modreverb_param_6( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x80) >> 3)
		retval[14] |= ((v & 0x40) >> 3)
		retval[14] |= ((v & 0x20) >> 3)
		retval[14] |= ((v & 0x10) >> 3)
		retval[14] |= ((v & 0x08) >> 3)
		retval[8] |= (v & 0x04)
		retval[13] |= ((v & 0x02) << 5)
		retval[13] |= ((v & 0x01) << 5)
	return retval


def get_modreverb_param_7( d ):
	return ((d[14] & 0x20) >> 5)


def set_modreverb_param_7( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[14] |= ((v & 0x01) << 5)
	return retval




def get_particlereverb_param_0( d ):
	return ((d[5] & 0x10) << 2) | ((d[5] & 0x08) << 2) | ((d[5] & 0x04) << 2) | ((d[5] & 0x02) << 2) | ((d[5] & 0x01) << 2) | ((d[0] & 0x08) >> 2) | ((d[4] & 0x40) >> 6)


def set_particlereverb_param_0( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[5] |= ((v & 0x40) >> 2)
		retval[5] |= ((v & 0x20) >> 2)
		retval[5] |= ((v & 0x10) >> 2)
		retval[5] |= ((v & 0x08) >> 2)
		retval[5] |= ((v & 0x04) >> 2)
		retval[0] |= ((v & 0x02) << 2)
		retval[4] |= ((v & 0x01) << 6)
	return retval


def get_particlereverb_param_1( d ):
	return ((d[7] & 0x02) << 5) | ((d[7] & 0x01) << 5) | ((d[0] & 0x02) << 3) | ((d[6] & 0x40) >> 3) | ((d[6] & 0x20) >> 3) | ((d[6] & 0x10) >> 3) | ((d[6] & 0x08) >> 3)


def set_particlereverb_param_1( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[7] |= ((v & 0x40) >> 5)
		retval[7] |= ((v & 0x20) >> 5)
		retval[0] |= ((v & 0x10) >> 3)
		retval[6] |= ((v & 0x08) << 3)
		retval[6] |= ((v & 0x04) << 3)
		retval[6] |= ((v & 0x02) << 3)
		retval[6] |= ((v & 0x01) << 3)
	return retval


def get_particlereverb_param_2( d ):
	return (d[9] & 0x02) | (d[9] & 0x01)


def set_particlereverb_param_2( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[9] |= (v & 0x02)
		retval[9] |= (v & 0x01)
	return retval


def get_particlereverb_param_3( d ):
	return ((d[11] & 0x08) << 3) | ((d[11] & 0x04) << 3) | ((d[11] & 0x02) << 3) | ((d[11] & 0x01) << 3) | ((d[8] & 0x20) >> 3) | ((d[10] & 0x40) >> 5) | ((d[10] & 0x20) >> 5)


def set_particlereverb_param_3( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x40) >> 3)
		retval[11] |= ((v & 0x20) >> 3)
		retval[11] |= ((v & 0x10) >> 3)
		retval[11] |= ((v & 0x08) >> 3)
		retval[8] |= ((v & 0x04) << 3)
		retval[10] |= ((v & 0x02) << 5)
		retval[10] |= ((v & 0x01) << 5)
	return retval


def get_particlereverb_param_4( d ):
	return ((d[11] & 0x20) >> 5)


def set_particlereverb_param_4( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[11] |= ((v & 0x01) << 5)
	return retval


def get_particlereverb_param_5( d ):
	return ((d[12] & 0x20) >> 5)


def set_particlereverb_param_5( d, v ):
	retval = d
	if d:
		retval = d[:]
		retval[12] |= ((v & 0x01) << 5)
	return retval




_funcs = [f for f in _inspect.getmembers( _sys.modules[__name__] ) if _inspect.isfunction( f[1] )]



def get_func( name ):
	retval = None
	global _funcs
	for func in _funcs:
		if name == func[0]:
			retval = func[1]
			break
	return retval


def get_params( d, n ):
	retval = ''
	for loop in range( 9 ):
		func = get_func( 'get_%s_param_%i' % (n, loop) )
		if func:
			if retval:
				retval += ', '
			retval += '%i' % (func( d ))
	return retval


