n = int(input())
a=[]
for i in range(n):
    a.append(int(input()))
td=0

for i in range(n-1):
    for j in range(n-1-i):
        if a[j+1]<a[j]:
            td=a[j+1]
            a[j+1]=a[j]
            a[j]=td

print(*a, sep='\n')