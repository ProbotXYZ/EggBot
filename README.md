# EggBot Pro Mini
3d-printable budget EggBot

This is a low-cost version of Egg Bot, printable 3D printers that accept large (cost of electronic parts only $8 from China without power supply).

Read this, it's important!
-------------------

If you are reading this, then you may be looking at the development version of EggBot Pro Mini. This means files may present inconsistencies (dimensions mismatch, lack of tolerances, etc). If you just want to build the machine, take a look at the following locations:

Releases: https://github.com/ProbotXYZ/EggBot/releases
YouTube: https://youtu.be/MZZwDX_0e_o

The list of parts to print
-------------------
1 x 0000001.Case_Bottom.stl
1 x 0000002.Case_Top.stl

1 x 0000003. Logo

2 x 0000004. M4_Nut_Holder
1 x 0000005. Axis_R
1 x 0000006. Spring_Holder
1 x 0000007. Axis_R_Holder
1 x 0000008. Axis_R_Lock
2 x 0000009. М4_Bolt_Holder_Bottom
2 x 0000010. М4_Bolt_Holder_Top
1 x 0000011. Axis_L_Holder
1 x 0000012. Axis_L
1 x 0000013. Hand_Holder
1 x 0000014. Hand_Holder_Guide
1 x 0000015. Hand_Holder_Guide_Case
1 x 0000016. Hand_H
1 x 0000017. Hand_V
1 x 0000018. Case_Right

Non-printable parts
-------------------
2 x <a href="http://s.click.aliexpress.com/e/72FuNFm">608zz Bearing</a>
1 x <a href="http://s.click.aliexpress.com/e/MBeuZb6">24mm Rubber Gasket</a>
1 x <a href="http://s.click.aliexpress.com/e/MBeuZb6">15mm Rubber Gasket</a>

Screws&Nuts
-------------------
1 x 15x20mm Spring
1 x 2x18mm Iron Nail without a hat
2 x M4x16 Bolt
2 x M4 Nut
8 x M3x12 Screw
5 x M3x16 Screw
12 x M3 Nut
4 x M3 Washer
12 x M2x4 Screw

Electronics
-------------------
1 x <a href="http://s.click.aliexpress.com/e/mMBaiuj">Arduino UNO</a>
2 x <a href="http://s.click.aliexpress.com/e/baQjima">ULN2003 Stepper Motor Driver Board</a>
2 x <a href="http://s.click.aliexpress.com/e/bYfuF6U">28byj-48-12v Stepper Motor</a>
1 x <a href="http://s.click.aliexpress.com/e/aAU3r7e">SG90 Micro Servo</a>
1 x <a href="http://s.click.aliexpress.com/e/zbiMrfU">12V DC Power Supply</a>
1 x <a href="http://s.click.aliexpress.com/e/6YFYRZR">USB Cable for connect to PC</a>
<a href="http://s.click.aliexpress.com/e/IY3rBuf">A few wires</a>

Firmware
-------------------
As the firmware used Eggduino. It's arduino firmware for EggBot / Spherebot with Inkscape-Integration (<a href="https://github.com/cocktailyogi/EggDuino">Github</a>).

For Installation:
1) Download and unzip <a href="http://www.thingiverse.com/download:3568252">Firmware.zip</a>.
2) Download the ARDUINO IDE here: https://www.arduino.cc/en/Main/Software and install it.
3) Run the software. Select the Arduino UNO board and the proper COM PORT (should be COM5 or so) in the menu "Tools->Board"…
4) Open Eggduino.ino from Firmware.zip and upload the Eggduino code to your Arudino Uno. 

Controlling program
-------------------
As the controlling program used Inkscape software.
1) Download and unzip the Inkscape software <a href="http://www.thingiverse.com/download:3571507">Software_inkscape+extension.zip</a>.
2) EggBot Control Extension already included in the Inkscape from <a href="http://www.thingiverse.com/download:3571507">Software_inkscape+extension.zip</a>.
3) Run the software. 

The EggBot Control extension for Inkscape is the tool that you will use to help you test and align the EggBot, as well as transfer your drawings to an egg. Once Inkscape is running, you’ll have an Extensions menu, and on that menu will be a submenu labeled Eggbot. 

Use template EggBot (File->New from Template) for your drawing.
