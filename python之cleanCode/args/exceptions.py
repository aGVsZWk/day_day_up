from typing import List, Dict, Set, String
from enum import Enum


ErrorCode = Enum('ErrorCode', 'OK INVALID_ARGUMENT_FORMAT UNEXPECTED_ARGUMENT \
                INVALID_ARGUMENT_NAME MISSING_STRING MISSING_INTEGER INVALID_INTEGER \
                MISSING_DOUBLE INVALID_DOUBLE')
# dir(ErrorCode)
# ErrorCode.__dict__

class ArgsException(Exception):
    errorArgumentId = '\0'
    errorParamter: str = ''
    errorCode: ErrorCode = ErrorCode.OK

    def __init__(self, message: String, errorCode: ErrorCode, errorParameter: String, errorArgumentId: String):
        if message:
            super().__init__(message)
        elif errorCode and errorParameter:
            self.errorCode = errorCode
            self.errorParamter = errorParameter
        elif errorCode and errorArgumentId and errorParameter:
            self.errorCode = errorCode
            self.errorParamter = errorParamter
            self.errorArgumentId = errorArgumentId

    def getErrorArgumentId(self) -> None:
        return errorArgumentId

    def setErrorArgumentId(self, errorArgumentId: String) -> None:
        self.errorArgumentId = errorArgumentId

    def getErrorParameter(self) -> None:
        return errorParamter

    def setErrorParameter(self, ErrorParameter: String) -> None:
        self.errorParamter = ErrorParameter

    def getErrorCode(self):
        return self.errorCode

    def setErrorCode(self, errorCode: ErrorCode):
        self.errorCode = errorCode

    def errorMessage(self) -> String:
        if self.errorCode == ErrorCode.OK:
            return "TILT: Should not get here.";
        elif self.errorCode == ErrorCode.INVALID_ARGUMENT_FORMAT:
            return "Could not find string parameter for -%s." % self.errorArgumentId
        elif self.errorCode == ErrorCode.MISSING_STRING:
            return "Could not find string parameter for -%s." % self.errorArgumentId
        elif self.errorCode == ErrorCode.INVALID_INTEGER:
            return "Argument -%s expects an integer but was '%s'." % (self.errorArgumentId, self.errorParameter)
        elif self.errorCode == ErrorCode.MISSING_INTEGER:
            return "Could not find integer parameter for -%s." % self.errorArgumentId
        elif self.errorCode == ErrorCode.INVALID_DOUBLE:
            return "Argument -%s expects a double but was '%s'." % (self.errorArgumentId, self.errorParameter)
        elif self.errorCode == ErrorCode.MISSING_DOUBLE:
            return "Could not find double parameter for -%s." % self.errorArgumentId
        elif self.errorCode == ErrorCode.INVALID_ARGUMENT_NAME:
            return "'%c' is not a valid argument name." % self.errorArgumentId
        elif self.errorCode == ErrorCode.INVALID_ARGUMENT_FORMAT:
            return "'%s' is not a valid argument format." % self.errorParameter
        else:
            return ""
