https://www.geeksforgeeks.org/precision-handling-python/
          import math
          a = float(input())
          b = float(input())

          c = a//b
          d = a/b

          print(math.trunc(c))
          print(d)

        
        
2.Accept list to add [i,j and k] such that > n

X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

ans = [[i, j, k] 

for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1) if i + j + k != N]

print (ans)
