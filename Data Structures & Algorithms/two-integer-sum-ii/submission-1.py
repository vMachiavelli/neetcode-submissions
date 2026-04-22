class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p2 = -1
        p1 = 0
        while numbers[p1] + numbers[p2] != target:
            print(p1, p2)
            if target - numbers[p1] < numbers[p2]:
                p2 = p2 - 1
            elif target - numbers[p1] > numbers[p2]:
                p1 = p1 + 1
        
        return [(p1 + 1),len(numbers) + p2 + 1]