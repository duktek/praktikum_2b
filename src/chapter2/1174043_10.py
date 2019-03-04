a = 1
b = 1
c = 7
d = 4
e = 0
f = 4
g = 3
array =[]
array.append(a)
array.append(b)
array.append(c)
array.append(d)
array.append(e)
array.append(f)
array.append(g)
for x in array:
    if x != 0:
        if x%2==1:
            print(x, end = "")