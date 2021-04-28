def getDB(filename):
    '''
    Read in a dataset and formats it as a list of list [t[i]],
    where t is a transaction and i is an item  

    '''
    file = open(filename, "r")
    db = []
    for line in file:
        t = line.split(" ")
        db.append(t)
    return db
