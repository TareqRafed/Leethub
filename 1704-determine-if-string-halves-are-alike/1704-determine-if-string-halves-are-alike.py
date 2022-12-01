class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        s = s.lower()
        str_len = len(s)
        left_word = 0
        right_word = 0
        for i, letter in enumerate(s):
            if letter in vowels:
                if i < (str_len // 2):
                    left_word += 1
                else:
                    right_word += 1
        
        
        return left_word == right_word