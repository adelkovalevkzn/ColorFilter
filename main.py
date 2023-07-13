import os
import magic
import numpy as np
import cv2
import argparse
from scripts.core import Color
from scripts.parser import Parser
from scripts.errors import UnknownMethodError, OutputError


mime = magic.Magic(mime=True)


def run(filename, method, params, output, show):

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


def main():
    parser = Parser().get_parser()
    args = parser.parse_args()

    filename = args.filename
    method = args.method
    params = args.params
    output = args.output
    show = args.show

    if os.path.isfile(filename):
        run(filename, method, params, output, show)

    elif os.path.isdir(filename):
        print('[*] Чтение директории...')
        if not os.path.exists(output):
            os.mkdir(output)

        elif not os.path.isdir(output):
            raise OutputError('При импортировании директории для вывода изображений должна быть директория')

        files = os.walk(filename)
        paths = []

        for f in files:

            for i in f[2]:
                file = os.path.join(f[0], i)

                try:

                    if 'image' in mime.from_file(file):
                        paths.append(os.path.join(f[0], i))

                except Exception:
                    pass

        for file in paths:
            f_output = output + '/' +'out_' + os.path.basename(file)
            run(file, method, params, f_output, show=0)


if __name__ == '__main__':
    main()
