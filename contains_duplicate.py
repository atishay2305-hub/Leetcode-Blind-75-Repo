class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #USING HASHSET
        # hashset = set()
        # for n in nums:
        #     if n in nums:
        #         return True
        #     hashset.add()
        # else:
        #     return False
            
        #USING BRUTE FORCE METHOD 
            for i in nums:
                for j in nums:
                    if nums[i] == nums[j]:
                        return True
            return False
        
        
        