import os
def diskUsage():
    path = input('Path: ')
    if path[0] == '/':
        path = path[1:]
        #Gets rid of first /
    total = 0
    #Counter for total bytes
    for i in os.listdir(path):
        if os.path.isdir(path+'/'+i) == True:
            #If path is a directory, creates counter for total bytes in directory
            tot = 0
            for k in os.listdir(path+'/'+i):
                tot += os.path.getsize(path+'/'+i+'/'+k)
                print(os.path.getsize(path+'/'+i+'/'+k),'\t'+'/'+path+'/'+i+'/'+k)
                #Returns number of bytes for each child in a directory
                total += os.path.getsize(path+'/'+i+'/'+k)
            print(tot+os.path.getsize(path+'/'+i),'\t'+'/'+path+'/'+i)
            #Returns overall usage for directory
        else:
            print(os.path.getsize(path+'/'+i),'\t'+'/'+path+'/'+i)
            #Returns number of bytes for each non-directory child in path
            total += os.path.getsize(path+'/'+i)
    print(total,'\t'+'/'+path)
    #Returns total usage for path
