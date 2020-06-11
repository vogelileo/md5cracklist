import itertools
import hashlib
import os
import time
start = time.time()
if os.path.exists("test.txt"):
    os.remove("test.txt")
else:
    print("The file does not exist")



f = open("test.txt", "a+")
count = 0
#string = "abcdefgh"
string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,-_@!$:;"
anzahlstellen = 7
#anzahlstellen = 20

for y in range(6, anzahlstellen + 1):
    for x in itertools.product(string, repeat=y):
        try:
            actuell = ''
            actuell = actuell.join(x)
            result = hashlib.md5(actuell.encode())

            f.write(result.hexdigest() + ":" + actuell + ";")

            if (count%(50000)==0):
                print(str(count) + " " + str(actuell) + " Stellen " + str(len(actuell)) + " von " + str(anzahlstellen))
                if (count%1000000==0):
                    print("Dateigroesse in Byte: " + str(os.path.getsize("test.txt")))

            count = count + 1
            if (count==1000000):
                time.sleep(100)

        except:
            print("Error Occured to String: " + str(count) + " " + actuell)


ende = time.time()
print("Erstellte Strings: " + str(count) + " in " + str(round((ende-start), 2)))

#print([''.join(x) for x in itertools.product('abcABC123', repeat=9)])
