class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'

    """

    def __init__(self, path):
        """Makes a list of the words contained in the file of the path and print
        the number of words"""

        file = open(path)

        # make a self.words = [word, word, word]
        self.words = self.getWords(file)

        print(f"{len(self.words)} words read")

    # TODO: write a __repr__
    def __repr__(self):
        return f"<WordFinder path={self.path}>"

    def getWords(self, file):
        """return a list of all the words in a file"""
        return [word.strip() for word in file]

    # TODO: return a random word from self.words
    # do not re-read the list of words each and should work with the
    # already-read-in words list
    def random(self):
        """"""
        ...
