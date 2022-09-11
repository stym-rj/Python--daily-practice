from operator import itemgetter

t=int(input())
lst1=[]

for i in range(t):
    lst2=[]
    
    temp1=input()
    temp2=float(input())
    lst2.append(temp1)
    lst2.append(temp2)
    lst1.append(lst2)

lst1.sort(key = itemgetter(1))

ans=[]
count=0
for i in range(1,len(lst1)-1):
    if lst1[i][1]==lst1[0][1]:
        continue
    if lst1[i][1]==lst1[i+1][1]:
        if count:
            ans.append(lst1[i+1][0])
        else:
            ans.append(lst1[i][0])
            ans.append(lst1[i+1][0])
            count=count+1

ans.sort()
for i in ans:
    print(i)
