# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

word1 = "abcd"
word2 = "pq"

i = 0
c1 = 0
c2 = 0
answer = ""
while(c1<len(word1) and c2<len(word2)):

    if i%2 == 0:
        answer += word1[c1]
        c1 += 1
    else:
        answer += word2[c2]
        c2 += 1

    i += 1

if c1<len(word1):
    answer += word1[c1:]
else:
    answer += word2[c2:]

print(answer)