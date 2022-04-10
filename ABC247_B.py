import io
import sys

_INPUT = """\
6
3
tanaka taro
tanaka jiro
suzuki hanako
3
aaa bbb
xxx aaa
bbb yyy
2
tanaka taro
tanaka taro
3
takahashi chokudai
aoki kensho
snu ke
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  ans='Yes'
  N=int(input())
  name=[list(input().split()) for _ in range(N)]
  for i in range(N):
    tmp=set()
    for j in range(N):
      if i!=j: tmp.add(name[j][0]); tmp.add(name[j][1])
    if name[i][0] in tmp and name[i][1] in tmp: ans='No'
  print(ans)