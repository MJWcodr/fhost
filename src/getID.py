from random import randbytes
from os import path
rand = randbytes(12).hex()

# checks if folder has an unique identifier, else create one


def getID(filePath):
    __id_file_name = "/.id"
    if (path.exists(filePath + __id_file_name)) and (path.getsize(filePath + __id_file_name) > 0):
        f = open(filePath + __id_file_name, "r")
        __out = f.readlines()[0][-4:]
        f.close()
        return __out
    else:
        f = open(filePath + __id_file_name, "w")
        f.write(rand)
        __out = rand[-4:]
        f.close()
        return __out
