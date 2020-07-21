# models.py = database initilisation for frambozenapp


import bozen
from bozen.butil import *
from bozen import FormDoc, MonDoc
from bozen import (StrField, ChoiceField, TextAreaField,
    IntField, FloatField, BoolField,
    MultiChoiceField, FK, FKeys,
    DateField, DateTimeField, BzDateTime)

import config
bozen.setDefaultDatabase(config.DB_NAME)
import allpages
bozen.notifyFlaskForAutopages(allpages.app, allpages.jinjaEnv)

import userdb

#---------------------------------------------------------------------

DECADE_BORN_CHOICES = [
    ('1920', "1920s or earlier"),  
    ('1930', "1930s"),  
    ('1940', "1940s"),  
    ('1950', "1950s"),  
    ('1960', "1960s"),  
    ('1970', "1970s"),  
    ('1980', "1980s"),  
    ('1990', "1990s"),  
    ('2000', "2000s"),  
    ('2010', "2010s"),  
    ('2020', "2020s"),
]    

RELIGION_CHOICES = [
    "Baha'i",
    "Buddhism",
    "Christianity - Catholic",  
    "Christianity - Orthodox", 
    "Christianity - Protestant",   
    "Christianity - Other",  
    "Hinduism",   
    "Islam - Sunni",       
    "Islam - Shia",       
    "Judaism",  
    "Shinto",
    "Sikh",
    "Taoism",
    "Atheism", 
    "Agnostic / Non-religious",
    "Other",
]    

class UserDemographics(MonDoc):
    """ demographics of a user """
    
    _id = StrField(desc="User id", title="User Id",
        displayInForm=False,
        required=True, readOnly=True)
    
    decadeBorn = ChoiceField(
        desc="which decade were you born in",
        choices=DECADE_BORN_CHOICES,
        showNull=True, allowNull=False)
    religionBroughtUp = ChoiceField(
        desc="religion you were brought up in",
        choices=RELIGION_CHOICES,
        showNull=True, allowNull=False)
    religionNow = ChoiceField(
        desc="religion you are now",
        choices=RELIGION_CHOICES,
        showNull=True, allowNull=False)
    
    savedAt = DateTimeField(desc="when the data was saved",
        displayInForm=False,
        readOnly=True)
     
    @classmethod
    def classLogo(cls):
        return "<i class='fa fa-male'></i> "
 
def getUserDemographics(userId: str) -> UserDemographics:
    """ get user demographics object, creating it if necessary """
    ai = UserDemographics.getDoc(userId)
    if not ai:
        ai = UserDemographics(_id=userId)
    return ai    

#---------------------------------------------------------------------

class Answer(MonDoc):
    """ an answer by a user to a question """
    
    user_id = FK(userdb.User)
    question_id = StrField(desc="ID of question")
    savedAt = DateTimeField(desc="when the question was answered", 
        readOnly=True)
    ans = StrField(desc="the user's answer to the question") 
 
    @classmethod
    def classLogo(cls):
        return "<i class='fa fa-check-square-o'></i> "
    
    def preSave(self):
        self.savedAt = BzDateTime.now()

Answer.autopages()    

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

