class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m=dict()
        for i in range(len(nums)):
            two_sum=target-nums[i]
            if two_sum in m:
                return [m[two_sum],i]
            else:
                m[nums[i]]=i
        return [-1,-1]