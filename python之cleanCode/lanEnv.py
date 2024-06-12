# 无意义语境
def printGuessStatistics(candidate, count):     # candidate: 候选人
    number = ''
    verb = ''    # 动词
    pluralModifier = ''  # 复数修饰语

    if count == 0:
        number = 'no'
        verb = 'are'
        pluralModifier = 's'
    elif count == 1:
        number = '1'
        verb = 'is'
        pluralModifier = ''
    else:
        number = str(count)
        verb = 'are'
        pluralModifier = 's'
    guessMessage = "There %s %s %s%s" % (verb, number, candidate, pluralModifier)
    print(guessMessage)


# 有意义语境（类版）
class GuessStatisticsMessage(object):
    def __init__(self):
        self.number = ''
        self.verb = ''
        self.pluralModifier = ''

    def make(self, candidate, count):
        self.createpluralDependentMessageParts(count)
        return "There %s %s %s%s" % (self.verb, self.number, candidate, self.pluralModifier)

    def createpluralDependentMessageParts(self, count):
        if count == 0:
            self.thereAreNoLetters()
        elif count == 1:
            self.thereIsOneLetter()
        else:
            self.thereAreManyLetters(count)

    def thereAreManyLetters(self, count):
        self.number = str(count)
        self.verb = 'are'
        self.pluralModifier = 's'

    def thereIsOneLetter(self):
        self.number = '1'
        self.verb = 'is'
        self.pluralModifier = ''

    def thereAreNoLetters(self):
        self.number = 'no'
        self.verb = 'are'
        self.pluralModifier = 's'


if __name__ == '__main__':
    printGuessStatistics('letters', 2)
    guessStatisticsMessage = GuessStatisticsMessage()
    guessStatisticsMessage.make('letter', 0)
