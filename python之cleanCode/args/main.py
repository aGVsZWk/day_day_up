from args import Args

def main(args):
    try:
        arg = Args(args)
        logging = arg.getBoolean('l')
        port = arg.getInt('p')
        directory = arg.getString('d')
        executeApplication(logging, port, directory)
    except ArgsException as e:
        print('"Argument error: %s\n"', e.errorMessage())
