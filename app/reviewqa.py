# reviewqa.py = review user's answers by group

from typing import List, Optional

from flask import request, redirect

from allpages import app, jinjaEnv
from bozen.butil import pr, prn, dpr, form, htmlEsc

import permission
from permission import needUser, currentUserName
import quest
from quest import Question, questionManager
import questions
import models

#---------------------------------------------------------------------


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
        h += form("""
<tr>
    <td><a href="/group/{groupId}">{groupName}</a></td>
    <td style='re'>{numAnswered}</td>
    <td><a href="/ask/{groupId}">{numUnanswered}</a>/{numTotal}</td>
    <td>(details)</td>
</tr>            
""",
            groupId = htmlEsc(group.id),
            numQs = numQs,
            groupName = htmlEsc(group.title),
            numAnswered = numAnswered,
            numUnanswered = numUnanswered,
            numTotal = numQs,
            
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
            'question_id': q. qid})
        if a:
            result += [a]
    return result        
        


#---------------------------------------------------------------------

#end
