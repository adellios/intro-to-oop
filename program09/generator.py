
class Generator():
    
    def __init__(self,source,n):
        super().__init__()
    
        self._source = source
        self._n = n
        
        recent = source[-n:]
        first = source[:n]
    
        keys = []
        for i in range(len(source)-1):
            if len(source[i:i+n]) == n:
                keys.append(source[i:i+n])

        pairs = []
        for k in range(len(keys)):
            if k < len(keys)-1:
                list = {keys[k]:keys[k+1][n-1]}
            else:
                list = {keys[k]:' '}
            pairs.append(str(list))
        
        d = {pairs[k][2:2+n]:{} for k in range(len(pairs))}
        for k in d:
            for i in range(len(pairs)):
                if pairs[i][2:2+n] == k:
                    d[k].update({pairs[i][6+n]:pairs.count(pairs[i])})
        
        prob = {k:{} for k in d}
        for k in d:
            s = 0
            for i in d[k]:
                s += d[k][i]
                p = d[k][i]/s
                prob[k].update({i:d[k][i]*p for i in d[k]})
                if d[k][i] > 1.0:
                    prob[k].update({i:1.0})
        global new
        new = min(prob[first])
        global c
        c = 0
        pass

    
    def nextChar(self):
        global c
        c += 1
        self._new = new
        return new
        first = first[-1:]+new
            
