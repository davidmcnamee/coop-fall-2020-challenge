class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.changesMade = []  # a stack to store values that are ready for undo()
        self.changesUndone = []  # a stack to store values that are ready for redo()

    def add(self, num: int):
        self.value += num
        self.changesMade.append(num)

    def subtract(self, num: int):
        return self.add(-num)

    def undo(self):
        return self.bulk_undo(1)

    def redo(self):
        return self.bulk_redo(1)

    def bulk_undo(self, steps: int):
        # take the top "steps" numbers from the stack
        undoneValues = self.changesMade[-steps:]
        # remove them from changesMade
        self.changesMade = self.changesMade[:-steps]
        # add them to changesUndone in reverse order (because it's a stack insert)
        undoneValues.reverse()
        self.changesUndone.extend(undoneValues)
        self.value -= sum(undoneValues)

    def bulk_redo(self, steps: int):
        # take the top "steps" numbers from the stack
        redoneValues = self.changesUndone[-steps:]
        # remove them from changesUndone
        self.changesUndone = self.changesUndone[:-steps]
        # add them to changesMade in reverse order (because it's a stack insert)
        redoneValues.reverse()
        self.changesMade.extend(redoneValues)
        self.value += sum(redoneValues)
