class solution:
    def runningsum(self,nums):
        sum = 0
        ans =[]
        for i in nums :
            sum+=i
            ans.append(sum)
        return ans
k = list(map(int,input("enter list : ").split()))
object = solution()
output = object.runningsum(k)
print(output)
