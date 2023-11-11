"""Word Finder: finds random words from a dictionary."""

import random 

class WordFinder:
    ...
    """
    >>> wf = WordFinder("/usr/share/dict/words")
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
        """Read dictionary and reports # of items"""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words"""
        return [w.strip() for w in dict_file]
    
    def random(self):
        """Return random word"""
        return random.choice(self.words)
