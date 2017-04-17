Eggbot Sine and Lace Extension
by dnewman

http://www.thingiverse.com/thing:24594

Summary

Sine and Lace is an Inkscape extension intended for use with the Eggbot. It may be used to draw sinusoidal and lace patterns with periods a multiple of the document size. Two curves drawn with the extension may be selected and have a third curve drawn such that it is bounded by the first two curves. In short, the extension is intended for generating some fun patterns for drawing on eggs.

Instructions

Before you can use this extension, you need to download the eggbot_sineandlace.py and eggbot_sineandlace.inx files. Both of those files are contained in the eggbot_sineandlace.zip file which you can download from this page. Open the zip file and place its contents in your local Inkscape extension folder,
~/.config/inkscape/extensions/
on Linux and OS X. On Windows systems, you can place them directly in the Inkscape extension directory. For example, if Inkscape is installed in C:/Program Files/Inkscape then the extension directory will be C:/Program Files/Inkscape/share/extensions.
Once you have placed the two files in the proper directory, exit and then restart Inkscape. The extension should appear under the "Extensions > Eggbot Contributed" menu as "Sine and Lace...".
When using the extension there are eleven fields you can set
Width (pixels) should typically be set to the document's width in pixels. For an Eggbot plot, that's 3200 pixels. However, you can use whatever width you need: the curve will have that width horizontally.
Height (pixels) specifies the vertical peak to trough height of the curve.
Number of cycles (periods) controls the number of periods of the curve form to produce across the specified width.
The field "Start angle at 2 pi (n / m); n = " is used to control the starting phase (angle) of the sine or lace curve. Values of 0 and 1 for n and m = 2 are typical when generating a curve and a version of the same curve 180 degrees out of phase. See the green and blue touching sine waves in the lower half of the sample .svg file: the green one has n=0, m=2 and the blue one n=1, m=2. They were started at different starting y coordinates.
The field "Start angle at 2 pi (n / m); m = " is used to control the starting phase of the sine or lace curve. See the immediately preceding paragraph for mors details.
Recede from envelope is used to scale the amplitude of a curve being bounded by two other curves. The amplitude will be reduced by the specified percentage. This helps alleviate visual issues caused be imprecise pen positioning (slippage) during plotting. For a value of 100, the curve is drawn full (100%) amplitude. For a value of 5%, it will be drawn only 95% of it's full size; i.e., multiplied by a scaling factor of 0.95.
Number of sample points specifies how many points along the curve to sample. In order to get good results, this value needs to be fairly high when drawing lace and the "Spline" check box is checked.
Starting x coordinate (pixels) specifies exactly that: the horizontal page position to begin the curve at.
Starting y coordinate (pixels) is the starting page vertical position to begin the curve at. Keep in mind that with SVG and Inkscape, y=0 is at the top of the document and increasing y values move down towards the document's bottom.
To draw lace, check the "Lace" checkbox. When unchecked, a sine wave is drawn.
To generate a sequence of splines rather than straight line segments, check the "Spline" checkbox. When using splines and drawing lace, the number of sample points needs to be large.
To bound a curve by two previously drawn curves, select the two bounding curves and then select Extensions > Eggbot Contributed > Sine and Lace.... You cannot use a curve which itself was bound by two other curves.