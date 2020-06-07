import sys


EX_OK = 0
EX_FAILURE = 1
EX_UNAVAILABLE = 69
EX_USAGE = 64
EX_CANTCREAT = 73


class Error(Exception):
    """Exception raised by commands."""

    status = EX_FAILURE

    def __init__(self, reason, status=None):
        self.reason = reason
        self.status = status
        super(Error, self).__init__(reason, status)

    def __str__(self):
        return self.reason


class UsageError(Error):
    """Exception raised for malformed arguments."""

    status = EX_USAGE


class Command(object):
    """Base class for command-line applications.

    Arguments:
        app (Celery): The app to use.
        get_app (Callable): Fucntion returning the current app
            when no app provided.
    """
    Error = Error
    UsageError = UsageError

    def __init__(self, stdout=None, stderr=None, on_error=None, on_usage_error=None):
        self.stdout = stdout or sys.stdout
        self.stderr = stderr or sys.stderr
        if on_error:
            self.on_error = on_error
        if on_usage_error:
            self.on_usage_error = on_usage_error

    def run(self, *args, **options):
        raise NotImplementedError('subclass responseibility')

    def out(self, s, fh=None):
        print(s, file=fh or self.stdout)

    def error(self, s):
        self.out(s, fh=self.stderr)

    def die(self, msg, status=EX_FAILURE):
        self.error(msg)
        sys.exit(status)

    def on_error(self, exc):
        self.error(exc)

    def on_usage_error(self, exc):
        self.handle_error(exc)

    def __call__(self, *args, **kwargs):
        try:
            self.run(*args, **kwargs)
        except self.UsageError as exc:
            self.on_usage_error(exc)
            return exc.status
        except self.Error as exc:
            self.on_error(exc)
            return exc.status

    def run_from_argv(self, prog_name, argv=None, command=None):
        print(sys.argv)
        return self.handle_argv(prog_name, sys.argv if argv is None else argv, command)

    def handle_argv(self, prog_name, argv, command=None):
        args = ()
        options = {}
        return self(*args, **options)



class multi(Command):
    """Start multiple worker instances."""
    def run_from_argv(self, prog_name, argv, command=None):
        pass     # todo


class help(Command):
    def run(self, *args, **kwargs):
        self.out('aaa')
        pass    # todo
        return EX_USAGE


class report(Command):


    def __init__(self, *args, **kwargs):
        super(report, self).__init__(*args, **kwargs)
        pass    # todo

    def run(self, *args, **kwargs):
        self.out('bbb')
        return EX_OK


class CeleryCommand(Command):
    commands = {
        # "worker": worker  # todo
    }
    prog_name = 'celery'

    @classmethod
    def register_command(cls, fun, name=None):
        cls.commands[name or fun.__name__] = fun    # so important
        return fun

    def execute(self, commmand, argv=None):     # so familiar
        try:
            cls = self.commands[commmand]
        except KeyError:
            cls, argv = self.commands['help'], ['help']
        try:
            return cls().run_from_argv(self.prog_name, argv[1:], commmand=argv[0])  # so import cls()
        except self.UsageError as exc:
            self.on_usage_error(exc)
            return exc.status
        except self.Error as exc:
            self.on_error(exc)
            return exc.status





c = report(on_error=lambda x: print("----{}".format(x)))
c.out('你好')
c.error('我是错误')
c.on_error('aaa')
c.run_from_argv('abc')
c()
c.die('I am die')   # sys.exit 以后的代码会不在执行
