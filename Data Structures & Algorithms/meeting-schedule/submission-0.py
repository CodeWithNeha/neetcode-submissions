"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, nums: List[Interval]) -> bool:
        for i in range(len(nums)-1):
            if nums[i].end >nums[i+1].start:
                return False
        return True
