# class Solution(object):
#     def candy(self, ratings):
#         """
#         :type ratings: List[int]
#         :rtype: int
#         """
#         #to right
#         candys = [1] * len(ratings)
#
#         for j in range(1, len(ratings)):
#             if ratings[j] > ratings[j-1]:
#                 candys[j] = candys[j-1] + 1
#
#         for i in range(len(ratings)-2, -1, -1):
#             if ratings[i] > ratings[i+1]:
#                 candys[i] = candys[i+1] + 1
#
#         return sum(candys), candys
#
# t = [1,3,4,5,2]
# s = Solution()
# a, b = s.candy(t)
# print(a)
# print(b)
