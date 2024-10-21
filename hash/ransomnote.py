# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input:
# ransomNote = "aca"
# magazine = "aab"
# # Output: true



from collections import defaultdict,Counter
def containsDuplicate():
    ransomNote = "aas"
    magazine = "aab"
    s=defaultdict(int)
    for i in magazine:
        s[i]+=1

    for i in ransomNote:
        if i not in s:
            return False
        elif s[i]==1:
            del s[i]
        else:
            s[i]-=1

    return True



print(containsDuplicate())