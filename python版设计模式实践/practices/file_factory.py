import abc
import random


class File(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def former(self):
        return

    @abc.abstractmethod
    def can_be_validate(self):
        return

    @abc.abstractmethod
    def can_be_dump(self):
        return

    @abc.abstractmethod
    def can_be_upload(self):
        return

class CsvFile(File):
    def former(self):
        return "csv"

    def can_be_validate(self):
        return True

    def can_be_dump(self):
        return True

    def can_be_upload(self):
        return True

class TxtFile(File):
    def former(self):
        return "txt"

    def can_be_validate(self):
        return True

    def can_be_dump(self):
        return True

    def can_be_upload(self):
        return True

class ExcelFile(File):
    def former(self):
        return "xlsx"

    def can_be_validate(self):
        return True

    def can_be_dump(self):
        return True

    def can_be_upload(self):
        return True

class Dumper(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def dump(self):
        pass

    @abc.abstractmethod
    def ready(self):
        return


class DictDumper(Dumper):
    def dump(self):
        return 'dump dict'

    def ready(self):
        return True


class TupleDumper(Dumper):
    def dump(self):
        return 'dump tuple'

    def ready(self):
        return True


class Validater(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def validate(self):
        return

    def ready(self):
        return True


class HeaderValidater(Validater):
    def validate(self):
        return "validate header"

    def ready(self):
        return True


class BodyValidater(Validater):
    def validate(self):
        return "validate body"

    def ready(self):
        return True


class Coser(object):
    def upload(self):
        return "upload file"

    def ready(self):
        return True


class Saver(object):
    def __init__(self, file, validater, dumper):
        self._file = file
        self._validater = validater
        self._dumper = dumper

    def can_save_file(self):
        if self._file.can_be_validate() and self._file.can_be_dump() and self._validater.ready() and self._dumper.ready():
            return True
        else:
            return False

class Uploader(object):
    def __init__(self, file, coser):
        self._file = file
        self._coser = coser

    def can_upload_file(self):
        if self._file.can_be_validate() and self._file.can_be_upload() and self.coser.ready():
            return True
        else:
            return False


class Client(object):

    def __init__(self):
        pass

    def save_file(self, saver):
        if saver.can_save_file():
            return "save file"
        else:
            return "can't save file"

    def upload_file(self, uploader):
        if uploader.can_upload_file():
            return "upload file"
        else:
            return "can't upload file"


class Factory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_file(self):
        return

    @abc.abstractmethod
    def create_validater(self):
        return

    @abc.abstractmethod
    def create_dumper(self):
        return

class CsvHeaderValidaterFactory(Factory):
    def create_file(self):
        return CsvFile()

    def create_validater(self):
        return HeaderValidater()

    def create_dumper(self):
        return DictDumper()

class CsvBodyValidaterFactory(Factory):
    def create_file(self):
        return CsvFile()

    def create_validater(self):
        return BodyValidater()

    def create_dumper(self):
        return DictDumper()

class TxtHeaderValidaterFactory(Factory):
    def create_file(self):
        return TxtFile()

    def create_validater(self):
        return HeaderValidater()

    def create_dumper(self):
        return DictDumper()

class TxtBodyValidaterFactory(Factory):
    def create_file(self):
        return TxtFile()

    def create_validater(self):
        return BodyValidater()

    def create_dumper(self):
        return DictDumper()

class ExcelHeaderValidaterFactory(Factory):
    def create_file(self):
        return ExcelFile()

    def create_validater(self):
        return HeaderValidater()

    def create_dumper(self):
        return DictDumper()

class ExcelBodyValidaterFactory(Factory):
    def create_file(self):
        return ExcelFile()

    def create_validater(self):
        return BodyValidater()

    def create_dumper(self):
        return DictDumper()

def get_factory():
    return random.choice([CsvHeaderValidaterFactory, CsvBodyValidaterFactory, TxtHeaderValidaterFactory, TxtBodyValidaterFactory, ExcelHeaderValidaterFactory, ExcelBodyValidaterFactory])()


if __name__ == '__main__':
    factory = get_factory()
    file = factory.create_file()
    validater = factory.create_validater()
    dumer = factory.create_dumper()
    saver = Saver(file, validater, dumper)
    client = Client(saver)
    client.save_file()
