class solution():
    def maximumWealth(self,accounts):

        ans = 0
        for account in accounts:
            ans = max(ans,sum(account))
        return ans
 
accounts = []
rows = int(input("enter number of rows :"))


for i in range(rows):
    row = list(map(int, input().split()))
    accounts.append(row)
obj = solution()
print(obj.maximumWealth(accounts))