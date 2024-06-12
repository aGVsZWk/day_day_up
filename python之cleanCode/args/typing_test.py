# @Author: helei
# @Date:   2020-09-01
# @Email:  v_heleihe@tencent.com
# @Filename: a.py
# @Last modified by:   helei
# @Last modified time: 2020-09-01
from typing import List


def fname(b:List[str])->None:
    print(b)


if __name__ == '__main__':
    aa = ['123', 123]
    fname(aa)
