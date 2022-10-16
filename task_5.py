data = [x for x in range(1,11)]

res = list(filter(lambda x: not x%2, data))
print (res)