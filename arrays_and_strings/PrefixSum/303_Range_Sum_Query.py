class NumArray:

    def __init__(self, nums: List[int]):
        #we have the nums array here. basically 
        self.prefix=[]
        #we want to be able to already have the prefix sum dealth with. 

        for i in range(len(nums)): 
            if i==0: 
                self.prefix.append(nums[i])
            else: 
                self.prefix.append(self.prefix[i-1]+nums[i]) 

    def sumRange(self, left: int, right: int) -> int:
        if left==0: 
            return self.prefix[right]
        else:
            return self.prefix[right]-self.prefix[left-1]