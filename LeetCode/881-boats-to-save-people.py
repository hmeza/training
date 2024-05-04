class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        people.reverse()
        boats = 0
        while people:
            value = people.pop(0)
            if value > limit:
                continue

            boats += 1
            if value == limit:
                continue

            if people and value + people[-1] <= limit:
                people.pop()
        return boats
