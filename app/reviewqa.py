# reviewqa.py = review user's answers by group

from flask import request, redirect

from allpages import app, jinjaEnv
from bozen.butil import pr, prn, form, htmlEsc

import permission
from permission import needUser
import quest
from quest import questionManager
import questions

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
    <th>Answered</th>
    <th>Unanswered</th>
    <th>Details</th>
</tr>    
"""    
    groups = questionManager.getGroups()
    for group in groups:
        h += form("""
<tr>
    <td><a href="/group/{groupId}">{groupName}</a></td>
    <td>{numAnswered}</td>
    <td><a href="ask/{groupId}">{numUnanswered}</a>/{numTotal}</td>
    <td>(details)</td>
</tr>            
""",
            groupId = htmlEsc(group.id),
            groupName = htmlEsc(group.title),
            numAnswered = 0,
            numUnanswered = len(group.questions),
            numTotal = len(group.questions),
        )
    #//for    
    h += "</table>\n"
    return h


#---------------------------------------------------------------------

#end
