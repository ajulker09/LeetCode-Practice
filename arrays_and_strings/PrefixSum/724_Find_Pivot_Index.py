class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums) 
        left_sum=0 
        for i in range(len(nums)):
            if left_sum==total_sum-nums[i]-left_sum: 
                if i==0: 
                    return 0 
                return i
            else: 
                left_sum+=nums[i] 
        
        return -1

        