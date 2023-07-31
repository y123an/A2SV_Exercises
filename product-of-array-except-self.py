class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = [1]
        prefix = [1]
        output = []

        for i in range(len(nums)-1):
            prefix.append(prefix[-1] * nums[i])
        
        for i in range(len(nums)-1,0,-1):
            postfix.append(postfix[-1] * nums[i])
        
        for i in range(len(nums)):
            output.append(prefix[i] * postfix[-1-i])
            
        return output

        # [1,2,3,4]

        # prefix = [1,1,3,6]
        # postfix = [1,4,12,24]
