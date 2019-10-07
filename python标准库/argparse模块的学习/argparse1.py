# 1. 入门配置
import argparse


parser = argparse.ArgumentParser(description="used for test")
parser.add_argument('--version', '-v', action='version', version='%(prog)s version: v 0.01', help='show the version')
parser.add_argument('--debug', '-d', action='store_true', help='show the version', default=False)

args = parser.parse_args()
print('=== end ===')

# please type 'python argparse1.py -v, python argparse1.py -v'
