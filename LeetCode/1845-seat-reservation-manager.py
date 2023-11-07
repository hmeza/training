from queue import PriorityQueue


class SeatManager:

    def __init__(self, n: int):
        self.current_seat = 0
        self.unreserved = PriorityQueue()

    def reserve(self) -> int:
        if self.unreserved.qsize() == 0:
            self.current_seat += 1
            return self.current_seat
        else:
            seat = self.unreserved.get()
            return seat[1]

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber == self.current_seat:
            self.current_seat -= 1
        else:
            self.unreserved.put((seatNumber, seatNumber))

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
