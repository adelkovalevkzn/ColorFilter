import argparse


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

