class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # num -> count
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        output = []
        for i in range(k):
            maxCount = max(count, key = count.get)
            output.append(maxCount)
            del count[maxCount]
            i += 1
        return output