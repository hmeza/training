from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1 and gas[0] >= cost[0]:
            return 0

        differences = [gas[i] - cost[i] for i in range(len(gas))]

        # if there exists a solution, it is GUARANTEED to be unique
        # -> find the max in differences
        last_index_that_worked = None
        accumulated = 0
        for i in range(len(differences)):
            if accumulated + differences[i] <= 0 and i != len(differences) - 1:
                last_index_that_worked = None
                accumulated = 0
                continue
            elif last_index_that_worked is None:
                last_index_that_worked = i
                accumulated += differences[i]
            else:
                accumulated += differences[i]

        if last_index_that_worked is None:
            return -1

        # now test solution
        new_gas = gas[last_index_that_worked:] + gas[0:last_index_that_worked]
        new_cost = cost[last_index_that_worked:] + cost[0:last_index_that_worked]
        car_gas = new_gas[0]
        try:
            for i in range(1, len(new_gas)):
                car_gas -= new_cost[i-1]
                if car_gas < 0:
                    raise Exception("Unable to arrive to destination")
                car_gas += new_gas[i]
            car_gas -= new_cost[len(new_cost) - 1]
            if car_gas < 0:
                raise Exception("Unable to arrive to destination")
            return last_index_that_worked
        except Exception:
            return -1


a = Solution()
assert a.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]) == 3
assert a.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]) == -1
assert a.canCompleteCircuit(gas=[1, 1, 6, 1, 6], cost=[1, 1, 5, 1, 5]) == 2
assert a.canCompleteCircuit(gas=[5, 8, 2, 8], cost=[6, 5, 6, 6]) == 3
assert a.canCompleteCircuit(gas=[3, 1, 1], cost=[1, 2, 2]) == 0
assert a.canCompleteCircuit(gas=[5, 5, 1, 3, 4], cost=[8, 1, 7, 1, 1]) == 3, a.canCompleteCircuit(gas=[5, 5, 1, 3, 4],
                                                                                                  cost=[8, 1, 7, 1, 1])
assert a.canCompleteCircuit(gas=[4], cost=[5]) == -1
assert a.canCompleteCircuit(gas=[2], cost=[2]) == 0
assert a.canCompleteCircuit(gas=[2, 0, 1, 2, 3, 4, 0], cost=[0, 1, 0, 0, 0, 0, 11]) == 0
assert a.canCompleteCircuit(gas=[3, 3, 3, 3, 3, 3, 3, 3], cost=[5, 1, 4, 4, 4, 2, 2, 2]) == 5

