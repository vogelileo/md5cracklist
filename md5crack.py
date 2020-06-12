import itertools
import hashlib
import os
import time
start = time.time()
target = input("Your String: ")

#string = "abcdefgh"
string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,-_@!$:;"
anzahlstellen = 20

def crack():
    count = 0
    for y in range(0, anzahlstellen + 1):
        for x in itertools.product(string, repeat=y):
            try:
                actuell = ''
                actuell = actuell.join(x)
                result = hashlib.md5(actuell.encode())

                if(target == result.hexdigest()):
                    print("From " + target + " zu " + actuell)
                    return actuell
                if (count % (50000) == 0):
                        print(str(count) + " " + str(actuell) + " Stellen " +
                            str(len(actuell)) + " von " + str(anzahlstellen))
                count = count + 1


            except:
                print("Error Occured to String: " + str(count) + " " + actuell)

crack()
ende = time.time()


#print([''.join(x) for x in itertools.product('abcABC123', repeat=9)])
