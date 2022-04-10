import io
import sys

_INPUT = """\
6
3
1 2 3
2 1 3
5
2 3 5 4 1
4 2 1 3 5
8
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353 
  N=int(input())
  P=list(map(int,input().split()))
  Q=list(map(int,input().split()))
  P=[P[i]-1 for i in range(N)]
  Q=[Q[i]-1 for i in range(N)]
  X=[[P[i],Q[i]] for i in range(N)]
  X.sort()
  ans=1
  flag=[0]*N
  for i in range(N):
    if flag[i]==1: continue
    idx=i
    tmp=set()
    while idx not in tmp: tmp.add(idx); flag[idx]=1; idx=X[idx][1]
    n=len(tmp)
    tt=0
    dp1=[[0]*2 for _ in range(n)]
    dp1[0][1]=1
    for j in range(n-1):
      dp1[j+1][0]=dp1[j][1]
      dp1[j+1][1]=sum(dp1[j])%mod
    tt=(tt+sum(dp1[-1]))%mod
    dp2=[[0]*2 for _ in range(n)]
    dp2[0][0]=1
    for j in range(n-1):
      dp2[j+1][0]=dp2[j][1]
      dp2[j+1][1]=sum(dp2[j])%mod
    tt=(tt+dp2[-1][1])%mod
    ans=(ans*tt)%mod
  print(ans)