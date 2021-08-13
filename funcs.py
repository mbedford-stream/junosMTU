from jnpr.junos import Device
from jnpr.junos.op.phyport import PhyPortTable
from pathlib import Path


def getInts(routerInfo):
    rtr = Device(host=routerInfo["host"],
                 port=routerInfo["port"], user=routerInfo["user"], password=routerInfo["password"])
    try:
        rtr.open()
    except Exception as err:
        print('Error: ' + repr(err))

    intTable = PhyPortTable(rtr)
    try:
        intTable.get()
    except Exception as err:
        print('Error: ' + repr(err))

    return intTable


def readList(listFile):
    returnList = []

    if Path(listFile).is_file() == False:
        return "", "File does not exist"

    try:
        with open(listFile, "r") as f:
            hostLines = f.readlines()
            for l in hostLines:
                returnList.append(l)
            f.close()
            return returnList, ""
    except Exception as err:
        return "", err


if __name__ == "__main__":
    print("funcs.py cannot be run directly")
    quit()
