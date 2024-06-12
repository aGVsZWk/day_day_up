# 函数只做一件事

# 1. 短小
# 1-1：if语句，else语句，while语句，代码块应该只有一行
# 1-2：函数的缩进层级不应该多于一层或两层

# 2. 只做一件事：看是否能在拆出一个函数，该函数不仅只是单纯地重新诠释其实现

def createMessage(data, candidate):
    return "There %s %s %s%s" % (data['verb'], data['number'], candidate, data['pluralModifier'])


def oneLetterState():
    data = {}
    data['number'] = '1'
    data['verb'] = 'is'
    data['pluralModifier'] = ''
    return data


def noLetterState():
    data = {}
    data['number'] = 'no'
    data['verb'] = 'are'
    data['pluralModifier'] = 's'
    return data


def manyLetterState(count):
    data = {}
    data['number'] = str(count)
    data['verb'] = 'are'
    data['pluralModifier'] = 's'
    return data


def getKeyPartMessageState(count):
    state = {}
    if count == 0:
        state = noLetterState()
    elif count == 1:
        state = oneLetterState()
    else:
        state = manyLetterState(count)
    return state


def guessMessage(candiate, count):
    state = getKeyPartMessageState(count)
    msg = createMessage(state, candiate)
    return msg


if __name__ == '__main__':
    guessMessage('letter', 1)
