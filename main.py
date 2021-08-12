from funcs import getInts

if __name__ == "__main__":

    hosts = ["172.31.0.1", "172.31.0.2"]

    for h in hosts:
        print("\n\nChecking interfaces on %s\n=================================\n" % h)
        intsList = getInts({"host": h, "port": 830, "user": "mark",
                            "password": "password123"})

        updateInts = []

        for i in intsList:

            if int(i.mtu) <= 6000:
                print("%s\n%s Current MTU: %d\n" %
                      (i.description, i.name, i.mtu))

                updateInts.append(i.name)

            else:
                print("%s\n%s Current MTU OK: %d\n" %
                      (i.description, i.name, i.mtu))

        for u in updateInts:
            print("set interfaces %s mtu 9192" % u)
