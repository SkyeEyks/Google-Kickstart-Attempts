import sys
import typing


class GoogleInput:
    def __init__(self, input_dir: str, outputs_dir: str, function: typing.Callable):
        self._in = sys.stdin.readline
        self._out = sys.stdout.write

        sys.stdout.write = self._write
        sys.stdin.readline = self._read

        self.i = -1
        with open(input_dir, 'r') as f:
            self.inputs = f.read().split('\n')
        self.output = ''
        self.ans = None
        if outputs_dir:
            with open(outputs_dir, 'r') as f:
                self.ans = f.read()

        function()

        self.checkOutput()

        sys.stdin.readline = self._in
        sys.stdout.write = self._out

    def reset(self):
        self.i = -1

    def checkOutput(self):
        if self.output == self.ans+"\n":
            self._out('Your output is correct! :)\n')
        else:
            self._out('Your output isn\'t correct :(\n')

    def _write(self, *args, sep: str = ' ', flush: bool = False):
        self._out(sep.join(str(_) for _ in args))
        self.output += sep.join(str(_) for _ in args)
        if flush: sys.stdout.flush()

    def _read(self):
        self.i += 1
        return self.inputs[self.i]
