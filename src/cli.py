from os import path
import sys
import re

options = sys.argv[1:]


def fixPath(filepath):
    print(filepath)
    if isCommandOption("h", "help"):

        return None
    if path.isdir(filepath):
        if (filepath[-1] == "/"):
            return filepath[:-1]
        else:
            return filepath
    else:
        return filepath


def isCommandOption(shortCode, longCode=None):
    if (len(sys.argv) > 1):
        __options = str(options)
        __regex = f"'-([a-z]*){shortCode}"
        if re.search(__regex, __options):
            return True
        elif (longCode):
            if (longCode in __options):
                return True
            else:
                return False
    else:
        return False


def getInstructions():
    __out__ = []
    if (isCommandOption("h", "help")):
        __out__ = __out__ + ["help"]
    if (isCommandOption("y")):
        __out__ = __out__ + ["yes"]
    if (isCommandOption("l", "links")):
        __out__ = __out__ + ["links"]
    if (isCommandOption("s", "shorten")):
        __out__ = __out__ + ["shorten"]
    return __out__


class cli:
    if (len(sys.argv) <= 1):
        print("must give atleast one argument")
        quit()
    file = fixPath(sys.argv[-1])
    instructions = getInstructions() if getInstructions() else []
