# reviewqa.py = review user's answers by group

from typing import List, Optional

from flask import request, redirect

from allpages import app, jinjaEnv
from bozen.butil import pr, prn, dpr, printargs, form, htmlEsc

import permission
from permission import needUser, currentUserName
import questlib
from questlib import Question, questionManager
import questions
import models

#---------------------------------------------------------------------
# review of questions, from all groups, for current user

@app.route('/review')
@needUser
def review():
    groupTable = calcGroupTable(permission.currentUserName())    
    tem = jinjaEnv.get_template("review.html")
    h = tem.render(
        groupTable = groupTable,
    )
    return h

def calcGroupTable(userName: str) -> str:
    """ caslculate the group table for the current user.
    Returns html.
    """
    h = """<table class='bz-report-table'>
<tr>
    <th>Group</th>
    <th>Questions<br>Answered</th>
    <th>Questions<br>Unanswered</th>
    <th>Details</th>
</tr>    
"""    
    groups = questionManager.getGroups()
    for group in groups:
        dpr("group.id=%r", group.id)
        numQs = len(group.questions)
        numAnswered = len(answeredQs(currentUserName(), group.questions))
        numUnanswered = numQs - numAnswered 
        if numUnanswered==0:
            detailsH= form("View <a href='/results/{groupId}' class='green'>"
                "<i class='fa fa-star'></i> "
                "Your Results</a>", 
                groupId = htmlEsc(group.id))
        else:    
            detailsH = ("<i class='fa fa-lock'></i> "
                "<i>answer all questions to unlock details</i>")
        h += form("""
<tr>
    <td><a href="/group/{groupId}">{groupName}</a></td>
    <td style='text-align:right;'>
        <a href="/answered/{groupId}">{numAnswered}</a></td>
    <td style='text-align:right;'>
        <a href="/ask/{groupId}">{numUnanswered}</a>/{numTotal}</td>
    <td>{details}</td>
</tr>            
""",
            groupId = htmlEsc(group.id),
            numQs = numQs,
            groupName = htmlEsc(group.title),
            numAnswered = numAnswered,
            numUnanswered = numUnanswered,
            numTotal = numQs,
            details = detailsH,
        )
    #//for    
    h += "</table>\n"
    return h

def answeredQs(userId: str, qs: List[Question]) -> List[Question]:
    """ return those questions from (qs) that user (userId)
    has anwered.
    """
    result = []
    for q in qs:
        a = models.Answer.find_one({
            'user_id': userId,
            'question_id': q.qid})
        if a:
            result += [q]
    return result        
        

#---------------------------------------------------------------------
# information about a group

@app.route('/group/<groupId>')
def group(groupId):
    g = questionManager.getGroup(groupId)
    if not g:
        return permission.http403("Group does not exist")
    cun = currentUserName()
    numQs = len(g.questions)
    numAnswered = 0 # number of questions this user has answered
    if cun:
        numAnswered = len(answeredQs(cun, g.questions))
    numUnanswered = numQs - numAnswered
    
    tem = jinjaEnv.get_template("group.html")
    h = tem.render(
        group = g,
        groupId = htmlEsc(g.id),
        groupTitle = htmlEsc(g.title),
        numQs = numQs,
        numAnswered = numAnswered,
        numUnanswered = numUnanswered,
    )
    return h

#---------------------------------------------------------------------
# questions the current user has answered in a group

@app.route('/answered/<groupId>')
@needUser
def answered(groupId):
    group = questionManager.getGroup(groupId)
    if not group:
        return permission.http403("Group does not exist")
    cun = currentUserName()
    ansQs = answeredQs(cun, group.questions)
    numQs = len(group.questions)
    numAns = len(ansQs)
    ansH = calcAnsH(cun, ansQs)
    
    tem = jinjaEnv.get_template("answered.html")
    h = tem.render(
        group = group,
        groupId = htmlEsc(group.id),
        groupTitle = htmlEsc(group.title),
        numQs = numQs,
        numAns = numAns,
        ansH = calcAnsH(cun, ansQs),
    )
    return h

@printargs
def calcAnsH(userId: str, qs: List[Question]) -> str:
    """ Return an html-encoded string containing user (userId)'s
    answers to the questions in (qs).
    """
    h = ""
    for q in qs:
        a = models.Answer.find_one({
            'user_id': userId,
            'question_id': q.qid})
        if not a: continue
        h += q.answerH(a.ans)
        
    #//for q    
    return h

#---------------------------------------------------------------------

#end
