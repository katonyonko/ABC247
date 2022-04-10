import io
import sys

_INPUT = """\
6
1011
0000
1111
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  print('0'+S[:3])