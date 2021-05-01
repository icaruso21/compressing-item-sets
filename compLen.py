def compLen(codeSet, db):
'''
Returns the minimum description length (MDL) of a code set compressing a dataset db.

Parameters:
	codeSet (list of sets): Candidate coding set of db
	db (list of lists): List of transactions comprising dataset 
Returns:
	length (int): MDL of codeSet on db
'''

	# length = length (in bits) describing codeSet + length (in bits) describing db encoded with codeSet


	# L(D|H)
	lDH = 0


	# L(H)
	lH = 0


	return lH + lDH