# 2.参数种类
## 2.1 必选参数
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('name')

args = parser.parse_args()
print(args.name)
# please type 'python argparse2-1.py zhangsan'
