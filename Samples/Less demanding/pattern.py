#!/usr/bin/env python

# pattern.py

# Generate an SVG document containing a geometric pattern intended for
# plotting with the Eggbot, http://www.egg-bot.com/ .

# Written by Daniel C. Newman
# dan dot newman at mtbaldy dot us
# 30 January 2011

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import sys

# Relative offsets to move (draw) from point to point

Points = [ [-0.5, 1.0], [-1.0, 0.5], [1.0, 0.5],
	   [0.5, 1.0], [0.5, -1.0], [1.0, -0.5], [-1.0, -0.5],
	   [-1.0, 0.0], [0.0, 1.0], [1.0, 0.0], [0.0, -1.0],
	   [-0.5, -1.0] ]

# Document height x width
Height = 1200
Width  = 3200

# Number of "stars" to draw horizontally across in the top row
answer = raw_input( 'Number of "stars" across the top row [20]: ' ).strip()
if answer == '':
	answer = '20'
try:
	NStarsAcross = int( answer )
except:
	print 'Cannot interpret "%s" as an integer; bye' % answer
	sys.exit(1)

if NStarsAcross <= 0:
	print 'Zero?  Okay, bye then'
	sys.exit(0)

answer = raw_input( 'Compress vertically for plotting on eggs [yes]? ' ).strip().lower()
if ( answer == '' ) or ( answer[1] == 'y' ):
	rescale = True
else:
	rescale = False

answer = raw_input( 'Output file [pattern.svg]: ' ).strip()
if answer == '':
	answer = 'pattern.svg'
try:
	f = open( answer, 'w' )
except:
	print 'Unable to open the file "%s"; bye' % answer
	sys.exit(1)

# Derived values
ScaleX = float( Width ) / float( 3 * NStarsAcross )
if rescale:
	ScaleY = ScaleX * 0.6666666 * 0.95
	Height = int( Height * 0.6666666 * 0.95 )
else:
	ScaleY = ScaleX

NStarsDown = int( Height / ( ScaleY * 3 ) )

def draw_star( tx=0.0, ty=0.0 ):

	path = 'M %f,%f' % ( tx, ty )
	for P in Points:
		path += ' l %f,%f' % ( P[0], P[1] )

	f.write( '<path d="M %s"/>\n' % path[2:] )

f.write(
'<svg xmlns="http://www.w3.org/2000/svg"\n' +
'     xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"\n' +
'     width="%d" height="%d">\n' % ( Width, Height ) )

color = 'black'

f.write('<g inkscape:groupmode="layer" inkscape:label="2 - %s"\n' % color )
f.write('   transform="scale(%f,%f)" fill="none" stroke="%s"\n' % ( ScaleX, ScaleY, color ) )
f.write('   stroke-width="%f">\n' % ( 1.0 / ScaleX ) )

for ix in range( 0, NStarsAcross ):
	x = float( ix ) * 3.0
	for iy in range( 0, NStarsDown ):
		y = float( iy ) * 3.0
		draw_star( x, y )
	for iy in range( NStarsDown - 1, -1, -1):
		y = float( iy ) * 3.0
		draw_star( x + 1.5, y + 1.5)

f.write( '</g>\n</svg>\n' )
f.close()
