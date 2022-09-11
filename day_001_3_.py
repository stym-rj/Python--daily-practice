sunday=[7, 14, 21, 28]
saturday=[6, 13, 20, 27]

t=int(input())

for i in range(t):
    defaultList= sunday + saturday;
    setDefaultList=set(defaultList)
    numFest=int(input())
    festList=[]

    n=input()
    m=n.split(" ")
    for i in m:
        festList.append(int(i))

    setFestList=set(festList)
    
    setDefaultList.update(setFestList)
    listDefaultList=list(setDefaultList)
    print(len(listDefaultList))