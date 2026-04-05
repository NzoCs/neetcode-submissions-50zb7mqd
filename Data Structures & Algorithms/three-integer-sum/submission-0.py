class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Trier le tableau pour éviter les doublons et utiliser two pointers
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            # Éviter les doublons pour le premier élément
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers pour trouver les deux autres nombres
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Éviter les doublons pour left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Éviter les doublons pour right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return res