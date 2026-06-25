class solution:
    def max_subarray(self,nums):
        max_sum = nums[0]
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            if curr_sum>max_sum:
                max_sum = curr_sum
            if curr_sum<0:
                curr_sum = 0
        return max_sum
k = list(map(int,input("enter list : ").split()))
obj = solution()
output = obj.max_subarray(k)
print(output)