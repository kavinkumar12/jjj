x1,y1=input().split()
x=int(x1)
y=int(y1)
for z in range(x,y):
  d=0
  c=z
  i=z
  while c!=0:
    b=c%10
    a=(b**3)
    c=c//10
    d=a+d
  #print (i,"",d)
  if i==d:
    print(i,end="")
