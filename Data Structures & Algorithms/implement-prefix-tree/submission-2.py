class PrefixTree:

    def __init__(self):
        self.store = set()

    def insert(self, word: str) -> None:
        self.store.add(word)

    def search(self, word: str) -> bool:
        return word in self.store

    def startsWith(self, prefix: str) -> bool:
        l = len(prefix)
        for w in self.store:
            if w[:l] == prefix:
                return True
        return False

        