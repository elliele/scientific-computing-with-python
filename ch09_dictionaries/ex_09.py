fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    #print(line)
    words = line.split()
    #print(words)
    for word in words:
        # combine the next 4 lines in one code
        # oldcount = di.get(word,0)
        #print(word,'old',oldcount)
        #newcount = oldcount +1
        #di[word] = newcount
        #print(word, 'new', newcount)

        #combine all above in one code
        #idiom: retrieve/create/update counter
        #di[word] = di.get(word,0) + 1
        #print (di)
        if word in di:
            di[word] = di[word] + 1
            #print('**Existing**')
        else:
            di[word] = 1
            #print('**New**')
        print(word, di[word])

largest = -1
theword = None
for k,v in di.items():
    print(k,v)
    if v > largest :
        largest = v
        theword = k # capture/remember the key that was largest
print('Done', largest, theword)
