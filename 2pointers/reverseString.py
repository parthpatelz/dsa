# 344. Reverse String
# # Write a function that reverses a string. The input string is given as an array of characters s.

# # You must do this by modifying the input array in-place with O(1) extra memory.



# # Example 1:

# # Input: s = ["h","e","l","l","o"]
# # Output: ["o","l","l","e","h"]
# # Example 2:

# # Input: s = ["H","a","n","n","a","h"]
# # Output: ["h","a","n","n","a","H"]

def reverseString():
    s = ["h","e","l","l","o"]
    n=len(s)
    l=0
    r=n-1
    while(l<r):
        s[l], s[r]= s[r],s[l]
        l+=1
        r-=1
    return s

print(reverseString())