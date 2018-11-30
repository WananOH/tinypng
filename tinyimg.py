#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import os.path
import click
import tinify


online_key_list = [
    "sq5RzZVjHxVKRN0CHSBn659XPb67PyMl",
    "rcj2WmWcPZGMDbmwDXJ69XQKGhyr6mCw",# 可以继续添加  防止一个key不够
]
online_key_list_iter = iter(online_key_list)
online_key = next(online_key_list_iter)

version = "1.0.1"  # 版本

# 压缩的核心
def compress_core(inputFile, outputFile, img_width):
    global online_key
    compresskey = online_key
    tinify.key = compresskey
    print "file = %s" % inputFile
    try:
        source = tinify.from_file(inputFile)
        if img_width is not -1:
            resized = source.resize(method="scale", width=img_width)
            resized.to_file(outputFile)
        else:
            source.to_file(outputFile)
    except tinify.AccountError, e:

        online_key = next(online_key_list_iter)
        compress_core(inputFile, outputFile, img_width)  # 递归方法 继续读取
    except tinify.ClientError, e:
        print(e)
        pass


# 仅压缩指定文件
def compress_file(inputFile, width):
    print "compress_file-------------------------------------"
    if not os.path.isfile(inputFile):
        print "这不是一个文件，请输入文件的正确路径!"
        return

    basename = os.path.basename(inputFile)
    fileName, fileSuffix = os.path.splitext(basename)
    if fileSuffix == '.png' or fileSuffix == '.jpg' or fileSuffix == '.jpeg':
        compress_core(inputFile, inputFile, width)
    else:
        print "不支持该文件类型!"


@click.command()
@click.option('-d', "--dir", type=str, default='/', help="压缩文件夹下所有文件")
@click.option('-f', "--file", type=str, default=None, help="单个文件压缩")
@click.option('-s', "--size", type=str, default='1024k', help="需要压缩的文件大小")
@click.option('-w', "--width", type=int, default=-1, help="图片宽度，默认不变")
def run(dir, file, width, size):
    if file is not None:
        compress_file(file, width)  # 仅压缩一个文件
        pass
    elif dir is not None:
        find_path = "find " + dir + " -regex '.*\(jpg\|JPG\|png\|PNG\|jpeg\)' -type f  -size +" + size + "  | sort -nr"
        # print(find_path)
        result = os.popen(find_path).read().split('\n')

        for item in result:
            # print(item)
            compress_file(item, width)
            pass
        pass
    else:
        print '请指定要压缩的文件或文件夹'
    print "结束!"


if __name__ == "__main__":
    run()
