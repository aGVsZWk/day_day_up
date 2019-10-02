class MacroCommand:
    def __init__(self, commands):
        self.commands = commands

    def __call(self):
        for command in self.commands:
            command()
