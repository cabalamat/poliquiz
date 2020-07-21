# quest.py = code for processing questions

from typing import List, Optional

from bozen.butil import dpr, htmlEsc, form

#---------------------------------------------------------------------

class Question:
    def askH(self)->str: 
        h = form("""
<p class='question'><i class='fa fa-question-circle-o'></i>
{qtext}</p>""",
           qtext = htmlEsc(self.qtext))
        return h

class MultiChoiceQuestion(Question):
    def __init__(self, qid: str, qtext: str, answers: List[str]):
        self.qid = qid
        self.qtext = qtext
        self.answers = answers
        
    def askH(self)->str: 
        h = super().askH()
        for ans in self.answers:
            h += form("""\
&nbsp; <input type=radio id="{qid}" name="{qid}" value="">
<span class='answer'>    
    <span class='answer-mc'>
    <i class='fa fa-dot-circle-o'></i>
    {ans}</span>
</span><br>             
""",          
                qid = self.qid,
                ans = htmlEsc(ans))
        #//for ans
        h += form("""\
&nbsp; <input type=radio id="{qid}" name="{qid}" value="">
<span class='answer">   
    <span class='answer-mc'>
    <i class='fa fa-dot-circle-o'></i>
    {ans}</span>
</span><br>
""",          
            qid = self.qid,
            ans = htmlEsc("Don't know / other"))
        return h
        

#---------------------------------------------------------------------

AD_ANS = [ # class, text, value
   ("answer-agree", "Strongly agree", "2"), 
   ("answer-agree", "Agree", "1"), 
   ("answer-neutral", "Neutral", "0"), 
   ("answer-disagree", "Disagree", "-1"), 
   ("answer-disagree", "Strongly disagree", "-2"),  
   ("answer-dk", "Don't know / other", "DK"),    
]    

class AgreeDisagreeQuestion(Question):
    def __init__(self, qid: str, qtext: str):
        self.qid = qid
        self.qtext = qtext
      
    def askH(self)->str: 
        h = super().askH()
        for ansClass, ansText, ansVal in AD_ANS:
            h += form("""\
&nbsp;&nbsp; <input type=radio id="{qid}" name="{qid}" value="{ansVal}">
<span class='answer">        
    <span class='{ansClass}'>
    <i class='fa fa-dot-circle-o'></i>
    {ansText}</span>
</span><br>
""",          
                qid = self.qid,
                ansClass = htmlEsc(ansClass),
                ansVal = htmlEsc(ansVal),
                ansText = htmlEsc(ansText))
        #//for ans
        return h  

#---------------------------------------------------------------------

class Group:
    """ a group of questions """
    
    id: str = ""
    title: str = ""
    questions: List[Question] = []
    
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.questions = []
    
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
    
    def getGroup(self, groupId: str) -> Optional[Group]:
        """ return the group whose id is (groupId) """
        for g in self.groups:
            if g.id == groupId: return g
        return None
        
    def addQuestion(self, q):
        self.questions += [q]
        self.groups[-1].questions += [q]
    
questionManager = QuestionManager()    

#---------------------------------------------------------------------

def questionListH():
    """ ask the questionms in the question list, as HTML """
    h = ""
    for q in questionManager.questions:
        h += q.askH() + "\n"
    return h    

def qid()->str:
    """ return an identity string for the next question """
    ids = form("Q{}", len(questionManager.questions))
    return ids

def group(gId:str, gTitle: str):
    """ set a group of questions """
    g = Group(gId, gTitle)
    questionManager.setCurrentGroup(g)


#---------------------------------------------------------------------

def mcq(qtext: str, answers: List[str]):
    global qList
    q = MultiChoiceQuestion(qid(), qtext, answers)
    questionManager.addQuestion(q)

def adq(qtext: str):
    global qList
    q = AgreeDisagreeQuestion(qid(), qtext)
    questionManager.addQuestion(q)


#end
