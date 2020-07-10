class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.undo_history = []  # a stack to store values that are ready for undo()
        self.redo_history = []  # a stack to store values that are ready for redo()

    def add(self, num: int):
        self.value += num
        self.undo_history.append(num)

    def subtract(self, num: int):
        return self.add(-num)

    def undo(self):
        return self.bulk_undo(1)

    def redo(self):
        return self.bulk_redo(1)

    def bulk_undo(self, steps: int):
        # take the top "steps" numbers from the stack
        undo_values = self.undo_history[-steps:]
        # remove them from undo_history
        self.undo_history = self.undo_history[:-steps]
        # add them to redo_history in reverse order (because it's a stack insert)
        undo_values.reverse()
        self.redo_history.extend(undo_values)
        self.value -= sum(undo_values)

    def bulk_redo(self, steps: int):
        # take the top "steps" numbers from the stack
        redo_values = self.redo_history[-steps:]
        # remove them from redo_history
        self.redo_history = self.redo_history[:-steps]
        # add them to undo_history in reverse order (because it's a stack insert)
        redo_values.reverse()
        self.undo_history.extend(redo_values)
        self.value += sum(redo_values)
