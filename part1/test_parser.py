from parser import Parser
import pprint
import collections


class TestParser(object):

    def compare(self, x, y):
        return collections.Counter(x) == collections.Counter(y)

    p = Parser(['-i', 'test.txt', '-i', 'test2.txt'])
    pp = pprint.PrettyPrinter(indent=2)
    pprint = pp.pprint

    def test_readfiles(self):
        self.p.readfiles()
        assert self.compare(self.p.files, ["test.txt", "test2.txt"])

        # self.pprint(self.p.atupstrfiles)
        # self.pprint(self.p.atupfiles)

    def test_splitwords(self):
        lstr = ['I am the best']
        expect = ['I', 'am', 'the', 'best']
        result = self.p.splitwords(lstr)
        # self.pprint(result[0])
        assert result[0] == expect
        pass

    def test_keepfloat(self):
        result = self.p.keepfloat(['abc', '12', '1.45', '3,99', '-4.12'])
        assert self.compare(result, ['12', '1.45', '-4.12'])

    def test_isfloat(self):
        assert(self.p.isfloat("3"))
        assert(self.p.isfloat("3.23"))
        assert(self.p.isfloat("3,212") is False)
        assert(self.p.isfloat("-3"))
        assert(self.p.isfloat("-3.343"))

    def test_filternumbers(self):
        # Check with filename
        # self.pprint(self.p.filternumbers("test.txt"))
        # self.pprint(self.p.filternumbers("test2.txt"))

        #assert self.p.filternumbers()
        pass

    def test_findstr(self):
        self.pprint(self.p.findstr('test.txt'))
        pass

    def test_mean(self):
        pass

    def test_sum(self):
        pass
