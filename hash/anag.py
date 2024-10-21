# 242: Valid Anagram

# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.



# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


def containsDuplicate():
    t = "tar"
    s = "rat"
    counter={}      #defaultdict(int) for c in magazine: counter[c]+=1  &&&   Counter(magazine)
    for c in s:
        if c in counter:
            counter[c]+=1
        else:
            counter[c]=1

    # print(counter)

    for c in t:
        if c not in counter:
            return False
        elif counter[c]==1:
            del counter[c]
        else:
            counter[c]-=1
    return True

print(containsDuplicate())