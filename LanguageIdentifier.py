# A simple language identifier class 
# Given an input text, one has to identify
# which language the word belongs to


class LanguageIdentifier:
	def __init__(self):
		self.languages = ["English", "Spanish", "French"]
		self.matrix_dict = {}

		for l in self.languages:
			self.matrix_dict[l] = [[0]*26]*26

	def create_bigrams(self, word):
		return [(word[i], word[i+1]) for i in range(len(word) - 1)]

	def create_bigram_transition_matrix(self, language, wordlist):
		dict = {}

		for word in wordlist:
			bigrams = self.create_bigrams(word)

			for bigram in bigrams:
				if dict.get(bigram) == None:
					dict[bigram] = 1
				else:
					dict[bigram] = dict[bigram] + 1
		N = sum(dict[key] for key in dict.keys())
		print dict

		for i in range(0,26):
			for j in range(0,26):
				first = chr(i+97)
				second = chr(j+97)

	    		if dict.get((first, second)) == None:
	    			continue
	    		else:
	    			print dict[(first, second)]
	    			fract = dict[(first, second)]/float(N)
	    			self.matrix_dict[language][i][j] = fract
	    			print fract, first, second

	def identify_language(self, word):
		bigrams = self.create_bigrams(word)
		maximum = None
		probMax = 0
		probNow = 0

		for language in self.languages:
			for bigram in bigrams:
				first, second = ord(bigram[0]) - 97, ord(bigram[1]) - 97
				probNow = probNow + self.matrix_dict[language][first][second]

			print probNow

			if probNow > probMax:
				maximum = language

			probNow = 0

		return maximum


if __name__ == '__main__':
	English = ["hello", "come", "go", "sit", "stand", "fight", "give", "return", "class", "create"]
	Spanish = ["hola", "ven", "salir", "sentar", "estar", "lucha", "dar", "regreso", "clase", "crear"]
	French = ["bonjour", "venez", "aller", "sieger", "supporter", "combattre", "donner", "revenir", "classe", "creer"]

	languageIdentifier = LanguageIdentifier()

	languageIdentifier.create_bigram_transition_matrix("English", English)
	languageIdentifier.create_bigram_transition_matrix("Spanish", Spanish)
	languageIdentifier.create_bigram_transition_matrix("French", French)

	print "goal is in: ", languageIdentifier.identify_language("goal")






