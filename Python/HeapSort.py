# By not using seperate method;heap

def heap_sort(list):
    while len(list) > 0:
        result = []
        while len(list) > 1:
            if len(list) % 2 == 0:
                if list[len(list)-1] > list[int(len(list)/2-1)]:
                    list[len(list)-1], list[int(len(list)/2 -
                                            1)] = list[int(len(list)/2-1)], list[len(list)-1]
                result.append(list[len(list)-1])
                list = list[:-1]
            elif len(list) % 2 == 1:
                if list[len(list)-2] > list[int((len(list)-1)/2-1)]:
                    list[len(list)-2], list[int((len(list)-1)/2-1)
                                            ] = list[int((len(list)-1)/2-1)], list[len(list)-2]
                elif list[len(list)-1] > list[int((len(list)-1)/2-1)]:
                    list[len(list)-1], list[int((len(list)-1)/2-1)
                                            ] = list[int((len(list)-1)/2-1)], list[len(list)-1]
                result.append(list[len(list)-1])
                result.append(list[len(list)-2])
                list = list[:-2]
        res.append(*list)
        list = result


addlist = []
n = int(input())
res = []
for i in range(n):
    addlist.append(int(input()))
heap_sort(addlist)

print(res)
