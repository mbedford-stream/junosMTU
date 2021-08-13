from funcs import getInts, readList
import getpass
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", help="File containing list of hosts to check", default="hosts.txt")
    args = parser.parse_args()

    print(args)

    hostList, err = readList(args.f)
    if err != "":
        print("Error opening file:")
        print(err)

    configsDir = "configs/"
    devUser = input("Username: ")
    devPass = getpass.getpass()

    for h in hostList:
        print("\n\nChecking interfaces on %s\n=================================\n" % h)
        intsList = getInts({"host": h.rstrip("\n"), "port": 830, "user": devUser,
                            "password": devPass})

        updateInts = []

        for i in intsList:

            if int(i.mtu) <= 6000:
                print("%s\n%s Current MTU: %d\n" %
                      (i.description, i.name, i.mtu))

                updateInts.append(i.name)

            else:
                print("%s\n%s Current MTU OK: %d\n" %
                      (i.description, i.name, i.mtu))

        try:
            changeHost = h.replace(".", "_").rstrip("\n")
            with open(configsDir+changeHost+".set", "w") as fileOut:
                for u in updateInts:
                    writeLine = "set interfaces %s mtu 9192\n" % u
                    print(writeLine)
                    fileOut.write(writeLine)
                fileOut.close()
        except Exception as err:
            print(err)
