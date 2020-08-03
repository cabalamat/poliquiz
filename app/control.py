# control.py = control panel


from typing import List, Optional

from flask import request, redirect

from allpages import app, jinjaEnv
from bozen.butil import pr, prn, dpr, printargs, form, htmlEsc

import permission
from permission import needUser, currentUserName
import quest
from quest import Question, questionManager
import models

#---------------------------------------------------------------------

@app.route('/controlPanel')
def controlPanel(): 
    tem = jinjaEnv.get_template("controlPanel.html")
    h = tem.render(
    )
    return h

#---------------------------------------------------------------------


#end
