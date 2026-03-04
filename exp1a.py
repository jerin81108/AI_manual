class Node:
 def __init__(self,d,l,f): self.data,self.level,self.fval=d,l,f
 def generate_child(self):
  x,y=self.find(self.data,'_'); v=[[x,y-1],[x,y+1],[x-1,y],[x+1,y]]; c=[]
  for i in v:
   child=self.shuffle(self.data,x,y,i[0],i[1])
   if child is not None: c.append(Node(child,self.level+1,0))
  return c
 def shuffle(self,puz,x1,y1,x2,y2):
  if 0<=x2<len(self.data) and 0<=y2<len(self.data):
   t=[x[:] for x in puz]; t[x2][y2],t[x1][y1]=t[x1][y1],t[x2][y2]; return t
  return None
 def find(self,puz,x):
  for i in range(len(self.data)):
   for j in range(len(self.data)):
    if puz[i][j]==x: return i,j
class Puzzle:
 def __init__(self,size): self.n,self.open,self.closed=size,[],[]
 def accept(self): return [input().split() for _ in range(self.n)]
 def f(self,s,g): return self.h(s.data,g)+s.level
 def h(self,s,g): return sum(1 for i in range(self.n) for j in range(self.n) if s[i][j]!=g[i][j] and s[i][j]!='_')
 def process(self):
  print("enter the start state matrix \n"); start=self.accept()
  print("enter the goal state matrix \n"); goal=self.accept()
  start=Node(start,0,0); start.fval=self.f(start,goal); self.open.append(start); print("\n")
  while True:
   cur=self.open[0]; print("="*49+"\n")
   for i in cur.data: print(*(j for j in i))
   if self.h(cur.data,goal)==0: break
   for i in cur.generate_child(): i.fval=self.f(i,goal); self.open.append(i)
   self.closed.append(cur); del self.open[0]; self.open.sort(key=lambda x:x.fval)
Puzzle(3).process()
