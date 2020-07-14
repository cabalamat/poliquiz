# demog.py = demographics page


from allpages import app, jinjaEnv
from bozen.butil import pr, prn

import config

prn("*** front.py ***")

#---------------------------------------------------------------------

@app.route('/demographics')
def demographics():
    tem = jinjaEnv.get_template("demographics.html")
    h = tem.render(
    )
    return h


# end


#end
