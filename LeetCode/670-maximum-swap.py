class Solution:
    def maximumSwap(self, num: int) -> int:
        numbers = list(str(num))
        limit = len(numbers) - 1
        for i, number in enumerate(numbers):
            if i == limit:
                break
            number = int(number)
            next_number = int(numbers[i+1])
            if number == next_number:
                continue
            elif number < next_number:
                numbers[i+1], numbers[i] = numbers[i], numbers[i+1]
                if i > 0 and numbers[i] > numbers[i-1]:
                    numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
                break
        return int("".join(map(str, numbers)))


s = Solution()
assert s.maximumSwap(2736) == 7236
assert s.maximumSwap(9973) == 9973
assert s.maximumSwap(2367) == 3267
