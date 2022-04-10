import io
import sys

_INPUT = """\
6
4 3 1
1 2 3 1
5 2 1
1 3 2 4 1
5 1 1
1 1 1 1 1
10 8 1
2 7 1 8 2 8 1 8 2 8
4 2 3
5 5 8 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  N,X,Y=map(int,input().split())
  A=list(map(int,input().split()))
  A=[0 if A[i]>X or A[i]<Y else 1 if A[i]==X else 2 if A[i]==Y else 3 for i in range(N)]
  ans=0
  A=deque(A)
  if X==Y:
    while len(A)>0:
      while len(A)>0 and A[0]==0: A.popleft()
      tmp=[]
      while len(A)>0 and A[0]>0:
        x=A.popleft()
        tmp.append(x)
      n=len(tmp)
      ans+=n*(n+1)//2
  else:
    while len(A)>0:
      while len(A)>0 and A[0]==0: A.popleft()
      tmp=[]
      while len(A)>0 and A[0]>0:
        x=A.popleft()
        tmp.append(x)
      o,t=0,0
      n=len(tmp)
      for i in range(n):
        while o<i or o<n and tmp[o]!=1: o+=1
        while t<i or t<n and tmp[t]!=2: t+=1
        if max(o,t)<n:
          ans+=n-max(o,t)
  print(ans)