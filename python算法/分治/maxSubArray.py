def findmaxArray(target, low, high):
   if low == high:
      return (low, high, target[high])
   mid = (low + high) // 2
   leftLow, leftHigh, leftMaxSum = findmaxArray(target, low, mid)
   rightLow, rightHigh, rightMaxSum = findmaxArray(target, mid+1, high)
   corssLow, crossHigh, crossMaxSum = findmaxArrayCrossMid(target, low, mid, high)
   
   if leftMaxSum >= rightMaxSum and leftMaxSum >= crossMaxSum:
      return (leftLow, leftHigh, leftMaxSum)
   elif rightMaxSum >= leftMaxSum and rightMaxSum >= crossMaxSum:
      return (rightLow, rightHigh, rightMaxSum)
   else:
      return (corssLow, crossHigh, crossMaxSum)


def findmaxArrayCrossMid(target, low, mid, high):
   leftSum, rightSum = 0, 0
   leftMaxSum, rightMaxSum = float('-inf'), float('-inf')
   for i in range(mid, low - 1, -1):
      leftSum += target[i]
      if leftSum > leftMaxSum:
         leftMaxSum = leftSum
         crossLow = i
   for i in range(mid+1, high + 1):
      rightSum += target[i]
      if rightSum > rightMaxSum:
         rightMaxSum = rightSum
         crossHigh = i
   return (crossLow, crossHigh, leftMaxSum + rightMaxSum)

if __name__ == '__main__':
   target = [1, -2, 3, -4, 5, -6]
   t = findmaxArray(target, 0, len(target)-1)
   print(t)
   target = [1, 3, -1, -2, 8, -1, -2, -3, 4]
   t = findmaxArray(target, 0, len(target)-1)
   print(t)
   target = [9, -8, 3, 4, -5, 6]
   t = findmaxArray(target, 0, len(target)-1)
   print(t)
