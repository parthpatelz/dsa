from collections import defaultdict,Counter
def isAnagram():
    # counter={}
    s = "anagram"
    t = "anaramg"


    S=Counter(s)
    T=Counter(t)
    if S != T:
        return False
    else:
        return True

print(isAnagram())