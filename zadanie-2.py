def func(list,start,end):
    for a in list:
        if a < start or a > end:
            yield a

list = [1,2,3,5,15,20,30,50,80]
for a in func(list,5,30):
    print(a)