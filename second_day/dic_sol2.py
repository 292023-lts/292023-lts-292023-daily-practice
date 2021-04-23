numlist = [1, 2, 3, 4]
newdict = current = {}
for name in numlist:
    current[name] = {}
    current = current[name]
print(newdict)