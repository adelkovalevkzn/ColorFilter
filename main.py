import os
import numpy as np
import cv2
import argparse


class UnknownMethodError(Exception):
    def __init__(self):
        self.message = "Неизвестный метод"

    def __str__(self):
        return self.message


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="python3 main.py",
            description="Цветокоррекция изображения",
            epilog="Методы: color_set, reverse_colors, only_channel, gray, black_and_white"

        )
        self.parser.add_argument('filename')
        self.parser.add_argument('-m', '--method')
        self.parser.add_argument('-p', '--params', nargs='*', required=False)
        self.parser.add_argument('-o', '--output')
        self.parser.add_argument('-s', '--show', type=int, default=0, required=False)

    def get_parser(self):
        return self.parser


class Color:
    def __init__(self, filename: str):
        """
        Загрузка изображения
        :param filename: имя файла или путь до файла
        """
        self.filename = filename
        self.image = cv2.imread(filename)

    def show(self):
        """
        Вывод изображения на экран
        :return: None
        """
        cv2.imshow(self.filename, self.image)
        cv2.waitKey()

    def save(self, output: str):
        """
        :param output: имя нового файла
        :return: None
        """
        cv2.imwrite(output, self.image)
        print(f'[*] Изображение сохранено в {os.path.abspath(output)}')

    def color_set(self, channel: str, value: int):
        """
        Установить значение канала цвета для всего иозбражения
        :param channel: редактируемый канал (red, green, blue)
        :param value: значение для редактируемого канала
        :return: None
        """
        channels = {"blue": 0, "green": 1, "red": 2}
        self.image[:, :, channels[channel]] = value

    def reverse_colors(self):
        """
        Реверсировать цвета изображения
        :return: None
        """

        reds = self.image[:, :, 2]
        blues = self.image[:, :, 0]

        self.image[:, :, 0] = reds
        self.image[:, :, 2] = blues

    def only_channel(self, channel: str):
        """
        Оставить единственный канал на фотографии
        :param channel: канал, который необходимо оставить (red, green, blue)
        :return: None
        """
        channels = {"blue": 0, "green": 1, "red": 2}

        channels.pop(channel)

        for ch in channels:
            self.image[:, :, channels[ch]] = 0

    def gray(self):
        """
        Оставить в изображении только оттенки серого
        :return: None
        """
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        print(self.image)

    def black_and_white(self):
        """
        Сделать изображение черно-белым
        :return: None
        """
        image_float_data = self.image.astype(float) / 255
        black_channel = 1 - np.max(image_float_data, axis=2)
        black_channel = (255 * black_channel).astype(np.uint8)
        _, self.image = cv2.threshold(black_channel, 100, 255, cv2.THRESH_BINARY_INV)


def main():
    parser = Parser().get_parser()
    args = parser.parse_args()

    filename = args.filename
    method = args.method
    params = args.params
    output = args.output
    show = args.show

    cf = Color(filename)

    if method == 'color_set':
        cf.color_set(params[0], params[1])
    elif method == 'reverse_colors':
        cf.reverse_colors()
    elif method == 'only_channel':
        cf.only_channel(params[0])
    elif method == 'gray':
        cf.gray()
    elif method == 'black_and_white':
        cf.black_and_white()
    else:
        raise UnknownMethodError

    cf.save(output)

    if show == 1:
        cf.show()


if __name__ == '__main__':
    main()
