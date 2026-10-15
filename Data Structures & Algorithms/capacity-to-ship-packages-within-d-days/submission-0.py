class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # brute force
        for capacity in range(max(weights), sum(weights)+1):
            required_days = 1
            current_weight = 0
            for weight in weights:
                
                if current_weight + weight>capacity:
                    current_weight = 0
                    required_days +=1
                current_weight += weight
            if required_days<=days:
                return capacity
        return days