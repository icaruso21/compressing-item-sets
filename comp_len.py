import math

def comp_len(codeSet, db, I):
	'''
	Returns the minimum description length (MDL) of a code set compressing a dataset db.

	Parameters:
		codeSet (list of sets): Candidate coding set of db
		db (list of lists): List of transactions comprising dataset 
		I (list of sets): Alphabet, list of singleton item sets
	Returns:
		length (int): MDL of codeSet on db
	'''
	# MDL = length (in bits) describing codeSet + length (in bits) describing db encoded with codeSet

	# L(D|H) - Length of dataset given code set

	dbCopy = [set(t) for t in db]
	itemFreq = [0 for i in codeSet]

	# Encode db with code set to find itemset frequencies
	for idx, itemset in enumerate(codeSet):
		for idx2, transaction in enumerate(dbCopy):
			if itemset.issubset(transaction):
				itemFreq[idx] += 1
				dbCopy[idx2] = transaction - itemset

	totalFreq = sum(itemFreq)

	# L(H) - length of code set representation
	lH = sum([(len(c) * math.ceil(math.log2(len(I)))) + math.ceil(math.log2(len(codeSet))) for idx, c in enumerate(codeSet) if itemFreq[idx] != 0])

	newItemFreq = []
	for i in itemFreq:
		if(i != 0):
			newItemFreq.append(i)
	itemFreq = newItemFreq

	lDH = -sum([f * math.log(f/totalFreq) for f in itemFreq])

	return lH + lDH