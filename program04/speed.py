miles = []
manager = open('speed.txt')
lines = manager.readlines()
for x in lines:
    found = False
    x = list(int(k) for k in x.split())
    if len(x) == 1:
        if x[0] == -1:
            found = True
            break
        miles.append(0)
        hours = 0
    if len(x) > 1:
        miles[-1] += (x[1]-hours)*x[0]
        hours = x[1]
for x in range(len(miles)):
    print(str(miles[x])+' miles\n')
