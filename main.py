# Part of Speech Tagger, defining a general HMM class.
# The HMM class will have a train method that relies
# on duck typing so it can accept general types.

import re, collections

# TODO: Remove non-word characters from the list of tokens
# TODO: Define a data structure for our HMM and for getting
#		the probabilities
# TODO: Define a data structure for part-of-speech tagged
#		text

class HMM:
	def train(self):
		"""
		Train the trigram model using linear interpolation,
		where we employ simple counts of decreasing n-grams
		to define our probabilities.
		"""
		return 0

	def viterbi(self):
		"""
		Recursively walk through the viterbi iteration and
		provide a most common path.
		"""
		return 0

def extract_sentences(*files):
	"""
	Take in a variable number of arguments, each of which
	is a file name and returns the unigram counts for each
	word.
	"""
	sentences = []
	for file_name in files:
		# Define a (terrible) regex to split the sentences in
		# a file. It has a look-behind to match for common uses
		# of the period, and a look-ahead to ensure that the
		# next sentence starts with a capital letter or a number.
		sentences.extend([sentence.strip() for sentence in re.split(r"(?<!\s)(?<!\be\.g|\bi\.e)(?<!\b[Mm]r|\b[Mm]s|\b[Dd]r|\bvs|\.\.)(?<!\b[Mm]rs)(?:\.|\!|\?)(?=\s+[A-Z0-9\(\)])", file(file_name).read())])
		# I would just like to note that the above line of code
		# is what happens when I program while tired.
	return sentences

def get_ngrams(sentences, n):
	"""
	Get an n-gram for a given array of sentences after first
	standardizing them with an initial and post character.
	"""
	assert n >= 1, "You must use at least a unigram"

	for sentence in sentences:
		tokens = sentence.split(" ")
		# We want to insert the * * ... STOP for the sentence
		for _ in range(n-1):
			tokens.insert(0, "*")
		tokens.extend(["STOP"])
		for index, token in enumerate(tokens):
			if index >= n:
				print token
		

get_ngrams(extract_sentences('test.txt'), 3)