class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        S1=set()
        ans=0
        sum=0
        i=0
        for j in range(len(nums)):
            while nums[j] in S1:
                S1.remove(nums[i])
                sum-=nums[i]
                i+=1
            S1.add(nums[j])
            sum+=nums[j]
            ans=max(ans,sum)
        return ans


        