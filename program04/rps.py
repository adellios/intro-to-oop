manager = open('rps.txt')
x = manager.readline()
y = manager.readline()
P1 = list(x)
P2 = list(y)
lines = manager.readlines()
for r in range(2):
    lines.remove('E\n')
counter1=counter=0
counter2=counter=0
for x in range(len(P1)):
    if P1[x] == P2[x]:
        pass
    elif P1[x] == 'R' and P2[x] =='S':
        counter1+=1
    elif P1[x] == 'R' and P2[x] == 'P':
        counter2+=1
    elif P1[x] == 'S' and P2[x] == 'P':
        counter1+=1
    elif P1[x] == 'S' and P2[x] == 'R':
        counter2+=1
    elif P1[x] == 'P' and P2[x] == 'R':
        counter1+=1
    elif P1[x] == 'P' and P2[x] == 'S':
        counter2+=1
print(counter1)
print(counter2)
