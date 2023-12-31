from random import choice


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
        """Makes a list of the words contained in the file of the path and
        print the number of words"""

        file = open(path)

        # make a self.words = [word, word, word]
        self.words = self.get_words(file)

        print(f"{len(self.words)} words read")

    def __repr__(self):
        return f"<WordFinder path={self.path}>"

    def get_words(self, file):
        """return a list of all the words in a file"""
        return [word.strip() for word in file]

    def random(self):
        """Return a random word from self.words"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):

    '''Special Word Finder: find words in a file, exclude blank lines
        and lines starting with # characters
    '''

    # def __init__(self, path):
    #     super().__init__(self, path)

    def __repr__(self):
        return f"<SpecialWordFinder path={self.path}>"

    def get_words(self, file):
        """ Return a list of all the words in a file,
            exclude blank lines and lines starting with # characters"""

        return [word for word in super().get_words(file)
                if not word.startswith("#") and word != ""]
