# demog.py = demographics page

from flask import request, redirect

from allpages import app, jinjaEnv
from bozen.butil import pr, prn

import ht
import config
import models
from permission import needUser, currentUserName

prn("*** front.py ***")

#---------------------------------------------------------------------

@app.route('/demographics', methods=['POST', 'GET'])
@needUser
def demographics():
    ud = models.getUserDemographics(currentUserName())
    msg = ""
        
    if request.method=='POST':
        ud = ud.populateFromRequest(request)
        if ud.isValid():
            ud.save()
            msg = "Saved user demographics"
    #//if    
    
    tem = jinjaEnv.get_template("demographics.html")
    h = tem.render(
        ud = ud,
        msg = ht.goodMessageBox(msg),
    )
    return h


# end


#end
