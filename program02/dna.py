strand=input('Enter a DNA strand:' )
pattern=input('Enter the pattern:' )
start=strand.find(pattern)
end=int(start)+len(pattern)
mutatedPattern=strand[end-1:start-1:-1]
startPattern=strand.find(mutatedPattern)
endPattern=int(startPattern)+len(pattern)
mutated=strand[:start]+strand[endPattern-1:start-1:-1]+strand[endPattern:]
print('Mutated DNA sequence:'+mutated)
