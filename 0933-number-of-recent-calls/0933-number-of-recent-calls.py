class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)

        # Remove elements older than t - 3000
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        # The return must be OUTSIDE the while loop
        return len(self.requests)
     
    
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)