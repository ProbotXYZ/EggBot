# Generate a 3200 x 1000 geometrical pattern for Eggbot plotting
# See http://www.egg-bot.com/ for info on the Eggbot
#
# Dan Newman, 1 January 2011
# dan dot newman at mtbaldy dot us
# Public domain (http://creativecommons.org/licenses/publicdomain/)

deltas1 = [[1,3], [1,2], [1,1], [2,1], [3,1], [-1,-3], [-1,-2], [-1,-1], [-2,-1], [-3,-1]]
deltas2 = [[-1,3], [-1,2], [-1,1], [-2,1], [-3,1], [1,-3], [1,-2], [1,-1], [2,-1], [3,-1]]

scale = float(20.0)/float(0.975)
color = "red"

def plate1( x, y ):
    x = float(x) * scale
    y = float(y) * scale
    p = ''
    for d in deltas1:
        if p == '':
            p = 'M '
        else:
            p += ' L '
        p += '%d,%d' % (x, y)
        x += scale * d[0]
        y -= scale * d[1]
    print '<path stroke-width="1" stroke="%s" fill="none" d="%s L %f,%f"/>' % (color, p, x, y)

def plate2( x, y ):
    x = float(x + 8) * scale
    y = float(y) * scale
    p = ''
    for d in deltas2:
        if p == '':
            p = 'M '
        else:
            p += ' L '
        p += '%d,%d' % (x, y)
        x += scale * d[0]
        y -= scale * d[1]
    print '<path stroke-width="1" stroke="%s" fill="none" d="%s L %f,%f"/>' % (color, p, x, y)

color = 'red'
print '<svg xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" width="3200" height="1000">'
print '<g inkscape:groupmode="layer" inkscape:label="1 - %s">' % color

for i in range(0, 13):
    for j in range(0,4):
        plate1(-4 + i*12, j*12 + 8)
for i in range(0, 13):
    for j in range(0,4):
        plate2(-4 + i*12, j*12 + 8)

print '</g>'
color = "green"
print '<g inkscape:groupmode="layer" inkscape:label="2 - %s">' % color

for i in range(0, 13):
    for j in range(1,5):
        plate1(-4 + 4 + i*12, j*12 + 0)
for i in range(0, 13):
    for j in range(1,4):
        plate2(-4 + 4 + i*12, j*12 + 4)

print '</g>'
color = "blue"
print '<g inkscape:groupmode="layer" inkscape:label="3 - %s">' % color

for i in range(0, 13):
    for j in range(2,5):
        plate1(-4 + 8 + i*12, j*12 - 8)
for i in range(0, 13):
    for j in range(1,5):
        plate2(-4 + 8 + i*12, j*12 - 0)
print '</g>'
print '</svg>'
