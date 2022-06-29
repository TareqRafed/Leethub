class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        ans = []
        
        sorted_people = sorted(people, key= lambda x: (-x[0], x[1]))
        
        for person in sorted_people:
            ans.insert(person[1], person)
        
        return ans