a=int(input())
b=c
d=0
while c!=0:
  c=c%10
  a=c//10
  b=(a*10)+b
if b==a:
  print("yes")
else:
  print("no")
