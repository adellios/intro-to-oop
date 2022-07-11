manager = open('dup.txt')
lines = manager.readlines()
W = [x.split() for x in lines]
W.remove(['0'])
for x in range(len(W)):
    W[x].remove(W[x][0])
    W[x].append('$')
Q = [', '.join(W[x]) for x in range(len(W))]
Q = '. '.join(Q)
Q = Q.split()

for x in range(len(Q)):
        if Q[x] == Q[x+1]:
            Q.remove(Q[x])
print(Q)




