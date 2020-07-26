# test_idnlib.py = tests idnlib.py


from bozen.butil import *
from bozen import lintest

from idnlib import *

#---------------------------------------------------------------------

class T_makeId(lintest.TestCase):
    """ test the makeId function, and the functions it calls """
    
    def test_abbrev(self):
        r = abbrev("help")
        self.assertSame(r, "Hlp", "removed the 'e'")
        r = abbrev("abcdefghi")
        self.assertSame(r, "Abc")
        r = abbrev("heeeeeeeeeeeeeeq")
        self.assertSame(r, "Hq")
        
    def test_replaceIrrelevant(self):
        r = replaceIrrelevant("help")
        self.assertSame(r, "help",)
        r = replaceIrrelevant("12th night, abc-def")
        self.assertSame(r, "  th night  abc def",)
        
    def test_makeId(self):    
        t = " the 2nd largest place "
        r = makeId(t)
        sb = "NdLrgPlc"
        self.assertSame(r, sb)
        
        r = makeId("The Myers-Briggs test!")
        sb = "MyrBrgTst"
        self.assertSame(r, sb)
        
        r = makeId("England should leave the UK and be an independent country")
        sb = "EngLvUkIndCnt"
        self.assertSame(r, sb)
        

#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_makeId)

if __name__=='__main__': group.run()


#end


