class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.done = []
        self.undone = []

    def add(self, num: int):
        self.value += num
        self.done.append(num)
        return self.value

    def subtract(self, num: int):
        self.value -= num
        self.done.append(-num)
        return self.value

    def undo(self):
        last = self.done.pop()
        self.value -= last
        self.undone.append(last)
        return self.value

    def redo(self):
        last = self.undone.pop()
        self.value += last
        self.done.append(last)
        return self.value

    def bulk_undo(self, steps: int):
        for i in range(steps):
            self.undo()
        return self.value

    def bulk_redo(self, steps: int):
        for i in range(steps):
            self.redo()
        return self.value
