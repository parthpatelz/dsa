
# for i in range(len(t)):
#     for j in range(len(s)):
#         if t[i] != s[j]:
#             j+=1
#             ans=False
#         elif t[i] ==s[j]:
#             ans = True
#             i+=1
#             j+=1
def isSubsequence():
    
    s='pqr'
    t='apbqcr'
    # ans=False
    S= len(s)
    T=len(t)

    if s=='': return False
    if S>T: return False

    j=0
    i=0

    for i in range(T):
        if t[i]==s[j]:
            if j== (S-1):
                return True
            j+=1

    return False


print(isSubsequence())