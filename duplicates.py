def duplicate(l):
    return list(set(l))

lst=list(map(float,input('Enter the list:').split()))
print(duplicate(lst))