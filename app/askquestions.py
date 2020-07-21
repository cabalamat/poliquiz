# askquestions.py == ask questions

from typing import List, Set, Optional

from flask import request, redirect

from allpages import app, jinjaEnv
from bozen.butil import pr, prn, dpr, form, htmlEsc

from permission import *
import quest
from quest import *
import questions
import models

#---------------------------------------------------------------------

@app.route('/askq', methods=['POST', 'GET'])
def askq():
    dpr("in askq()")
    if request.method=='POST':
        pass
    #//if    
    
    tem = jinjaEnv.get_template("askq.html")
    h = tem.render(
        qs = quest.questionListH() # get html-formatted list of questions
    )
    return h

#---------------------------------------------------------------------

@app.route('/ask/<groupId>', methods=['POST', 'GET'])
@app.route('/ask/<groupId>/<numQs>', methods=['POST', 'GET'])
@needUser
def ask(groupId, numQs=5):
    dpr("groupId={}, numQs={}", groupId, numQs)
    group = questionManager.getGroup(groupId)
    if not group:
        return http403("Group does not exist")
    
    unansweredQs = getUnansweredQs(group, currentUserName())
    qListH = getQuestionsH(unansweredQs)
    numAns = len(group.questions) - len(unansweredQs)
    
    tem = jinjaEnv.get_template("ask.html")
    h = tem.render(
        group = group,
        groupTitle = htmlEsc(group.title),
        groupId = htmlEsc(group.id),
        numQ = len(group.questions),
        numAns = numAns,
        qs = qListH,
    )
    return h

def getUnansweredQs(g: Group, cun: str) -> List[Question]:
    """ Get a list of the questions (in (g) that the current user (cun)
    hasn't answered.
    The questions are returned in the same order that they are in (g).
    """
    questionIds = [q.qid for q in g.questions]
    answeredQuestionIds: Set[str] = set()
    answers = models.Answer.find({
        'user_id': cun, 
        'question_id': {'$in': questionIds}})
    for a in answers:
        answeredQuestionIds.add(a.question_id)
    unansweredQuestionIds = set(questionIds) - answeredQuestionIds   
    unansweredQs = [q 
                    for q in g.questions 
                    if q.qid in unansweredQuestionIds]
    return unansweredQs

def getQuestionsH(qs: List[Question]) -> str:
    """ return html containing the questions as part of a form """
    h = ""
    for q in qs:
        h += q.askH() + "\n"
    return h    

#---------------------------------------------------------------------


#end
