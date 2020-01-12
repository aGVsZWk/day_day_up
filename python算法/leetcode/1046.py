class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        while len(stones) >= 2:
            t1 = max(stones)
            stones.remove(t1)
            t2 = max(stones)
            stones.remove(t2)
            if t1 != t2:
               stones.append(t1-t2)
        return 0 if not stones else stones[0]
