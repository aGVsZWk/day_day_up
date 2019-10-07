# python自带的命令解析参数模块有3个: getopt, optparse, argparse, 第三个是神器

# 0. Hello World
import argparse
parser = argparse.ArgumentParser(description="used for test")
args = parser.parse_args()

# please type 'python argparse0.py -h'
