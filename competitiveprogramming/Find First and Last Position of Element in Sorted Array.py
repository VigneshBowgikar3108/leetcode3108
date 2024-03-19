class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos=[]
        for i in range(len(nums)):
            if nums[i]==target:
                pos.append(i)
        if len(pos)==0:
            return [-1,-1]
        else:
            return [min(pos),max(pos)]
        