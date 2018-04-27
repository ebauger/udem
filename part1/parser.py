#!/usr/bin/env python3

import sys
import getopt
import ast


class Parser(object):
    # List of file name
    # look like ['a.txt', 'b.txt', ...]
    files = []

    # Init after readfiles()
    # look like ['sentence 1', 'sentence 2']
    atupstrfiles = []
    # looke like ['sentence', '1'], ['sentence', '2']]
    atupfiles = []

    # linesmatch = []

    def __init__(self, argv):
        """
        Read argv from the standard input and add to self.files list
        """
        msgHelper = 'parser.py -i <file1> [-i file2[, -i fileN]]'
        try:
            opts, args = getopt.getopt(argv, "i:", "--input")
        except getopt.GetoptError:
            print(msgHelper)
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-i':
                self.files.append(arg)

    def readfiles(self):
        """
        Read each files and create a list of each line on atupstrfiles
        and atupfiles attributs of the Parser class
        """
        for file in self.files:
            with open(file, "r") as file:
                lines = file.readlines()  # array for eachline
            self.atupfiles.append((file.name, lines))
            # array of string of each line for the file
            strings = self.splitwords(lines)
            tfilerstr = (file.name, strings)
            self.atupstrfiles.append(tfilerstr)

    def splitwords(self, strline):
        """
        strline = ['s1 s2 s3 sss4']
        Return a list of words with the split function
        => ['s1', 's1', 's3', 'sss4']
        """
        return list(map(lambda x: x.split(), strline))

    def keepfloat(self, strline):
        """
        strline = ['abc', '12', '1.45']
        Return => ['12', '1.45']
        """
        return list(filter(lambda x: self.isfloat(x), strline))

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def filternumbers(self, fname=None, listnumbers=None):
        """
        Filter the numbers of the @fname or the specifice lines and return
        a list of numbers
        """

        listfloat = []
        # case by filename
        if listnumbers is None and fname is not None:
            for filename, content in self.atupstrfiles:
                if filename == fname:
                    for line in content:
                        line = self.keepfloat(line)
                        if line != []:
                            listfloat.append(line)
        # case by specific lines
        elif listnumbers is not None and fname is None:
            listnumbers = self.splitwords(listnumbers)
            for line in listnumbers:
                listfloat.append(self.keepfloat(line))
        else:
            return []  # return empty list
        # clean empty list (now done on line 87)
        listfloat = list(filter(lambda x: not (not x), listfloat))
        # create flat list
        listfloat = list(sum(listfloat, []))
        # convert string list to number list
        listfloat = list(map(lambda x: ast.literal_eval(x), listfloat))
        return listfloat

    def findstr(self, fname=None, lines=None,
                strarray=['/product/', '/produit/', '/catalog'],
                exclude=['#', ';']):
        """Return list of line who respects strarray search patterns and
        excludes patterns at the first element of the line.
        """
        linesfound = []
        if fname is not None and lines is None:
            for filename, content in self.atupfiles:
                if filename == fname:
                    # Filter look like :
                    # True in [y in 'abcde' for y in ['a', 'b', 'c']]
                    #       => True in [True, True, True] => True
                    linesfound.append(
                        list(filter(lambda x:
                                    True in
                                    [(y in x) for y in strarray], content)))

                    # filter exlude symbols
                    linesfound = list(
                        filter(lambda x: not(x[0] in exclude), linesfound[0]))
                    return linesfound
        elif lines is not None and fname is None:
            return linesfound
        return linesfound

    def mean(self, fname=None, lines=None):
        numbers = self.filternumbers(fname, lines)
        if numbers is None or len(numbers) == 0:
            return 0
        else:
            return sum(numbers) / len(numbers)

    def sum(self, fname=None, lines=None):
        numbers = self.filternumbers(fname, lines)
        return sum(numbers)

    def count(self, fname):
        """
        Print words count in each files
        """
        for filename, content in self.atupstrfiles:
            if filename == fname:
                # list of length of each line

                leneachline = list(map(lambda x: len(x), content))
                return sum(leneachline)
        return 0


if __name__ == "__main__":
    p = Parser(sys.argv[1:])
    p.readfiles()

    # loop on each files
    for name in p.files:
        patterns = ['/product/', '/produit/', '/catalog']
        firstwith = ['#', ';']

        print('==== Statistics for {:s} ===='.format(name))
        print('Words count: {:d}'.format(p.count(name)))
        print('Mean: {:f} ; Sum: {:f}'.format(p.mean(name), p.sum(name)))
        specificlines = p.findstr(
            fname=name, strarray=patterns, exclude=firstwith)
        print('Numbers of line {} with patterns: {} exclude lines with: {}'
              .format(len(specificlines), patterns, firstwith))
        print('Mean: {: f}; Sum: {: f} with patterns: {} exclude lines with {}'
              .format(
                  p.mean(lines=specificlines),
                  p.sum(lines=specificlines), patterns, firstwith))
