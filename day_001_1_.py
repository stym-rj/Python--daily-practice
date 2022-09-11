n=int(input())

for i in range(n):

    test=input()
    m=test.split()
    
    supriya=int(m[0])
    namita=int(m[1])

    f_supriya=int(supriya/10)
    f_namita=int(namita/10)

    print(f_namita-f_supriya)