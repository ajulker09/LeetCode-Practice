class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum=[] 
        rightSum=[] 

        answer=[]# size n 

        if len(nums)<=1:
            return [0]
        else:
            prefix=[] 
            for i in range(len(nums)): 
                if i==0: 
                    prefix.append(nums[i]) 
                    leftSum.append(0)
                else: 
                    prefix.append(prefix[i-1]+nums[i]) 
                    leftSum.append(prefix[i-1]) 
            
            right=len(nums)-1
            left=0
            
            for i in range(len(nums)): 
                if i==right:
                    rightSum.append(0)
                else:
                    rightSum.append(prefix[right]-prefix[left])
                    left+=1
            
            for i in range(len(nums)): 
                answer.append(abs(leftSum[i]-rightSum[i]))
            
            return answer