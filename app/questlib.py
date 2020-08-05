# questlib.py = code for processing questions

from typing import List, Optional, Union, Tuple, Set
from abc import abstractmethod

import markdown

from bozen.butil import dpr, htmlEsc, form

import idnlib

#---------------------------------------------------------------------

def md(s: str) -> str:
    """ convert a string from markdown to HTML """
    h = markdown.markdown(s.strip())
    return h

#---------------------------------------------------------------------
# html for questions

def answerChoiceRB(qid:str, 
        ansClass:str, ansVal: str, ansText: str) -> str:
    """ return html for a radio button for an answer to a question.
    qid = question ID
    ansClass = CSS class for this answer
    ansVal = value for answer in the database
    ansText = value for answer to be displayed
    """
    h = form("""\
&nbsp; <input type=radio id="{qid}" name="{qid}" value="{ansVal}">
<span class='answer {ansClass}'>
    <tt>[{ansVal}]</tt> {ans}
</span><br>             
""",         
        qid = htmlEsc(qid),
        ansClass = ansClass,
        ansVal = htmlEsc(ansVal),
        ans = htmlEsc(ansText)
    )
    return h

#---------------------------------------------------------------------

class Question:
    def askH(self) -> str: 
        """ return the question as html """
        h = form("""
<p class='question'><i class='fa fa-question-circle-o'></i>
<tt>[{qid}]</tt> {qtext}</p>""",
            qid = htmlEsc(self.qid),
            qtext = htmlEsc(self.qtext))
        return h
    
    def answerH(self, ans) -> str:
        """ return the querstion as html with the answer selected
        in (ans). 
        """
        userAnswerText = self.answerText(ans)
        h = form("""
<p class='question'><i class='fa fa-question-circle-o'></i>
<tt>[{qid}]</tt> {qtext}</p>
<tt>[{ansVal}]</tt> {ansText}
<br>
""",
            qid = htmlEsc(self.qid),
            qtext = htmlEsc(self.qtext),
            ansVal = htmlEsc(ans),
            ansText = htmlEsc(userAnswerText)
        )
        return h
    
    @abstractmethod
    def userAnswerText(self, ans: str) -> str:
        pass


MultiChoiceAnswer=Union[Tuple[str,str],str]
MultiChoiceAnswers = List[MultiChoiceAnswer]
NormalizedMCAnswers = List[Tuple[str,str]]

def strNVal(i: int) -> str:
    """ convert numbers to strings to get 'A', 'B', 'C'...Z..Z001 etc """
    if i >=0 and i<= 25:
        return chr(ord('A')+i)
    else:
        return "Z%03d"%(i,)

def normalizeMCA(answers: MultiChoiceAnswers) -> NormalizedMCAnswers:
    result = []
    nextVal = 0
    for answer in answers:
        if isinstance(answer,tuple):
            result += [answer]
        else:
            result += [(strNVal(nextVal), answer)]
            nextVal += 1
    #//for    
    return result

class MultiChoiceQuestion(Question):
    def __init__(self, qid: str, qtext: str, answers: List[str]):
        """ (answers) is of the form:
            [ ('A', "Answer 1"),
              ('B', "Answer 2")]
        
        with the internal value preceding the display string. If the
        tuple is replaced by a str, the internal values become 'A', 'B', etc        
        """
        self.qid = qid
        self.qtext = qtext
        self.answers = normalizeMCA(answers)

        
    def askH(self)->str: 
        h = super().askH()
        for ansVal, ansText in self.answers:
            h += answerChoiceRB(self.qid, "answer-mc", ansVal, ansText)
        #//for ans
        
        dk = "Don't know / other"
        h += answerChoiceRB(self.qid, "answer-dk", "--", "Don't know / other")
        return h
    
    def answerText(self, ans):
        r = "???"
        for ansVal, ansText in self.answers:
            if ansVal==ans: r = ansText
        #//for    
        return r
        

#---------------------------------------------------------------------

AD_ANS = [ # class, value, text,
   ("answer-agree",    "2",  "Strongly agree"), 
   ("answer-agree",    "1",  "Agree"), 
   ("answer-neutral",  "0",  "Neutral"), 
   ("answer-disagree", "-1", "Disagree"), 
   ("answer-disagree", "-2", "Strongly disagree"),  
   ("answer-dk",       "--", "Don't know / other"),    
]    

class AgreeDisagreeQuestion(Question):
    def __init__(self, qid: str, qtext: str):
        self.qid = qid
        self.qtext = qtext
      
    def askH(self)->str: 
        h = super().askH()
        for ansClass, ansVal, ansText in AD_ANS:
            h += answerChoiceRB(self.qid, ansClass, ansVal, ansText)
        #//for ans
        return h  
    
    def answerText(self, ans):
        r = ""
        for ansClass, ansVal, ansText in AD_ANS:
            if ansVal==ans: r = ansText
        #//for    
        return r

#---------------------------------------------------------------------

class Group:
    """ a group of questions """
    
    id: str = ""
    title: str = ""
    introH = ""
    questions: List[Question] = []
    
    def __init__(self, id, title, intro):
        self.id = id
        self.title = title
        self.questions = []
        self.introH = md(intro)
        
    def questionIds(self) -> Set[str]:
        """ return the ids of all the questions in this group """
        return set(q.qid for q in self.questions)
    
#---------------------------------------------------------------------

class QuestionManager:
    """ handles groups of questions """
    
    questions: List[Question] = []
    groups: List[Group] = []
    
    def __init__(self):
        self.questions = []
        self.groups = []
    
    def setCurrentGroup(self, g: Group):
        self.groups += [g]
        
    def getGroups(self) -> List[Group]:
        """ return all the groups this QuestionManager has """
        return self.groups
    
    def groupIds(self) -> Set[str]:
        """ return the ids of all the QuestionManager's groups """
        return set(g.id for g in self.groups)
    
    def getGroup(self, groupId: str) -> Optional[Group]:
        """ return the group whose id is (groupId) """
        for g in self.groups:
            if g.id == groupId: return g
        return None
    
    def xxxgetCurrentGroup(self) -> Optional[Group]:
        """ return the current group, or None if there isn't one """
        if len(self.groups) < 1: return None
        g = self.groups[-1]
        return g
    
    def getCurrentGroupId(self) -> str:
        """ return the id of the current group """
        if len(self.groups) < 1: return ""
        g = self.groups[-1]
        return g.id
        
    def addQuestion(self, q):
        self.questions += [q]
        group = self.groups[-1]
        if not q.qid:
            q.qid = "%s-%s" % (
                self.getCurrentGroupId(),
                idnlib.makeDistinctId(q.qtext, group.questionIds()))
        group.questions += [q] 
        
questionManager = QuestionManager()    

#---------------------------------------------------------------------

def questionListH():
    """ ask the questionms in the question list, as HTML """
    h = ""
    for q in questionManager.questions:
        h += q.askH() + "\n"
    return h    

#---------------------------------------------------------------------

MultiChoiceAnswer=Union[Tuple[str,str],str]
MultiChoiceAnswers = List[MultiChoiceAnswer]

def group(gTitle: str, intro: str=""):
    """ Create a group of questions. 
    (gTitle) is the title of the group.
    (intro) is a markdown-encoded introduction to the group.
    """
    gid = idnlib.makeDistinctId(gTitle, questionManager.groupIds())
    g = Group(gid, gTitle, intro)
    questionManager.setCurrentGroup(g)

def mcq(qtext: str, answers: MultiChoiceAnswers, id: str=""):
    global qList
    if id:
        dpr("id=%r", id)
        id = questionManager.getCurrentGroupId() + "-" + id
        dpr("id=%r", id)
    q = MultiChoiceQuestion(id, qtext, answers)
    questionManager.addQuestion(q)

def adq(qtext: str, id: str=""):
    global qList
    if id:
        dpr("id=%r", id)
        id = questionManager.getCurrentGroupId() + "-" + id
        dpr("id=%r", id)
    q = AgreeDisagreeQuestion(id, qtext)
    questionManager.addQuestion(q)






#end
