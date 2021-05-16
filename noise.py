def noise(I, codeSet, db):
    '''
	Returns a list of freak transactions in the database.

	Parameters:
		I (list of sets): Alphabet, list of singleton item sets
		codeSet (list of sets): Coding set of db
		db (list of lists): List of transactions comprising dataset 
	Returns:
		noise (set of sets): set of freak transactions in the database
	'''
    noise = {}
    for t in range(0, len(db)):
        if len(db[t]) < len(codeSet[t]): # if L_S(t) > L_{CS}(t)
            noise.add(frozenset(db[t]))

    return noise
