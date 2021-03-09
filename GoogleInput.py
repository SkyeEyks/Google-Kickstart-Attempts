class GoogleInput:
    def __init__(self, *inputs):
        self.i = -1
        self.inputs = inputs

    def get(self) -> str:
        self.i += 1
        return self.inputs[self.i]

    def reset(self):
        self.i = -1
