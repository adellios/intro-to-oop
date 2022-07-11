from random import sample, randint
choices = sorted(sample(range(1,20), randint(2,6)))
alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
A = 0
B = 1
C = 2
D = 3
E = 4
F = 5
c = len(choices)
w = [alphabet[i] + ') ' + str(choices[i]) + '%' for i in range(c)]
limit = 1000000

def greeting():
    print('\nPlease select an interest rate:')
    print('\n'.join(map(str, w)))

def getRate(choices):
    global e
    e = input('Enter A-' + str(alphabet[c-1]) + ': ')
    while e not in alphabet[:c]:
	    print('That is not a valid selection.\n')
	    print('Please select an interest rate:')
	    print('\n'.join(map(str, w)))
	    try:
		    e = input('Enter A-' + str(alphabet[c-1]) + ': ')
	    except ValueError:
		    print('That is not a valid selection.\n')

def getPrincipal(limit=1000000):
    global p
    p = 0
    while not 0 < int(p) < limit:
            try:
                p = float(input('\nEnter the principal: '))
                if int(p) < 0:
                    print('You must enter a positive amount.\n')
                if int(p) > limit:
                    print('The principal can be at most 10000000.\n')
            except ValueError:
                print('Please enter a number.\n')

def computeBalance(p, Rate):
    global Balance
    Balance = '$' + '%.2f' % (float(p) + p*Rate)

def results():
    print('\nInitial Principal    Interest Rate    End of Year Balance\n=========================================================')
    print(P,' '*(19-len(P)),Rate,' '*11,Balance,'\n')



def askYesNo():
    i = input('Another Computation [y/n]? ')
    if i[0] == 'n' or i[0] == 'N':
        print('\nQuitting program. Bye.')
    while i[0] == 'y' or i[0] == 'Y':
        try:
            greeting()
            getRate(choices)
            getPrincipal(limit=1000000)
            computeBalance(p, Rate)
            results()
            i = input('Another Computation [y/n]? ')
        except ValueError:
            print('That is not a valid selection.\n')

greeting()

getRate(choices)

E = alphabet.index(e)
Rate = choices[E]/100

getPrincipal(limit=1000000)

P = '$' + str(p)

computeBalance(p, Rate)

results()

askYesNo()
