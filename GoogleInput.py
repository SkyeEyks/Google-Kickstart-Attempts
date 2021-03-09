import sys
import _io


class GoogleInput:
    def __init__(self, input_dir: str, outputs_dir: str = None):
        Print.googleInput = self
        self.i = -1
        with open(input_dir, 'r') as f:
            self.inputs = f.read().split('\n')
        self.output = ''
        self.ans = None
        if outputs_dir:
            with open(outputs_dir, 'r') as f:
                self.ans = f.read()

    def get(self) -> str:
        self.i += 1
        return self.inputs[self.i]

    def reset(self):
        self.i = -1

    def checkOutput(self):
        if self.output == self.ans+"\n":
            Print.out.write('Your output is correct! :)\n')
        else:
            Print.out.write('Your output isn\'t correct :(\n')


class Print(_io.TextIOWrapper):
    out: _io.TextIOWrapper
    googleInput: GoogleInput

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Print.out = sys.stdout
        sys.stdout = self

    def write(self, *args, **kwargs):
        Print.out.write(*args, **kwargs)
        Print.googleInput.output += kwargs['sep'].join(args) if 'sep' in kwargs else ' '.join(args)


Print(sys.stdout)
