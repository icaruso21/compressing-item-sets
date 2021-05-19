from standard import standard
from comp_len import comp_len
from cover_order import cover_order

def naive_compression(I,J,db):
	'''
	Returns a list of item sets J sorted in decreasing order by level of "cover" in dataset db.

	Parameters:
		I (list of sets): Alphabet, list of singleton item sets
		J (list of sets): List of all item sets (permutations) made from I 
		db (list of lists): List of transactions comprising dataset 
	Returns:
		codeSet (list of sets): minimal coding set of db
	'''
	codeSet = standard(I,db) # Create code set using singleton items (alphabet I)

	for singleton in I:
		try:
			J.remove(singleton)
		except:
			continue

	canItems = cover_order(J,db) # Consider candidate item sets in cover order

	#print("Base code set: ")
	#print(codeSet)
	#print(comp_len(codeSet, db, I))
	#print("---------------")

	while len(canItems) > 0:
		cand = canItems.pop(0)

		canCodeSet = codeSet.copy()
		canCodeSet.append(cand)
		canCodeSet = cover_order(canCodeSet, db)

		#print(canCodeSet)

		# Compare length of candidate and existing code sets
		if comp_len(canCodeSet, db, I) < comp_len(codeSet, db, I):
			codeSet = canCodeSet # Update code set if adding candidate itemset improves compression

		#print(comp_len(canCodeSet, db, I))

	return codeSet