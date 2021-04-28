def naiveCompression(I,J,db):
'''
Returns a list of item sets J sorted in decreasing order by level of "cover" in dataset db.

Parameters:
	I (list of sets): Alphabet, list of singleton item sets
	J (list of sets): List of all item sets (permutations) made from I 
	db (list of lists): List of transactions comprising dataset 
Returns:
	codeSet (list of sets): minimal coding set of db
'''
	codeSet = standard(I,db)

	for singleton in I:
		J.remove(singleton)

	canItems = coverOrder(J,db)

	while len(canItems) > 0:
		cand = canItems.pop(0)

		canCodeSet = codeSet
		canCodeSet = standard(canCodeSet.append(cand), db)

		if compLen(canCodeSet, db) < compLen(codeSet, db):
			codeSet = canCodeSet

	return codeSet