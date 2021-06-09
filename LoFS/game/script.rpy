# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define nm = Character('Неизвестный', color="#f75252")
define nf = Character('Неизвестная', color="#f75252")
define ni = Character('Нира', color="#c8ffc8", image='cat')
define so = Character('Сор', color="#c8ffc8", image='sora')
define sh = Character ('Тень', color="#f75252", image='shadow')

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

init:
    $ standartLeft = Position (xalign=0.2, yalign=1.0)
    $ standartRight = Position (xalign=0.8, yalign=1.0)

# Игра начинается здесь:
label start:
    
    narrator ```Ну-у.. {w} Мгмь… {w} Мне начинать, да?.. {w} Что-ж… 

    Кхмь-кхмь… {w} Я надеюсь хоть немного расшевелить сервер в преддверии лета, что бы он не лежал забытым на задворках дискорда и памяти.
    {w}Хочу чтобы в это время он не затух сильнее, окончательно, среди других занятий.```

    return