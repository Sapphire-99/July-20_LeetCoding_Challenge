class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res= set()
        for i in range(n-1):
            l=i+1
            r=n-1
            while(l<r):
                sum=(nums[i]+nums[l]+nums[r])
                if (sum==0):
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif (sum<0):
                    l+=1
                else:
                    r-=1
        return res
