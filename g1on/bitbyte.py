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


def move_bits( e, mask, shift, indexfrom, indexto ):
	if e:
		tmpfrom = e[indexfrom] & mask
		e[indexfrom] &= (0xff ^ mask)
		if shift > 0:
			tmpfrom <<= shift
		elif shift < 0:
			tmpfrom >>= -shift
		e[indexto] |= tmpfrom


def swap_bits( e, mask, shift, indexfrom, indexto ):
	if e:
		tmpfrom = e[indexfrom] & mask
		e[indexfrom] &= (0xff ^ mask)
		if shift > 0:
			mask <<= shift
		elif shift < 0:
			mask >>= -shift
		tmpto = e[indexto] & mask
		e[indexto] &= (0xff ^ mask)
		if shift > 0:
			tmpfrom <<= shift
			tmpto >>= shift
		elif shift < 0:
			tmpfrom >>= -shift
			tmpto <<= -shift
		e[indexfrom] |= tmpto
		e[indexto] |= tmpfrom


def throw_bits( ea, eb, mask, shift, indexfrom, indexto ):
	if ea and eb:
		tmp = ea[indexfrom] & mask
		ea[indexfrom] &= (0xff ^ mask)
		if shift > 0:
			tmp <<= shift
		elif shift < 0:
			tmp >>= -shift
		eb[indexto] |= tmp


def exchange_bits( ea, eb, mask, shift, indexfrom, indexto ):
	if ea and eb:
		tmpa = ea[indexfrom] & mask
		ea[indexfrom] &= (0xff ^ mask)
		if shift > 0:
			mask <<= shift
		elif shift < 0:
			mask >>= -shift
		tmpb = eb[indexto] & mask
		eb[indexto] &= (0xff ^ mask)
		if shift > 0:
			tmpa <<= shift
			tmpb >>= shift
		elif shift < 0:
			tmpa >>= -shift
			tmpb <<= -shift
		ea[indexfrom] |= tmpb
		eb[indexto] |= tmpa


def move_byte( e, indexfrom, indexto ):
	if e:
		tmp = e[indexfrom]
		del e[indexfrom]
		e.insert( indexto, tmp )


def swap_byte( e, indexfrom, indexto ):
	if e:
		tmp = e[indexfrom]
		e[indexfrom] = e[indexto]
		e[indexto] = tmp


def throw_byte( ea, eb, indexfrom, indexto ):
	if ea and eb:
		tmp = ea[indexfrom]
		ea[indexfrom] = eb[indexto]
		eb[indexto] = tmp

