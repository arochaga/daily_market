""" Functions needed """

import urllib
import os

FILE_NAME = "daily.txt"

def download_file(day, month, year):
    """Downloads the correct file according to the date"""

    url = "http://www.omie.es/datosPub/marginalpdbc/marginalpdbc_"\
         + year + month + day + ".1"

    print(url)
    testfile = urllib.URLopener()
    testfile.retrieve(url, FILE_NAME)


def read_prices():
    """Parses the prices of the daily market"""

    print("Hour      " + "Price" + "\n")

    with open(FILE_NAME) as prices_file:
        prices_file.next()
        for line in prices_file:
            if line == "*\r\n":
                continue
            splitted_line = line.split(";")
            #print(splitted_line)
            year, month, day, hour, price, dummy, dummy2 = splitted_line
            print(hour + "    " + price + "\n")

    prices_file.close()
    os.remove(FILE_NAME)


