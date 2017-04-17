# Generate a 3200 x 800 geometrical pattern for Eggbot plotting
# See http://www.egg-bot.com/ for info on the Eggbot
#
# Dan Newman, 2 January 2011
# dan dot newman at mtbaldy dot us
# Public domain (http://creativecommons.org/licenses/publicdomain/)

HEIGHT = float( 800.0 )
WIDTH = float( 3200.0 )

scale = WIDTH / ( 16.0 * 3 )  # 16 horizontal repeats
epsilon = float(1.0e-5)

# Relative moves for drawing the vertical elements
DOWN  = [[0.0, scale], [scale, 2*scale], [0.0, scale], [-scale, 2*scale]]
UP    = [[0.0, -scale], [scale, -2*scale], [0.0, -scale], [-scale, -2*scale]]

# How to switch to going up when you stop going down after DOWN[i]
DU_switch = [scale, -scale, -scale, scale]

# Relative moves for drawing the horizontal elements (L2R = left-to-right)
L2R = [[scale, 0.0], [2*scale, scale], [scale, 0.0], [2*scale, -scale]]
R2L = [[-scale, 0.0], [-2*scale, scale], [-scale, 0.0], [-2*scale, -scale]]

# How to switch to R2L after stopping in L2R at index i
LR_switch = [scale, -scale, -scale, scale]

# Compute the intersection of two lines
# See eggbot_hatch.py for complete details

def intersect( P1, P2, P3, P4 ):

	'''
	Determine if two line segments defined by the four points P1 & P2 and
	P3 & P4 intersect.  If they do intersect, then return the fractional
	point of intersection "sa" along the first line at which the
	intersection occurs.
	'''

	# Precompute these values -- note that we're basically shifting from
	#
	#		P = P1 + s (P2 - P1)
	#
	# to
	#
	# 		P = P1 + s D
	#
	# where D is a direction vector.  The solution remains the same of
	# course.  We'll just be computing D once for each line rather than
	# computing it a couple of times.

	D21x = P2[0] - P1[0]
	D21y = P2[1] - P1[1]
	D43x = P4[0] - P3[0]
	D43y = P4[1] - P3[1]

	# Denominator
	d = D21x * D43y - D21y * D43x

	# Return now if the denominator is zero
	if d == 0:
		return float( -1 )

	# For our purposes, the first line segment given
	# by P1 & P2 is the LONG hatch line running through
	# the entire drawing.  And, P3 & P4 describe the
	# usually much shorter line segment from a polygon.
	# As such, we compute sb first as it's more likely
	# to indicate "no intersection".  That is, sa is
	# more likely to indicate an intersection with a
	# much a long line containing P3 & P4.

	nb = ( P1[1] - P3[1] ) * D21x - ( P1[0] - P3[0] ) * D21y

	# Could first check if abs(nb) > abs(d) or if
	# the signs differ.
	sb = float( nb ) / float( d )
	if ( sb < 0 ) or ( sb > 1 ):
		return float( -1 )

	na = ( P1[1] - P3[1] ) * D43x -  ( P1[0] - P3[0] ) * D43y
	sa = float( na ) / float( d )
	if ( sa < 0 ) or ( sa > 1 ):
		return float( -1 )

	return sa

# Determine whether a line segment needs to be clipped to
# fit within the drawing page

def clip( x1, y1, x2, y2 ):
	if ( x1 >= 0.0 ) and ( x1 <= WIDTH ) and ( x2 >= 0.0 ) and ( x2 <= WIDTH ) and \
			( y1 >= 0.0 ) and ( y1 <= HEIGHT ) and ( y2 >= 0.0 ) and ( y2 <= HEIGHT ):
		return float( -1.0 )

	if ( x1 < 0.0 ) or ( x2 < 0.0 ):
		s = intersect( [x1, y1], [x2, y2], [0.0, 0.0], [0.0, HEIGHT] )
		if ( s > 0.0 ):
			return s

	if ( x1 > WIDTH ) or ( x2 > WIDTH ):
		# We allow going an extra pixel across in case there is drawing error
		s = intersect( [x1, y1], [x2, y2], [WIDTH+1.0, 0.0], [WIDTH+1.0, HEIGHT] )
		if ( s > 0.0 ):
			return s

	if ( y1 < 0.0 ) or ( y2 < 0.0 ):
		s = intersect( [x1, y1], [x2, y2], [0.0, 0.0], [WIDTH, 0.0] )
		if ( s > 0.0 ):
			return s

	if ( y1 > HEIGHT ) or ( y2 > HEIGHT ):
		s = intersect( [x1, y1], [x2, y2], [0.0, HEIGHT], [WIDTH, HEIGHT] )
		if ( s > 0.0 ):
			return s

	return float( -1.0 )

# Plot a collection of line segments

def plot( points, color='black' ):

	# First line segment
	s = clip( points[0][0], points[0][1], points[1][0], points[1][1] )
	if ( s < 0.0 ):
		p = 'M %f,%f' % ( points[0][0], points[0][1] )
	else:
		p = 'M %f,%f' % ( points[0][0] + s * ( points[1][0] - points[0][0] ),
						  points[0][1] + s * ( points[1][1] - points[0][1] ) )
	x0 = points[1][0]
	y0 = points[1][1]
	p += ' L %f,%f' % ( x0, y0 )

	# Intermediate line segments
	for i in range(2, len( points ) - 1):
		x0 = points[i][0]
		y0 = points[i][1]
		p += ' L %f,%f' % ( x0, y0 )

	# Final line segment
	x = points[-1][0]
	y = points[-1][1]
	s = clip( x0, y0, x, y )
	if ( s < 0.0 ):
		p += ' L %f,%f' % ( x, y )
	else:
		p += ' L %f,%f' % ( x0 + s * ( x - x0 ), y0 + s * ( y - y0 ) )

	print '<path stroke="%s" stroke-width="1" fill="none" d="%s"/>' % ( color, p )

# Draw the vertical elements

def vertical( x, y, color, down, up ):

	if ( y > ( scale + epsilon ) ):
		i = len( down ) - 1
		while ( y > ( scale + epsilon) ):
			x -= down[i][0]
			y -= down[i][1]
			i -= 1
			if ( i < 0 ):
				i = len( down ) - 1
	else:
		i = -1

	points = [[x, y]]
	while ( y < ( HEIGHT - epsilon ) ):
		i += 1
		if ( i >= len( down ) ):
			i = 0
		x += down[i][0]
		y += down[i][1]
		points.append( [x, y] )

	plot( points, color )

	x += DU_switch[i]
	points = [[x, y]]
	while ( y > epsilon ):
		x += up[i][0]
		y += up[i][1]
		points.append( [x, y] )
		i -= 1
		if ( i < 0 ):
			i = len( up ) - 1

	plot( points, color )

# Draw the horizontal elements

def horizontal( x, y, color, l2r, r2l ):

	if ( x > ( scale + epsilon ) ):
		i = len( l2r ) - 1
		while ( x > ( scale + epsilon ) ):
			x -= l2r[i][0]
			y -= l2r[i][1]
			i -= 1
			if ( i < 0 ):
				i = len( l2r ) - 1
	else:
		i = -1

	points = [[x, y]]
	while ( x < ( WIDTH - epsilon ) ):
		i += 1
		if ( i >= len( l2r ) ):
			i = 0
		x += l2r[i][0]
		y += l2r[i][1]
		points.append( [x, y] )

	plot( points, color )

	y += LR_switch[i]
	points = [[x, y]]
	while ( x > epsilon ):
		x += r2l[i][0]
		y += r2l[i][1]
		points.append( [x, y] )
		i -= 1
		if ( i < 0 ):
			i = len( r2l ) - 1

	plot( points, color )

print '<svg xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" width="%d" height="%d">' % ( int( WIDTH ), int( HEIGHT ) )
print '<g inkscape:groupmode="layer" inkscape:label="1 - vertical">'

Color = 'green'
x1 = 0.0
y1 = 0.0
x2 = 1.5 * scale
y2 = 1.5 * scale
while ( x1 < ( WIDTH - epsilon ) ):
	vertical( x1, y1, 'green', DOWN, UP )
	if ( x2 < ( WIDTH - epsilon ) ):
		vertical( x2, y2, 'green', DOWN, UP )
	x1 += 3 * scale
	x2 += 3 * scale

print '</g>'
print '<g inkscape:groupmode="layer" inkscape:label="2 - horizontal">'

x1 = 0.0
y1 = 0.0
x2 = 1.5 * scale
y2 = 1.5 * scale
while ( y1 < ( HEIGHT - epsilon ) ):
	horizontal( x1, y1, 'blue', L2R, R2L)
	if ( y2 < ( HEIGHT - epsilon ) ):
		horizontal( x2, y2, 'blue', L2R, R2L)
	y1 += 3 * scale
	y2 += 3 * scale

print '</g>'
print '<g inkscape:groupmode="layer" inkscape:label="3 - border">'
print '<path stroke="black" stroke-width="1" fill="none" d="M 0,0 l %d,0"/>' % ( int( WIDTH ) )
print '<path stroke="black" stroke-width="1" fill="none" d="M 0,%d l %d,0"/>' % ( int( HEIGHT ), int( WIDTH ) )
print '</g>'
print '</svg>'
