# Яйцебот Про Мини
<p align="center">
<img src="EggPainter.png" width="70%">
<div align="center"><i>3d-печатный бюджетный яйцебот.</i></div>
</p>  

<a href="https://github.com/ProbotXYZ/EggBot/blob/master/README.md">On English</a>

Ссылки
-------------------
<a href="https://youtu.be/MZZwDX_0e_o">YouTube</a></br>
<a href="http://www.thingiverse.com/thing:2245428">Thingiverse.com</a></br>
<a href="http://probot.xyz">Probot.XYZ</a></br>
<a href="http://egg-bot.com/">Оригинальный EggBot</a>


Прочтите, это важно!
-------------------

Это хранилище разработки проекта. Некоторые файлы могут находится не в консистентном состоянии. Если вы хотите создать устройство самостоятельно, то смотрите <a href="https://github.com/ProbotXYZ/EggBot/releases">релизы.</a>

Cписок деталей и количество, которое нужно напечатать:
-------------------
<a href="https://github.com/ProbotXYZ/EggBot/tree/master/Stl/ru">Загрузите отсюда</a></br>
1 x 0000001. Нижняя крышка корпуса</br> 
1 x 0000002. Верхняя крышка корпуса</br> 
1 x 0000003. Логотип</br> 
2 x 0000004. Держатель гайки М4</br> 
1 x 0000005. Правая ось поддержки яйца</br> 
1 x 0000006. Держатель пружины</br> 
1 x 0000007. Держатель правой оси</br> 
1 x 0000008. Фиксатор оси поддержки</br> 
2 x 0000009. Держатель болта М4 низ</br> 
2 x 0000010. Держатель болта М4 верх</br> 
1 x 0000011. Держатель левой оси</br> 
1 x 0000012.Левая ось поддержки яйца</br> 
1 x 0000013. Держатель руки маркера</br> 
1 x 0000014. Направляющая держателя руки маркера</br> 
1 x 0000015. Корпус направляющей</br> 
1 x 0000016. Рука маркера H</br> 
1 x 0000017. Рука маркера V</br> 
1 x 0000018. Правая крышка корпуса</br> 

Не печатаемые части:
-------------------
2 x <a href="http://s.click.aliexpress.com/e/72FuNFm">608zz Подшипник</a></br>
1 x <a href="http://s.click.aliexpress.com/e/MBeuZb6">24mm Резиновая прокладка</a></br>
1 x <a href="http://s.click.aliexpress.com/e/MBeuZb6">15mm Резиновая прокладка</a></br>

Болты и гайки, которые без труда можно найти в любом хозяйственном магазине: 
-------------------
1 x <a href="http://s.click.aliexpress.com/e/qF6YzRZ">Пружина диаметр 9-15мм длина 17-20мм</a></br> 
1 x 2x18мм Гвоздь без шляпки</br> 
2 x M5x16 Болт</br> 
2 x M5 Гайка</br> 
8 x M3x12 Винт</br> 
5 x M3x16 Винт</br> 
12 x M3 Гайка</br> 
4 x M3 Шайба</br> 
12 x <a href="http://s.click.aliexpress.com/e/uNzBU3V">M2x4 Винт</a></br>

Электроника
-------------------
1 x <a href="http://s.click.aliexpress.com/e/mMBaiuj">Arduino UNO</a></br>
2 x <a href="http://s.click.aliexpress.com/e/baQjima">ULN2003 Драйвер шагового двигателя</a></br>
2 x <a href="http://s.click.aliexpress.com/e/bYfuF6U">28byj-48-12v Шаговый двигатель</a></br>
1 x <a href="http://s.click.aliexpress.com/e/aAU3r7e">SG90 Микро серво двигатель</a></br>
1 x <a href="http://s.click.aliexpress.com/e/zbiMrfU">12В Блок питания</a></br>
1 x <a href="http://s.click.aliexpress.com/e/6YFYRZR">USB Кабель для ПК</a></br>
<a href="http://s.click.aliexpress.com/e/IY3rBuf">Немного проводов</a></br>

Инструкция по сборке
-------------------
Загрузите инструкцию по сборке <a href="https://github.com/ProbotXYZ/EggBot/blob/master/AssemblyInstructions/Assembly_Instruction_ru.pdf">отсюда</a>.</br>
3Д модель сборки <a href="https://github.com/ProbotXYZ/EggBot/blob/master/AssemblyInstructions/Instruction%203D.stl">тут</a>.

<p align="center">
<img src="AssemblyInstructions/Assembly.png" width="70%">
</p>  

Прошивка
-------------------
В качестве прошивки используется Eggduino. Это ардуино прошивка для EggBot / Spherebot с интерацией Inkscape (<a href="https://github.com/cocktailyogi/EggDuino">Github</a>).

Для установки:
1) Загрузите и распакуйте <a href="https://github.com/ProbotXYZ/EggBot/blob/master/Firmware/Firmware.zip">Firmware.zip</a>.
2) Загрузите ARDUINO IDE отсюда: https://www.arduino.cc/en/Main/Software и установите его.
3) Запустите ARDUINO IDE. Выберите плату Arduino UNO и COM порт (может быть COM5 или другой) в меню "Tools->Board"…
4) Откройте Eggduino.ino из <a href="https://github.com/ProbotXYZ/EggBot/blob/master/Firmware/Firmware.zip">Firmware.zip</a> и загрузите в ваш Arudino Uno. 

Программа для печати и управления
-------------------
В качестве управляющей программы используется свободный векторный редактор Inkscape.
1) Загрузите и распакуйте <a href="https://github.com/ProbotXYZ/EggBot/blob/master/Software/Software_(inkscape%2Bextension).zip">Software_inkscape+extension.zip</a>.
2) Расширение для редактора уже включено в архив <a href="https://github.com/ProbotXYZ/EggBot/blob/master/Software/Software_(inkscape%2Bextension).zip">Software_inkscape+extension.zip</a>.
3) Запустите Inkscape. 

Расширение EggBot Control для Inkscape это утилита, при помощи которой можно тестировать и управлять Яйцеботом, а также отправлять на рисование ваши ресунки. После того как Inkscape запущен, в меню Extensions ищите подменю Eggbot. 

Для ваших рисунков вы можете использовать шаблон (File->New from Template).

Не забудьте посмотреть <a href="https://github.com/ProbotXYZ/EggBot/tree/master/Samples">примеры рисунков</a>.
