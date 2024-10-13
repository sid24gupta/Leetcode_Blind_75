# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3. Longest Substring Without Repeating Characters
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def lengthOfLongestSubstring(s: str) -> int:

    lookup = {}
    i = 0
    j = 0
    length_so_far = 0

    while j < len(s):

        lookup[s[j]] = 1 + lookup.get(s[j],0)

        if lookup[s[j]] == 2:

            while lookup[s[j]] != 1:
                lookup[s[i]] -= 1
                i += 1
        else:
            length_so_far = max(length_so_far,j-i+1)
        j+= 1

    return length_so_far



s = "abcabcbb"
v1 = lengthOfLongestSubstring(s)
print(v1)