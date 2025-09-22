class Solution:
    def pivotInteger(self, n: int) -> int:
        nums=[]
        for i in range(n): 
            nums.append(i+1) 

        total=sum(nums)
        left=0 
        for i in range(len(nums)): 
            if left+nums[i]==total-left:
                return i+1 
            left+=nums[i]
        
        return -1
