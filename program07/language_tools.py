
class LanguageHelper():

    words = open('English.txt').readlines()
    global language
    language = set()
    
    
    def __init__(self,words):
        self.words = words
        for w in words:
            if isinstance(w,str):
                language.add(w)

    def __contains__(self,query):
        self.query = query
        if isinstance(query,str):
            if query in language:
                return True
            else:
                return False

    def getSuggestions(self,query):
        self.query = query
        found = False
        suggestions = []
        
        for w in language:
            for i in range(len(w)):
                if query not in language:

                    if query == query.capitalize():
                        w = w.capitalize()
                
                    if w == query[:i+1]+query[i+2:]:
                        suggestions.append(w)
                        break
        
                    if w[:i]+w[i+1:] == query[:i]+query[i+1:]:
                        suggestions.append(w)
                        break

                    if query == w[:i]+w[i+1:]:
                        suggestions.append(w)
                        break
        
                    if query == w[:i] + w[i+1:i-1:-1] + w[i+2:]:
                        suggestions.append(w)
                        if w[i] == w[i+1] and query[i] == query[i+1]:
                            suggestions.remove(w)
                            break

        if suggestions == '':
            return []
        else:
            suggestions.sort()
            return suggestions

        
        
