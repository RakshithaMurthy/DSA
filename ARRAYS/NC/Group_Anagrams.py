#Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

#S1
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictstr=defaultdict(list)
        for i in strs:
            sorted_str = ''.join(sorted(i))
            dictstr[sorted_str].append(i)
        return list(dictstr.values())

'''
Time complexity: O(m* nlogn)
Space complexity: O(m*n)
Where m is the number of strings and n is the length of the longest string.
'''



