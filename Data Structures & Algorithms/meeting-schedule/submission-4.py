"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        temp = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i].end <= temp.start or intervals[i].start >= temp.end:
                temp = intervals[i]
            else:
                return False
            
        return True