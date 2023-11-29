class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Makes a list of the words contained in the file of the path"""
        file = open(path)

        # make a self.words = [word, word, word]
        self.words = self.getWords(file)

    # call a print method
    def getWords(self, file):
        return [word.strip() for word in file]

    def printWords(self):
        # print 'len(self.words) words read'
        ...