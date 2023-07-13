import cv2
import os
import numpy as np


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

