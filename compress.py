#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import click
from PIL import Image


@click.command()
@click.option('-d', "--dir", type=str, default='/', help="压缩文件夹下所有文件")
@click.option('-w', "--width", type=int, default=1024, help="图片宽度，默认不变")

def run(dir,width):
    if dir is not None:
        find_path = "find " + dir + " -regex '.*\(jpg\|JPG\|png\|PNG\|jpeg\)' -type f  | sort -nr"
        result = os.popen(find_path).read().split('\n')

        for item in result:
            compress_file(item, width)
            pass
        pass
    else:
        print('请指定要压缩的文件或文件夹')
    print('End')

def compress_file(item, width):
    if item:
        img = Image.open(item)
        x, y = img.size
        if x >= width:
            convert_path = "convert -resize 50%x50% " + item + ' ' +item
            print(item)
            os.popen(convert_path)


if __name__ == "__main__":
    run()