#Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

#S1  - Hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        return count_s == count_t

#TC = O(n + m), SC =O(1) - we have at most 26 different characters


#S2 - Array + Hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
#TC = O(n + m), SC =O(1) - we have at most 26 different characters


#S3 - sorting solution - Bad
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        return sorted(s) == sorted(t)

#TC = O(nlogn+mlogm), SC= O(1) O(n+m) depending on the sorting algorithm.
