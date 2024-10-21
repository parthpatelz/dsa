s = " name is khan"

# print(s.__contains__("o"))


# fxyzor i in s:
#     if i != " ":
#         print (i)



def mergeAlternately():
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # merged = ""

        word1 ="abc"
        word2="xyzop"

        A , B = len(word1), len(word2)
        a,b=0,0
        s=[]
        print(a,b)
        while (A>a and B>b):
                s.append(word1[a])
                a= a+1
                s.append(word2[b])
                b=b+1


        print(a,b)
        while (A>a):
                s.append(word1[a])
                a= a+1
        while(B>b):
                s.append(word2[b])
                b=b+1

        return "".join(s)



print(mergeAlternately())