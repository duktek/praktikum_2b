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
        i = 1
        bil = 0
        while i <= x:
            if x%i==0:
                bil+=1
            i+=1
        if bil == 2:
            print(x)