# class Solution(object):
#     def canCompleteCircuit(self, gas, cost):
#         """
#         :type gas: List[int]
#         :type cost: List[int]
#         :rtype: int
#         """
#         twoGas = gas + gas
#         twoCost = cost + cost
#         i = 0
#         oil = 0
#         while i < len(gas):
#             oil = gas[i]
#             for j in range(len(gas)):
#                 oil = oil - twoCost[i+j]
#                 if oil >= 0:
#                     oil += twoGas[i+j+1]
#                 else:
#                     break
#             if oil >= 0:
#                 return i
#             else:
#                 i += 1
#         return -1

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        restGas = 0
        minRestGas = 0
        i = 0
        station = 0
        while i < len(gas):
            restGas += gas[i] - cost[i]
            # minRestGas = min(minRestGas, restGas)
            if restGas < minRestGas:
                minRestGas = restGas
                station = i + 1
            i += 1
        return -1 if restGas < 0 else station
