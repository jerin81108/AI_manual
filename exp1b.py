board = {k:{} for k in ['queen','row','col','nwtose','swtone']}
def init(n):
 for i in range(n): board['queen'][i],board['row'][i],board['col'][i]=-1,0,0
 for i in range(-n+1,n): board['nwtose'][i]=0
 for i in range(2*n-1): board['swtone'][i]=0
def free(i,j): return not(board['row'][i] or board['col'][j] or board['nwtose'][j-i] or board['swtone'][j+i])
def sq(i,j,v): board['queen'][i],board['row'][i],board['col'][j],board['nwtose'][j-i],board['swtone'][j+i]=j if v else -1,v,v,v,v
def solve(i):
 n = len(board['queen'])
 for j in range(n):
  if free(i,j):
   sq(i,j,1)
   if i==n-1 or solve(i+1): return True
   sq(i,j,0)
 return False
n=int(input("How many queens? "))
init(n)
if solve(0):
 for r in sorted(board['queen']): print((r,board['queen'][r]))
