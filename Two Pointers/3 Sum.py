#Overall Complexity= quadratic
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() #Sorting nums
        res=[]
        for i in range(len(nums)-2): 
          #Skip the same value for first element to avoid duplicates
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
          #Using two pointers for the next two integers
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                  #Skip duplicates for second and third elements
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                    r-=1
        return res
        

        


        
