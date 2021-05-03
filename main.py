import sys
import naive_compression, DBReader

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
		print("Invalid Arguments.")
		print("Usage: python main.py --v version --f file_path")
		return
	else:
		print("Running naive compression on data in " + sys.argv[2] + ".")

		# Read data file into memory
		data = DBReader(sys.argv[2])

		# Extract alphabet
		alphabet = set()
		for transaction in data:
			for item in transaction:
				alphabet.add(item)

		# Extract all item sets J
		j = []

		codeSet = naive_compression(alphabet, j, data)

		# Print final codeSet
		for itemset in codeSet:
			print(itemset)
