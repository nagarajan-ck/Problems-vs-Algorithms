def get_min_max(ints):
    if(len(ints)==0):
        return "Empty input list"
    min = ints[0]
    max = min
    for i in ints:
        if(i>max):
            max =i
        if(i<min):
            min = i
    return (min,max)


print(get_min_max([6,2,4,2,55,32,4,6,1,0,-3,6,222,-42,53,233,-123])) #prints (-123, 233)

print(get_min_max([1])) #prints (1, 1)

print(get_min_max([])) #prints 'Empty input list'
