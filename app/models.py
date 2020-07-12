# models.py = database initilisation for frambozenapp


import bozen
from bozen.butil import *
from bozen import FormDoc, MonDoc
from bozen import (StrField, ChoiceField, TextAreaField,
    IntField, FloatField, BoolField,
    MultiChoiceField, FK, FKeys,
    DateField, DateTimeField)

import config
bozen.setDefaultDatabase(config.DB_NAME)
import allpages
bozen.notifyFlaskForAutopages(allpages.app, allpages.jinjaEnv)

#---------------------------------------------------------------------


#---------------------------------------------------------------------
# admin site

def createAdminSite():
    """ create admin site """
    adminSite = bozen.AdminSite(stub=config.ADMIN_SITE_PREFIX)
    adminSite.runFlask(allpages.app, allpages.jinjaEnv)

if config.CREATE_ADMIN_SITE:
    createAdminSite()

#---------------------------------------------------------------------


#end

