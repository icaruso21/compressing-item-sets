import sys
import itertools
from naive_compression import naive_compression
from DBReader import getDB
from timeit import default_timer as timer

def main():
	'''
	Runs a version of dataset compression and prints the resulting coding set.

	Arguments:
		--v: Version of compression algorithm to run, default=naive
		--f: Path to .txt file representing dataset
	Returns:
		None
	'''
	# Parse arguments
	if len(sys.argv) != 3:
		print("main.py: Invalid Arguments.")
		print("Usage: python main.py version file_path")
		return
	else:
		if(sys.argv[1] == "pruning"):
			print("Running compression with pruning on data in " + sys.argv[2] + ".")
		else:
			print("Running naive compression (default) on data in " + sys.argv[2] + ".")

		# Read data file into memory
		data = getDB(sys.argv[2])

		print("Data: ", data)

		# Extract alphabet
		alphabet = set()
		for transaction in data:
			for item in transaction:
				alphabet.add(item)

		alphabet = [set(singleton) for singleton in alphabet]

		print("Alphabet: ", alphabet)

		# Extract all item sets J
		j = set()

		for transaction in data:
			for l in range(1,len(transaction)+1):
				subsets = list(map(set, itertools.combinations(transaction,l)))
				for s in subsets:
					j.add(frozenset(s))
			j.add(frozenset(transaction))

		j = list(j)

		print("J: ", j)


		# Run Compression Algorithm
		start = timer()
		if(sys.argv[1] == "pruning"):
			pass
		else:
			codeSet = naive_compression(alphabet, j, data)
		end = timer()

		runtime = (end - start)

		# Print final codeSet
		print("Code Set:")
		for itemset in codeSet:
			print(itemset)

		print("Compression took " + str(runtime) + " seconds on data in " + sys.argv[2] + ".")

if __name__ == '__main__':
	main()