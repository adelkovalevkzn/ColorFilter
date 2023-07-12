# ColorFilter

### Консольная утилита для простой цветокоррекции изображения

## Установка
- git clone https://github.com/adelkovalevkzn/ColorFilter
- cd ColorFilter
- pip3 install -r requirements.txt

## Использование
python3 main.py [имя_файла] -m [метод] -p [параметры] -o [сохранить_как] -s [вывод на экран (0 или 1)]


#### Методы:
- color_set - установка значения канала на всем изображении (-p "red", "green", "blue"  [0-255])
- reverse_colors - поменять красный и синий канал местами 
- only_channel - оставить единственный канал (-p "red", "green", "blue")
- gray - преобразование в оттенки серого
- black_and_white - сделать изображение черно-белым (бинарным)