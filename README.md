# Egg Painter Mini (eggbot pro MOD)

<a href="https://github.com/ProbotXYZ/EggBot/blob/master/README_RU.md">На Русском</a>

This is a low-cost version of EggBot, printable 3D printers that accept large (cost of electronic parts only $8 from China without power supply).</br>

<a href="https://youtu.be/MZZwDX_0e_o">YouTube</a></br>
<a href="http://www.thingiverse.com/thing:2245428">Thingiverse.com</a></br>
<a href="http://probot.xyz">Probot.XYZ</a></br>

Read this, it's important!
-------------------

If you are reading this, then you may be looking at the development version of EggBot Pro Mini. This means files may present inconsistencies (dimensions mismatch, lack of tolerances, etc). If you just want to build the machine, take a look at the following locations - <a href="https://github.com/ProbotXYZ/EggBot/releases">Releases</a>

The list of parts to print
-------------------
<a href="https://github.com/ProbotXYZ/EggBot/tree/master/Stl/en">Download this</a></br>
1 x 0000001. Case_Bottom</br>
1 x 0000002. Case_Top</br>
1 x 0000003. Logo</br>
2 x 0000004. M4_Nut_Holder</br>
1 x 0000005. Axis_R</br>
1 x 0000006. Spring_Holder</br>
1 x 0000007. Axis_R_Holder</br>
1 x 0000008. Axis_R_Lock</br>
2 x 0000009. М4_Bolt_Holder_Bottom</br>
2 x 0000010. М4_Bolt_Holder_Top</br>
1 x 0000011. Axis_L_Holder</br>
1 x 0000012. Axis_L</br>
1 x 0000013. Hand_Holder</br>
1 x 0000014. Hand_Holder_Guide</br>
1 x 0000015. Hand_Holder_Guide_Case</br>
1 x 0000016. Hand_H</br>
1 x 0000017. Hand_V</br>
1 x 0000018. Case_Right</br>

Non-printable parts
-------------------
2 x <a href="http://s.click.aliexpress.com/e/72FuNFm">608zz Bearing</a></br>
1 x <a href="http://s.click.aliexpress.com/e/MBeuZb6">24mm Rubber Gasket</a></br>
1 x <a href="http://s.click.aliexpress.com/e/MBeuZb6">15mm Rubber Gasket</a></br>

Screws&Nuts
-------------------
1 x 15x20mm Spring</br>
1 x 2x18mm Iron Nail without a hat</br>
2 x M4x16 Bolt</br>
2 x M4 Nut</br>
8 x M3x12 Screw</br>
5 x M3x16 Screw</br>
12 x M3 Nut</br>
4 x M3 Washer</br>
12 x M2x4 Screw</br>

Electronics
-------------------
1 x <a href="http://s.click.aliexpress.com/e/mMBaiuj">Arduino UNO</a></br>
2 x <a href="http://s.click.aliexpress.com/e/baQjima">ULN2003 Stepper Motor Driver Board</a></br>
2 x <a href="http://s.click.aliexpress.com/e/bYfuF6U">28byj-48-12v Stepper Motor</a></br>
1 x <a href="http://s.click.aliexpress.com/e/aAU3r7e">SG90 Micro Servo</a></br>
1 x <a href="http://s.click.aliexpress.com/e/zbiMrfU">12V DC Power Supply</a></br>
1 x <a href="http://s.click.aliexpress.com/e/6YFYRZR">USB Cable for connect to PC</a></br>
<a href="http://s.click.aliexpress.com/e/IY3rBuf">A few wires</a></br>

Firmware
-------------------
As the firmware used Eggduino. It's arduino firmware for EggBot / Spherebot with Inkscape-Integration (<a href="https://github.com/cocktailyogi/EggDuino">Github</a>).

For Installation:
1) Download and unzip <a href="https://github.com/ProbotXYZ/EggBot/blob/master/Firmware/Firmware.zip">Firmware.zip</a>.
2) Download the ARDUINO IDE here: https://www.arduino.cc/en/Main/Software and install it.
3) Run the software. Select the Arduino UNO board and the proper COM PORT (should be COM5 or so) in the menu "Tools->Board"…
4) Open Eggduino.ino from <a href="https://github.com/ProbotXYZ/EggBot/blob/master/Firmware/Firmware.zip">Firmware.zip</a> and upload the Eggduino code to your Arudino Uno. 

Controlling program
-------------------
As the controlling program used Inkscape software.
1) Download and unzip the Inkscape software <a href="https://github.com/ProbotXYZ/EggBot/blob/master/Software/Software_(inkscape%2Bextension).zip">Software_inkscape+extension.zip</a>.
2) EggBot Control Extension already included in the Inkscape from <a href="https://github.com/ProbotXYZ/EggBot/blob/master/Software/Software_(inkscape%2Bextension).zip">Software_inkscape+extension.zip</a>.
3) Run the software. 

The EggBot Control extension for Inkscape is the tool that you will use to help you test and align the EggBot, as well as transfer your drawings to an egg. Once Inkscape is running, you’ll have an Extensions menu, and on that menu will be a submenu labeled Eggbot. 

Use template EggBot (File->New from Template) for your drawing.

Examples
-------------------
<a href="https://github.com/ProbotXYZ/EggBot/tree/master/Samples">Sample pictures</a>
