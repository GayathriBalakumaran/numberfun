N=int(input())
for i in range(N):
  lst=list(map(int,input().split(' ')))

  if( lst[0]+lst[1]==lst[2]  or lst[0]*lst[1]==lst[2]
   or lst[0]-lst[1]==lst[2] or lst[1]-lst[0]==lst[2]
   or lst[0]/lst[1]==lst[2] or lst[1]/lst[0]==lst[2]):
    print("Possible")

  else:
    print("Impossible")