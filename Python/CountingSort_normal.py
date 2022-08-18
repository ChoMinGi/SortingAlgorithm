import sys


def counting_sort(list):
    counting_array = []
    result = [0]*len(list)
    td = 0
    for i in range(max(list)+1):
        counting_array.append(list.count(int(i))+td)
        td = counting_array[i]
    for i in list:
        result[int(counting_array[i])-1] = i
        counting_array[i] -= 1
    print(*result, sep='\n')


addlist = []
n = int(input())
for i in range(n):
    addlist.append(int(sys.stdin.readline()))
counting_sort(addlist)
