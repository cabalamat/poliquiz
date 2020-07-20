# reviewqa.py = review user's answers by group

from flask import request, redirect

from allpages import app, jinjaEnv
from bozen.butil import pr, prn

import quest
import questions

#---------------------------------------------------------------------


@app.route('/review')
def review():
    tem = jinjaEnv.get_template("review.html")
    h = tem.render(
    )
    return h

#---------------------------------------------------------------------

#end
