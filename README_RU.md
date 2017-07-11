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

Cписок деталей и количество, которое нужно напечатать
-------------------
<p align="center">
<img src="Stl/Items.jpg" width="70%">
</p>  
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

Не печатаемые части
-------------------
2 x <a href="http://canbemake.ru/recommends/608zz-podshipnik/">608zz Подшипник</a></br>
1 x <a href="http://canbemake.ru/recommends/rubber-gasket/">24mm Резиновая прокладка</a></br>
1 x <a href="http://canbemake.ru/recommends/rubber-gasket/">15mm Резиновая прокладка</a></br>

Болты и гайки, которые без труда можно найти в любом хозяйственном магазине 
-------------------
1 x <a href="http://canbemake.ru/recommends/pruzhiny/">Пружина диаметр 9-15мм длина 17-20мм</a></br> 
1 x 2x18мм Гвоздь без шляпки</br> 
2 x M5x20 Болт</br> 
2 x M5 Гайка</br> 
8 x <a href="http://canbemake.ru/recommends/bolt-m3x12/">M3x12 Винт</a></br> 
5 x M3x16 Винт</br> 
12 x <a href="http://canbemake.ru/recommends/gajka-m3/">M3 Гайка</a></br> 
4 x M3 Шайба</br> 
12 x <a href="http://canbemake.ru/recommends/m2x4/">M2x4 Винт</a></br>

Электроника
-------------------
1 x <a href="http://canbemake.ru/recommends/arduino-uno/">Arduino UNO</a></br>
2 x <a href="http://canbemake.ru/recommends/uln2003-drajver-shagovogo-dvigatelya/">ULN2003 Драйвер шагового двигателя</a></br>
2 x <a href="http://canbemake.ru/recommends/28byj-48-12v-shagovyj-dvigatel/">28byj-48-12v Шаговый двигатель</a></br>
1 x <a href="http://canbemake.ru/recommends/sg90-mikro-servo-dvigatel/">SG90 Микро серво двигатель</a></br>
1 x <a href="http://canbemake.ru/recommends/12v-blok-pitaniya/">12В Блок питания</a></br>
1 x <a href="http://canbemake.ru/recommends/usb-kabel-dlya-pk/">USB Кабель для ПК</a></br>
<a href="http://canbemake.ru/recommends/nemnogo-provodov/">Немного проводов</a></br>

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
2) Для Arduino UNO с контроллером CH340G (почти все китайские платы) загрузите и установите драйвер: http://www.wch.cn/download/CH341SER_ZIP.html.
3) Загрузите ARDUINO IDE отсюда: https://www.arduino.cc/en/Main/Software и установите его.
4) Запустите ARDUINO IDE. Выберите плату Arduino UNO и COM порт (может быть COM5 или другой) в меню "Tools->Board"…
5) Откройте Eggduino.ino из <a href="https://github.com/ProbotXYZ/EggBot/blob/master/Firmware/Firmware.zip">Firmware.zip</a> и загрузите в ваш Arudino Uno. 

Программа для печати и управления
-------------------
В качестве управляющей программы используется свободный векторный редактор Inkscape.
1) Загрузите и распакуйте <a href="https://github.com/ProbotXYZ/EggBot/blob/master/Software/Software_(inkscape%2Bextension).zip">Software_inkscape+extension.zip</a>.
2) Расширение для редактора уже включено в архив <a href="https://github.com/ProbotXYZ/EggBot/blob/master/Software/Software_(inkscape%2Bextension).zip">Software_inkscape+extension.zip</a>.
3) Запустите Inkscape. 

Расширение EggBot Control для Inkscape это утилита, при помощи которой можно тестировать и управлять Яйцеботом, а также отправлять на рисование ваши ресунки. После того как Inkscape запущен, в меню Extensions ищите подменю Eggbot. 

Если у вас Inkscape при попытке управления ботом выдаёт ошибку "Failed to connect to EggBot", то не отчаивайтесь. Проблему можно легко решить. Посмотрите в списке подключенного оборудования, то как называется ваша плата. Затем в файле ebb_serial.py плагина для Inkscape замените в строке 52 текст "USB-SERIAL CH340" на ваше название.

Для ваших рисунков вы можете использовать шаблон (File->New from Template).

Не забудьте посмотреть <a href="https://github.com/ProbotXYZ/EggBot/tree/master/Samples">примеры рисунков</a>.
