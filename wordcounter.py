
fname = input("Enter File: ")
if len(fname) < 1: 
    fname = "sample.txt"

try:
    with open(fname) as handle:
        word_count = {}
        for line in handle:
            words = line.strip().split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
        
        if word_count:  # Check if dictionary isn't empty
            most_common_word = max(word_count, key=word_count.get)
            print(most_common_word, word_count[most_common_word])
        else:
            print("No words found in file")
            
except FileNotFoundError:
    print(f"File '{fname}' not found")



#fname = input("Enter File: ")
#if len(fname) < 1 : fname = "sample.txt"
#handle = open(fname)
#
#di = dict()
#
#for lin in handle:
#    lin = lin.rstrip()
#    wds = lin.split()
#    for w in wds:
#        di[w] = di.get(w,0) + 1
# print(di)
# largest value
#largest = -1
#theword = None
#for k,v in di.items() :
    # print(k,v)
#    if v > largest :
#        largest = v
#        theword = k
#print(theword, largest)


# counter method 1
        # oldcount = di.get(w,0)
        # print(w,"old",oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount
        # print(w,"new",oldcount)

# counter method 2
        # print(w)
        # if w in di :
            # di[w] = di[w] + 1
            # print("***Existing")
        # else :
            # di[w] = 1
            # print("***New")
        # print(w,di[w])

