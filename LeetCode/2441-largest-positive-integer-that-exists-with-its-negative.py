class Solution:
    def findMaxK(self, nums) -> int:
        # sort and prepare
        nums = sorted(nums)
        nums.reverse()

        try:
            a = nums.pop(0)
            z = nums.pop()
        except IndexError:
            return -1

        while nums:
            if a <= 0 or z >= 0:
                return -1
            if a + z == 0:
                return a
            elif a + z < 0:
                z = nums.pop()
            elif a + z > 0:
                # go to next
                a = nums.pop(0)
        if a + z == 0:
            return a
        return -1


a = Solution()
b = a.findMaxK([22,34,2,44,-8,49,-5,22,46,39,-23,-15,27,48,-37,10,22,-45,13,-2])
print(b)
