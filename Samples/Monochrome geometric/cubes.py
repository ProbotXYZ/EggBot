import math

L = math.sqrt(5)
v0 = [ [0.0, 0.0], [2.0, -1.0], [4.0,   0.0], [2.0, 1.0] ]
e0 = [ [0.0, 0.0], [2.0, -1.0], [2.0,   1.0], [4.0, 0.0] ]

v1 = [ [0.0, 0.0], [2.0,  1.0], [2.0, L+1.0], [0.0,   L] ]
e1 = [ [0.0, 0.0], [2.0,  1.0], [0.0, L],     [2.0, L+1.0] ]

v2 = [ [4.0, 0.0], [4.0,    L], [2.0, L+1.0], [2.0, 1.0] ]
e2 = [ [4.0, 0.0], [4.0,    L], [2.0, 1.0], [2.0, L+1.0] ]

e3 = [ [-2.0, -1.0], [0.0, 0.0], [0.0, -2.0], [2.0, -1.0] ]

color = 'black'
polygons = [ v0, v1, v2 ]
edge_sets = [ e0, e1, e2, e3 ]

H = float( L + 1.0 - ( -1.0 ) )
W = float( 4.0 )
S = float( 40.0 )

def shrink_line( x0, y0, x1, y1, s=0.05 ):

	dx = x1 - x0
	dy = y1 - y0

	xx0 = x0 + s * dx
	xx1 = x0 + ( 1.0 - s ) * dx
	yy0 = y0 + s * dy
	yy1 = y0 + ( 1.0 - s ) * dy

	return xx0, yy0, xx1, yy1

def draw_outlines( tx=0.0, ty=0.0, face=0 ):

	path = ''
	edges = edge_sets[face]
	i = 0
	j = 1
	if face == 1:
		i = 2
		j = 3
	print '<path d="M %f,%f L %f,%f"/>' % ( S * ( tx + edges[i][0] ),
						S * ( ty + edges[i][1] ),
						S * ( tx + edges[j][0] ),
						S * ( ty + edges[j][1] ) )

def draw_hashes( tx=0.0, ty=0.0, face=0, steps=3 ):

	path = ''
	edges = edge_sets[face]

	L0x = edges[0][0]
	L0y = edges[0][1]
	d0x = edges[1][0] - L0x
	d0y = edges[1][1] - L0y

	L1x = edges[2][0]
	L1y = edges[2][1]
	d1x = edges[3][0] - L1x
	d1y = edges[3][1] - L1y

	if steps <= 1:
		steps = 2

	step = 1.0 / float( steps - 1 )

	for i in range(0, steps):

		if ( face == 3 ) and ( ( i == 0 ) or ( i == steps ) ):
			continue

		x0 = S * ( tx + L0x + i * step * d0x )
		y0 = S * ( ty + L0y + i * step * d0y )
		x1 = S * ( tx + L1x + i * step * d1x )
		y1 = S * ( ty + L1y + i * step * d1y )

		if 0 == ( i % 2 ):
			x0, y0, x1, y1 = shrink_line( x0, y0, x1, y1, 0.05 )
		else:
			x1, y1, x0, y0 = shrink_line( x0, y0, x1, y1, 0.05 )
		path += 'L %f,%f L %f,%f ' % ( x0, y0, x1, y1 )

	print '<path d="M %s"/>' % path[2:]


print '<svg xmlns="http://www.w3.org/2000/svg"'
print '     xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"'
print '     width="3200" height="1200">'

color = 'red'
print "  <g inkscape:groupmode='layer' inkscape:label='1 - %s'" % color
print "     fill='none' stroke='%s' stroke-width='1'>" % color

for i in range( 0, 20 ):
	x0 = i * 4.0
	for j in range( 0, 9 ):
		x = x0 + j * 2.0
		y = j * ( L + 1.0 )
		if j == 0:
			draw_outlines( x, y, 0 )
		draw_hashes( x, y, 0, 4 )
		draw_hashes( x, y, 1, 5 )
		draw_hashes( x, y, 2, 6 )
		if j == 8:
			draw_outlines( x, y, 1 )
print '  </g>'

print '</svg>'
