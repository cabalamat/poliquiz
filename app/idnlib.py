# idnlib.py = library for identity names

"""
Identity Name Library
~~~~~~~~~~~~~~~~~~~~~

Questions, and sections (groups of questions) will each have a string
identifier. We would like this to be based on the texst of the 
question/section but stay the same if there is a small change in this 
text (e.g. fixing a typo) or for if new sections and questions are added.

Alternately we could hand-code the section and question identifiers,
but that's potentially time consuming and error prone
"""

from typing import *

#---------------------------------------------------------------------


FUNCTION_WORDS = """
a about above across after again against
ago ahead all almost along already also although
always am among an and another any anybody
anyone anything are aren't around as at away
back backward backwards be because before behind being
below beneath beside between beyond both but by
can can't cannot cause could couldn't despite did
didn't do does doesn't don't down during each
eight either enough even ever every everybody everyone
everything except few fifteen fifty first five for
forty forward four from had hadn't half has
hasn't have haven't he her here hers herself
him himself his how however hundred i if
in inside inspite instead into is isn't it
its itself just last least less like little
many may mayn't me might mightn't million mine
more most much must mustn't my myself near
nearno need needn't needs neither never next nine
nineteen no nobody none nor not nothing now
of off often on once one only onto
or other ought oughtn't our ours ourselves out
outside over past per perhaps quite rather round
s second seldom seven several shall shan't she
should shouldn't since six so some somebody someone
something sometimes soon still such ten than that
the their theirs them themselves then there therefore
these they third thirty this those though thousand
three through thus till to together too toward
towards twelve twenty two under unless until up
upon us used usedn't usen't usually very was
wasn't we well were weren't what whatever when
where whether which while who whom whose why
will with within without won't would wouldn't yet
you your yours yourself yourselves
br a b c i em
"""

functionWords = set(FUNCTION_WORDS.lower().split())

#---------------------------------------------------------------------

ALLOW_CHARS = ("ABCDEFGHIJKLMNOPQRSTUVWXWY"
               "abcdefghijklmnopqrstuvwxyz"
               "'")

MAX_LEN = 20

def makeId(s: str) -> str:
    """ make an identity-string from a string 
    This looks at the words in the input, 
    removes the function words    
    """
    ws = replaceIrrelevant(s).lower().split()
    ws2 = [w 
           for w in ws 
           if w not in functionWords and len(w)>1]
    abbWs = [abbrev(w) for w in ws2]
    abbrStr = "".join(abbWs)
    abbrStr2 = abbrStr[:MAX_LEN]
    return abbrStr2
    
def replaceIrrelevant(s: str) -> str:
    """ replaces chars not in (ALLOW_CHARS) with a space """
    r = ""
    for ch in s:
        if ch in ALLOW_CHARS:
            r += ch
        else:
            r += " "
    #//for
    return r

def abbrev(s: str) -> str:
    """ build an abbreviation string of a word. This takes the 1st letter
    then the next 2 non-vowel letters """
    if len(s)<1: return ""
    first, rest = s[0], s[1:]
    nonVowels = "".join(ch for ch in rest if ch not in "aeiou")
    return first.upper() + nonVowels[:2].lower()

#---------------------------------------------------------------------

def makeDistinctId(s: str, disallowed: Set[str]) -> str:
    """ make an id from (s) which is not the same as any of the values 
    in (disallowed).
    """
    ids = makeId(s)
    if ids not in disallowed: 
        return ids
    x = 1
    while True:
        candidate = ids + str(x)
        if candidate not in disallowed: return candidate
        x += 1
    #//while    


#---------------------------------------------------------------------




#end
