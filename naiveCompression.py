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
	codeSet = standard(I,db) # Create code set using singleton items (alphsbet I)

	for singleton in I:
		J.remove(singleton)

	canItems = coverOrder(J,db) # Consider candidate item sets in cover order

	while len(canItems) > 0:
		cand = canItems.pop(0)

		canCodeSet = codeSet
		canCodeSet = standard(canCodeSet.append(cand), db)

		# Compare length of candidate and existing code sets
		if compLen(canCodeSet, db) < compLen(codeSet, db):
			codeSet = canCodeSet # Update code set if adding candidate itemset improves compression

	return codeSet