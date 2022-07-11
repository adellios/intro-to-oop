lines = ''
N = int(input())
for n in range(N):
    lines += input()+'\n'
W = [int(n) for n in lines.split()]
print('Gnomes:')
for x in range(N):
    if W[N*x]<W[N*x+1]<W[N*x+2] or W[N*x]>W[N*x+1]>W[N*x+2]:
        print('Ordered')
    else:
        print('Unordered')
