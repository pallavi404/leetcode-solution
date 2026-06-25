#905
class solution:
    def sort_array(self,nums: List[int]):
        start = 0
        for i in range(len(nums)):
            if nums[i]%2==0:
                temp = nums[i]
                nums[i] = nums[start]
                nums[start] = temp
                start+=1
        return nums
k = list(map(int,input("enter list : ").split()))
obj = solution()
output = obj.sort_array(k)
print(output)
