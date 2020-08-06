# g_myrbrg.py = stuff for Myers-Briggs

from typing import Optional, Union

import questlib

import models

#---------------------------------------------------------------------

class MyersBriggs(questlib.Group):

    @classmethod
    def groupId(cls) -> str:
        """ return this group's id """
        return "MyrBrg"
    
    @classmethod
    def fullQid(cls, shortQid: str) -> str:
        return self.groupId + "-" + shortQid
    
    def answerExists(self, userId: str, qid: str) -> bool:
        """ has (userid) answered question (qid)? """
        an = models.Answer.find_one({
            'user_id': userId,
            'question_id': qid})
        return bool(an)
                                     
    def getAnswer(self, userId: str, qid: str) -> Optional[models.Answer]:
        """ has (userid) answered question (qid)? """
        an = models.Answer.find_one({
            'user_id': userId,
            'question_id': qid})
        return an
    
    def getAni(self, userId: str, qid: str) -> int: 
        """ get the (ani) answer for a question """
        an = self.getAnswer(userid, qid)
        if an: 
            return an.ani
        else:
            return 0
        
    def getAns(self, userId: str, qid: str) -> str: 
        """ get the (ans) answer for a question """
        an = self.getAnswer(userid, qid)
        if an: 
            return an.ans
        else:
            return ""

    def calcComposites(self, userId):
        """ calculate the composites for the Myers-Briggs for user (userId) 
        """
        def aEx(shortQid): 
            return self.answerExists(userId, self.fullQid(shortQid))
        def ani(shortQid): 
            return self.getAni(userId, self.fullQid(shortQid))
        def ans(shortQid): 
            return self.getAns(userId, self.fullQid(shortQid))
        
        COMPOSITES = [
            ("EI", ["Q1","Q5","Q9", "Q13","Q17"]),
            ("SN", ["Q2","Q6","Q10","Q14","Q18"]),
            ("TF", ["Q3","Q7","Q11","Q15","Q19"]),
            ("JP", ["Q4","Q8","Q12","Q16","Q20"]),
        
        if (all(aEx(q) for q in eiQs)
            and any(ans(q)!="--" for q in eiQs)):
            ei = sum(ani(q) for q in eiQs)
            
        for compName, compSQs in COMPOSITES:
            if (all(aEx(q) for q in compSQs)
                and any(ans(q)!="--" for q in compSQs)):
                compVal = sum(ani(q) for q in compSQs)
                saveAnswer(userId, fullQid("C-"+compName), compVal)
        #//for    
            
            

#---------------------------------------------------------------------

#end
