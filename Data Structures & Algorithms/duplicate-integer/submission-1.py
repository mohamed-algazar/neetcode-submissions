class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        duplicates = set()
        duplicate = False
        for num in nums:
            if num in seen:
                duplicates.add(num)
                duplicate = True
            else:
                seen.add(num)
        return duplicate