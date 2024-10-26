class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #nums=sorted(nums)
        i=0 
        j=len(nums)-1 

        while i<j:
            sum=nums[i]+nums[j]

            if sum==target:
                return [i,j]
                break 
            elif sum<target:
                i+=1 
            else:
                j-=1        


        
