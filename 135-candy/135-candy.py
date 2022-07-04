class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = len(ratings)
        kidsCandies = [1 for _ in ratings]
        
        
        for i in range(1, len(ratings)):
            if  ratings[i - 1] < ratings[i]:
                kidsCandies[i] += kidsCandies[i - 1]
        
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i] and kidsCandies[i - 1] <= kidsCandies[i]:
                kidsCandies[i - 1] += (kidsCandies[i] - kidsCandies[i - 1]) + 1
                
        return sum(kidsCandies)