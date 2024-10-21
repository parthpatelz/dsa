# 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# m, n = len(matrix), len(matrix[0])

# print(m)
# print(n)
def spiralOrder():
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        # matrix = [[1,2,3],[4,5,6],[7,8,9]]
        m, n = len(matrix), len(matrix[0])
        UP,RIGHT,DOWN,LEFT=0,1,2,3
        UP_WALL,RIGHT_WALL,DOWN_WALL,LEFT_WALL=0,n,m,-1
        direction=RIGHT
        ans=[]
        i,j=0,0

        while(len(ans)!=m*n):
                if direction==RIGHT:
                        while j<RIGHT_WALL :
                                ans.append(matrix[i][j])
                                j+=1
                        i+=1
                        j-=1
                        RIGHT_WALL-=1
                        direction=DOWN
                elif direction==DOWN:
                        while i<DOWN_WALL:
                                ans.append(matrix[i][j])
                                i+=1
                        i-=1
                        j-=1
                        DOWN_WALL-=1
                        direction=LEFT
                elif direction==LEFT:
                        while j>LEFT_WALL:
                                ans.append(matrix[i][j])
                                j-=1
                        i-=1
                        j+=1
                        LEFT_WALL+=1
                        direction=UP
                elif direction==UP:
                        while i>UP_WALL:
                                ans.append(matrix[i][j])
                                i-=1
                        i+=1
                        j+=1
                        UP_WALL+=1
                        direction=RIGHT
        return ans

print(spiralOrder())


# ans=[]
#         m,n = len(matrix),len(matrix[0])
#         UP,RIGHT,DOWN,LEFT=0,1,2,3
#         UP_WALL,RIGHT_WALL,DOWN_WALL,LEFT_WALL=0,n,m,-1
#         direction=RIGHT
#         i,j=0,0

#         while len(ans)!=m*n :
#             if direction==RIGHT:
#                 while j<RIGHT_WALL:
#                     ans.append(matrix[i][j])
#                     j+=1
#                 i+=1
#                 j-=1
#                 RIGHT_WALL-=1
#                 direction=DOWN

#             elif direction==DOWN:
#                 while i<DOWN_WALL:
#                     ans.append(matrix[i][j])
#                     i+=1
#                 i-=1
#                 j-=1
#                 DOWN_WALL-=1
#                 direction=LEFT

#             elif direction ==LEFT:
#                 while j>LEFT_WALL:
#                     ans.append(matrix[i][j])
#                     j-=1
#                 j+=1
#                 i-=1
#                 LEFT_WALL-=1
#                 direction=UP

#             elif direction ==UP:
#                 while i>UP_WALL:
#                     ans.append(matrix[i][j])
#                     i-=1
#                 i+=1
#                 j+=1
#                 UP_WALL+=1
#                 direction=RIGHT

#         return ans