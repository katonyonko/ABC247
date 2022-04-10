import io
import sys

_INPUT = """\
6
2
1
4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  ans=[1]
  for i in range(N-1):
    ans=ans+[i+2]+ans
  print(*ans)