import sys
import math
line = sys.stdin.readline().strip().split()
x, y, z = int(line[0]), int(line[1]), int(line[2])
max_n = max(x, y, z)
min_n = min(x, y, z)
x, y, z = min_n, x+y+z-min_n-max_n, max_n

def isTriangle(i, j, k):
    if i + j > k and j + k > i and i + k > j:
        return True
    else:
        return False

count = 0
for i in xrange(1, z+1):
    for j in xrange(1, y+1):
        max_k = max(i, j)
        min_k = min(i, j)
        down_bound = max_k - min_k + 1
        upper_bound = x if x < i+j-1 else i+j-1
        temp = 1
        if down_bound == upper_bound:
            count += 1
        else:
            count += len(xrange(down_bound, upper_bound+1))
            count = count % 1000000007
            temp = len(xrange(down_bound, upper_bound+1))
        print (i, j), down_bound, upper_bound, temp
print count % 1000000007
