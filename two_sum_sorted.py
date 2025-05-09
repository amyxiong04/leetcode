class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # below implementation is O(n^2)
        # left = 0

        # for num in numbers:
        #     right = len(numbers) - 1
        #     complement = target - num
        #     while left < right:
        #         if numbers[right] == complement:
        #             return [left + 1, right + 1]  #(1-indexed)
        #         right -= 1
        #     left += 1

        # this implementation is better because it is O(n)
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else: 
                right -= 1