class Invoker(object):
    def __init__(self, ):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def run(self):
        for command in self.commands:
            command['function'](*command["params"])


if __name__ == '__main__':

    def f(string1, string2):
        return print("Writing {} - {}".format(string1, string2))

    invoker = Invoker()
    invoker.add_command({"function": f, "params": ("Command 1", "String 1")})
    invoker.add_command({"function": f, "params": ("Command 2", "String 2")})
    invoker.run()
