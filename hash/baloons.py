# 1189. Maximum Number of Balloons

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.


from collections import Counter,defaultdict


def maxNumberOfBalloons():
    # text = "nlaebolko"
    text = "loonbalxballpoon"
    s='baloon'
    counter=defaultdict(int)
    for i in text:
        counter[i]+=1

    if any(i not in counter for i in s):
        return 0
    else:
        return min(counter['b'],counter['a'],counter['l']//2,counter['o']//2,counter['n'])


print(maxNumberOfBalloons())