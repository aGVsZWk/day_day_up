from typing import List, Dict, Set
from marshaler import ArgumentMarshaler
from exceptions import ArgsException


class Args(object):
    marshalers: Dict[str, ArgumentMarshaler] = {}
    argsFound: Set[str] = set()
    # currentArgument: List[str] = []

    def __init__(self, schema: str, args: List[str]) -> None:
        try:
            self.marshalers: Dict[str, ArgumentMarshaler] = {}
            self.argsFound: Set[str] = set()
            # self.currentArgument = []
            self.parseSchema(schema)
            self.parseArgumentStrings(args)
        except:
            raise ArgsException()

    def parseSchema(self, schema: str) -> None:
        try:
            for element in schema.split(','):
                if len(element) > 0:
                    self.parseSchemaElement(element.strip())
        except:
            raise ArgsException()
            
