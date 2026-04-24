class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {}
        suffix = {}

        total = 1
        for i in range(len(nums)):
            total *= nums[i]
            prefix[i] = total
        
        total = 1
        for i in range(len(nums)):
            total *= nums[-i -1]
            suffix[len(nums)+ -i - 1] = total

        print(prefix)
        print(suffix)
        
        ret = []
        for i in range(len(nums)):
            if i == 0:
                ret.append(suffix[i + 1])
            elif i != len(nums) - 1:
                ret.append(prefix[i - 1] * suffix[i + 1])
            else:
                ret.append(prefix[i - 1])


        return ret
