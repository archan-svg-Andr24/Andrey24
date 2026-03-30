class MinMaxWordFinder:
    def __init__(self):
        self.words = []

    def add_sentence(self, sentence):
        self.words.extend(sentence.split())

    def shortest_words(self):
        if not self.words:
            return []
        min_len = min(len(w) for w in self.words)
        result = [w for w in self.words if len(w) == min_len]
        result.sort()
        return result

    def longest_words(self):
        if not self.words:
            return []
        max_len = max(len(w) for w in self.words)
        result = sorted({w for w in self.words if len(w) == max_len})
        return result