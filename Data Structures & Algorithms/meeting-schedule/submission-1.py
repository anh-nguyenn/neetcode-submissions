"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # intervals.sort()
        arr = []
        for obj in intervals:
            arr.append([obj.start, obj.end])
        arr.sort()
        for i in range(len(arr) - 1):
            curr = arr[i]
            nxt = arr[i + 1]
            if nxt[0] < curr[1]:
                return False
        return True
            
