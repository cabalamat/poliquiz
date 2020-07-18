# demog.py = demographics page


from allpages import app, jinjaEnv
from bozen.butil import pr, prn

import config
import models
from permission import needUser

prn("*** front.py ***")

#---------------------------------------------------------------------

@app.route('/demographics', methods=['POST', 'GET'])
@needUser
def demographics():
    ud = models.getUserDemographics("")
    
    tem = jinjaEnv.get_template("demographics.html")
    h = tem.render(
        ud = ud,
    )
    return h


# end


#end
