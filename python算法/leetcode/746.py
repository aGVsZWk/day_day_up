class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        attachLadderCost = [0] * len(cost)

        for i in range(2, len(cost)):
            attachLadderCost[i] = min(attachLadderCost[i-2]+cost[i-2], attachLadderCost[i-1]+cost[i-1])
        return attachLadderCost[len(cost)-1]
