import _specify_dir
from typing import List
from math import floor, log10
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from FeatureSet.Extractors.utils import patterns
from FeatureSet.Extractors.data_prep import DataPrep


class NgramExtractor(DataPrep):
    """Extract ngrams"""

    def __init__(self, n) -> None:
        super().__init__()
        self.NGRAM = n
        self.WORD_PATTERN = patterns["word_pattern"]

    def __repr__(self) -> str: return f"Class: {self.__class__.__name__}"

    def extract_ngrams(self) -> List[List[str]]:
        ngrams_ex = []
        for file in self.get_sourcecode:
            n_gram = ngrams(word_tokenize(file), self.NGRAM)
            ngrams_ex.append([''.join(grams) for grams in n_gram])
        return ngrams_ex


class TF_IDF(NgramExtractor):
    """Extracts TF-IDF"""

    def __init__(self, n) -> None:
        super().__init__(n)