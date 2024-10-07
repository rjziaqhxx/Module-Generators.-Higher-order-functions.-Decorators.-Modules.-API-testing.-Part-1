def func(a,b):
    if a > b:
        max = a
        min = b
    else:
        max = b
        min = a
    for num in range(min,max):
        if num % 2 != 0:
            yield num

for odd in func(2,16):
    print(odd)