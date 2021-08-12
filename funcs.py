from jnpr.junos import Device
from jnpr.junos.op.phyport import PhyPortTable


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


if __name__ == "__main__":
    print("funcs.py cannot be run directly")
    quit()
