# askquestions.py == ask questions

from flask import request, redirect

from allpages import app, jinjaEnv
from bozen.butil import pr, prn

import quest
import questions

#---------------------------------------------------------------------


@app.route('/askq', methods=['POST', 'GET'])
def askq():
        
    if request.method=='POST':
        pass
    #//if    
    
    tem = jinjaEnv.get_template("askq.html")
    h = tem.render(
        qs = quest.questionListH() # get html-formatted list of questions
    )
    return h

#---------------------------------------------------------------------


#end
