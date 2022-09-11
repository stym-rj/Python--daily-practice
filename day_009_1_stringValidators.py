n = input()
count = 0
for i in n:
    if (i.isalnum()):
        print(True)
        count = count+1
        break
if count == 0:
    print(False)


count = 0
for i in n:
    if (i.isalpha()):
        print(True)
        count = count+1
        break
if (count == 0):
    print(False)


count = 0
for i in n:
    if (i.isdigit()):
        print(True)
        count = count+1
        break
if (count == 0):
    print(False)


count = 0
for i in n:
    if (i.islower()):
        print(True)
        count = count+1
        break
if (count == 0):
    print(False)


count = 0
for i in n:
    if (i.isupper()):
        print(True)
        count = count+1
        break
if (count == 0):
    print(False)
