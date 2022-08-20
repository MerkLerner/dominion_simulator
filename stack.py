class Stack:
    def __init__(self, card_type=None, size=None):
        self._stack = []

        for _ in range(size):
            self._stack.append(card_type())

    def remove(self):
        if self.size <= 0:
            raise Exception

        self._stack.pop(-1)

    @property
    def size(self):
        return len(self._stack)