class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        secondSign = False
        answer = False
        for i in range(len(bits)):
            if secondSign == False and bits[i] == 1:
                answer = False
                secondSign = True
            elif secondSign == False and bits[i] == 0:
                answer = True
                secondSign = False
            elif secondSign == True:
                secondSign = False
                answer = False
            else:
                continue
        return answer       
