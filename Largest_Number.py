class Solution:
    
    def largestNumber(self, nums: List[int]) -> str:

        for i,n in enumerate(nums):
           nums[i] = str(n)
        
        def cmp(a,b):
            if a+b > b+a:
                return -1
            else:
                return 1

        nums = sorted(nums , key=cmp_to_key(cmp))
        ans = "".join(nums)

        return str(int(ans))