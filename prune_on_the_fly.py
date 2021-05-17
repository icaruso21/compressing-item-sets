def prune_on_the_fly(canCodeSet, codeSet, db, I):
	'''
	Removes an element from CanCodeSet and check if the resulting compression is better than that of CodeSet itself.

	Parameters:
		canCodeSet (list of sets): Candidate coding set of db
		codeSet (list of sets): Current coding set of db
		db (list of lists): List of transactions comprising dataset 
		I (list of sets): Alphabet, list of singleton item sets
	Returns:
		codeSet (list of sets): minimal coding set of db
	'''

	
	pruneSet = [j for j in codeSet if cover(j, canCodeSet) < cover(j, codeSet)]
	# pruneSet contains all J from codeSet where cover(J, canCodeSet) < cover(J, codeSet)

	pruneSet = standard(pruneSet, db)

	while(len(pruneSet) > 0):
		cand = pruneSet.pop()

		posCodeSet = codeSet.copy()
		posCodeSet.remove(cand) 

		if comp_len(posCodeSet, db, I) < comp_len(canCodeSet, db, I):
			canCodeSet = posCodeSet

	return canCodeSet


def cover(j, codeSet):
	'''
	Finds the cover of an itemset in a coding set.

	Parameters:
		j (set if ints): Itemset in codeSet
		codeSet (list of sets):  Coding set of db
	Returns:
		cover (float): 
	'''
	cover = 0
	#codeSetLen = [len(j) for j in codeSet]

	for itemset in codeSet:
		if j.issubset(itemset):
			cover += len(j)

	return cover