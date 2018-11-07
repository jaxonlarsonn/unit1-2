import math
A=float(input())
B=float(input())
H=float(input())
days=H/(A-B)
if (A>H):
    print(1)
elif(H>A):
    print(math.ceil(days)
