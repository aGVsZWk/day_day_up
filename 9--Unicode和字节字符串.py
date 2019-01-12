# 九. Unicode和字节字符串

# 1-- Python的字符串类型
"""python2.x"""
# 1.str表示8位文本和二进制数据
# 2.unicode表示宽字符和Unicode文本

"""Python3.x"""
# 1.str表示Unicode文本(8位或者更宽)
# 2.bytes表示不可变的二进制数据
# 3.bytearray是一种可变的bytes类型


# 2--字符编码方法
"""ASCII"""     # 一个字节, 只包含英文字符, 0到127. 共128个字符, 利用函数可以进行字符和数字的相互转换
ord('a')        # 字符a的ASCII码为97, 所以这里返回97
chr(97)         # 和上面的过程相反, 返回字符"a"
"""Latin-1"""   # 一个字节, 包含特殊字符, 0到255. 共256个字符, 相当于对ASCII码的扩展
chr(196)        # 返回一个特殊字符: A
"""Unicode"""   # 宽字符, 一个字符包含多个字节, 一般用于亚洲的字符集, 比如中文有好几万字
"""UTF-8"""     # 可变字节数, 小于128的字符表示单个字节, 128到0X7FF之间的代码转换为两个字节, 0X7FF以上的代码转换为3或4个字节
# 注意: 可以看出来, ASCII码是Latin-1和UTF-8的一个子集
# 注意: utf-8是unicode的一种实现方式, unicode, gbk, gb2312是编码字符集




# 3--查看Pyhton中的字符串编码名称. 查看系统的编码
import encodings
# help(encodings)
import sys
sys.platform    # win32
sys.getdefaultencoding()    # utf-8   返回当前系统平台的编码类型
sys.getsizeof(object)   # 返回object占用的bytes的大小



# 4--源文件字符集编码声明: 添加注释来指定想要的编码形式, 从而改变默认值, 注释必须出现在脚本的第一行或者第二行
"""说明:其实这里只会检查#和coding:utf-8, 其余的字符都是为了美观而加上的"""
# _*_coding: utf-8 _*_
# coding = utf-8



# 5--#编码: 字符串 --> 原始字节      # 解码: 原始字节 --> 字符串




# 6--Python3.x中字符串应用
s = '...'       # 构建一个str对象, 不可变对象
b = b'...'       # 构建一个bytes对象, 不可变对象
ord('.')        # 返回46
s[0], b[0]      # 返回(".", 46)
s[1:], b[1:]    # 返回('..', b'..')
B = B"""
xxxx
yyyy
"""
# B = B'\nxxxx\nyyyy\n'

# 编码, 将str字符串转化为其它raw bytes形式
# str.encode(encoding='utf-8', errors='strict')
# bytes(str, encoding)
#
# 编码实例:
S = 'egg'
S.encode()  # b'egg'
bytes(S, encoding='ascii')  # b'egg'

# 解码: 将raw bytes字符串转化为str形式:
# bytes.decode(encoding='utf-8', errors='strict')
# str(bytes_or_buffer[, encoding[, errors]])

# 解码实例:
B = b'spam'
B.decode()  # 'spam'
str(B)  # b'spam', 不带编码的str调用, 结果为打印该bytes对象
str(B, encoding='ascii')    # 'spam'. 带编码的str调用, 结果为转化该bytes对象



# 7--Python2.x的编码问题
# u = u'汉'
# print repr(u)  # u'\xba\xba'
# s = u.encode('UTF-8')
# print repr(s)  # '\xc2\xba\xc2\xba'
# u2 = s.decode('UTF-8')
# print repr(u2)  # u'\xba\xba'
# 对unicode进行解码是错误的
# s2 = u.decode(
#     'UTF-8')  # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
# 同样，对str进行编码也是错误的
# u2 = s.encode(
#     'UTF-8')  # UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position 0: ordinal not in range(128)


# 8--bytes对象
B = b'abc'  # b'abc'
B = bytes('abc', 'ascii')   # b'abc'
B = bytes([97, 98, 99])     # b'abc'    # ascii码的97, 98, 99是a, b, c
B = 'abc'.encode()
# bytes对象的方法调用基本和str类型一直, 但:B[0返回的是ASCII码值是97, 而不是b'a'
B[0]



#  9--文本文件: 根据Unicode编码来解释文件内容, 要么是平台的默认编码, 要么是指定的编码类型
# 二进制文件: 表示字节值的整数的一个序列 open('bin.txt', 'rb')


# 10--unicode文件
s = 'A\xc4B\xe8C'   # AÄBèC
len(s)  # 5
# 手动编码
l = s.encode('latin-1')     # b'A\xc4B\xe8C'  len(l) = 5
u = s.encode('utf-8')       # b'A\xc3\x84B\xc3\xa8C'    len(u) = 7
# 文件输出编码
open('latindata', 'w', encoding='latin-1').write(s)
l = open('latindata', 'rb').read()  # l = b'A\xc4B\xe8C'  len(l) = 5
open('utf8data', 'w', encoding='utf-8').write(s)
u = open('utf8data', 'rb').read()  # u = b'A\xc3\x84B\xc3\xa8C'  len(u) = 7
# 文件输入编码
s = open('latindata', 'r', encoding='latin-1').read()  # s = 'AÄBèC'  len(s) = 5
s = open('latindata', 'rb').read().decode('latin-1')  # s = 'AÄBèC'  len(s) = 5
s = open('utf8data', 'r', encoding='utf-8').read()  # s = 'AÄBèC'  len(s) = 5
s = open('utf8data', 'rb').read().decode('utf-8')  # s = 'AÄBèC'  len(s) = 5







