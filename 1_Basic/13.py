'''1
23
456
78910'''
a=1
for i in range(1, 5):
    for j in range(i):
        print(a, end="")
        a+=1
    print()
