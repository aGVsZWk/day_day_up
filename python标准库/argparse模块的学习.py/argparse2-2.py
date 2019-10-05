# 2.1 参数种类
## 2.2 可选参数
### 有两种方式:
### 1. 单下划线制定的短参数, 如 -h
### 2. 双下划线制定的长参数, 如 --help


import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-v', '--verbosity', help='increase output verbosity')
args = parser.parse_args()
if args.verbosity:
    print('verbosity turned on')
    print(args.verbosity)

else:
    print('verbosity turned off')

# please type `python argparse2-2.py ` `python argparse2-2.py -v xxxx`
