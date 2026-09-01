class Safe:
    def __init__(self):
        self._codes = [70, 76, 65, 71, 123, 118, 97, 117, 108, 116, 95, 97,
                        99, 99, 101, 115, 115, 95, 103, 114, 97, 110, 116,
                        101, 100, 125]

    # TODO: add an unlock() method that turns each number in self._codes
    # back into a character (they're character codes) and returns the
    # joined result.

safe = Safe()
print(safe.unlock())
