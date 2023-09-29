from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_delivered = [0 for n in range(len(ratings))]

        def candy_left(i, ratings):
            if i == 0:
                return 1
            return candy_delivered[i-1] + 1 if ratings[i-1] < ratings[i] else 1

        def candy_right(i, ratings):
            if i + 1 == len(ratings):
                return 1
            return candy_left(i, ratings) if ratings[i+1] < ratings[i] else 1

        for i in range(0, len(ratings)):
            candy_delivered[i] = max(candy_left(i, ratings), candy_right(i, ratings))
            if self._is_min_of_a_serie(ratings, i):
                self._go_back_and_increase_candy(ratings, i, candy_delivered)
        return sum(candy_delivered)

    def _is_min_of_a_serie(self, ratings, i):
        return (len(ratings) - 1 > i > 0 and ratings[i-1] > ratings[i] <= ratings[i+1])\
            or (len(ratings) - 1 == i > 0 and ratings[i-1] > ratings[i])

    def _go_back_and_increase_candy(self, ratings, i, candy_delivered):
        i -= 1
        while i >= 0 and ratings[i] > ratings[i+1]:
            if candy_delivered[i+1] >= candy_delivered[i]:
                candy_delivered[i] = candy_delivered[i+1] + 1
            i -= 1


a = Solution()
assert a.candy([1,0,2]) == 5
assert a.candy([1,2,2]) == 4
assert a.candy([1,2,87,87,87,2,1]) == 13
assert a.candy([1,6,10,8,7,3,2]) == 18
assert a.candy([1,2,3,1,0]) == 9
assert a.candy([1,3,4,5,2]) == 11
assert a.candy([1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4]) == 47
