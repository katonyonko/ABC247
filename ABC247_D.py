import io
import sys

_INPUT = """\
6
4
1 2 3
2 2
1 3 4
2 3
2
1 1000000000 1000000000
2 1000000000
5
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  Q=int(input())
  d=deque()
  for i in range(Q):
    query=input().split()
    if query[0]=='1':
      x,c=map(int,query[1:])
      d.append([x,c])
    else:
      c=int(query[1])
      ans=0
      while c>0:
        tmp=d.popleft()
        if c>=tmp[1]: ans+=tmp[0]*tmp[1]; c-=tmp[1]
        else: ans+=tmp[0]*c; d.appendleft([tmp[0],tmp[1]-c]); c=0
      print(ans)