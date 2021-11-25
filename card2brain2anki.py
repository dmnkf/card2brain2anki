#!/usr/bin/python3

import csv
import pdftotext
import os
import sys


def main(path):
    with open(path, "rb") as f:
        pdf = pdftotext.PDF(f)

    # Iterate over all the pages
    csv_array = []
    front = True
    for page in pdf:
        page = page.replace("© AKAD", "")
        if front:
            csv_array.append([page])
            front = False
        else:
            csv_array[-1].append(page)
            front = True

    print(csv_array)
    print(len(csv_array))

    with open(f'{path}.csv', 'w') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerows(csv_array)


if __name__ == '__main__':
    fn = sys.argv[1]
    if os.path.exists(fn):
        main(fn)

