class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1 #Using two pointers, left and right
        max_amount=0
        while l<r:
            curr_amount=min(height[l],height[r])*(r-l) #current amount= min(left height,right height) x (width between the heights)
            max_amount=max(curr_amount,max_amount) #updating max amount
            if height[l]>height[r]: # move towards the larger height
                r-=1
            else:
                l+=1
        return max_amount

        
