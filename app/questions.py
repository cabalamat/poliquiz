# questions.py = list of questions

"""
# Questions for Poliquiz

This is the list of questions. Questions are of two types:

(1) agree/disagree, with options that mathematical linear relation to 
    each other.
(2) multi-choice, wih a series of options that have no linear relation.

## Agree/Disagree Questions

These have a range of linear answers from +2 to -2. There is also an option 
of Don't Know, which odesn't count as anything on the linear progression.

Example:

Q: Britain was right to leave the EU.
() Strongly agree [+2]
() Agree [+1]
() Neutral [0]
() Disagree [-1]
() Strongly disagree [-2]
() Don't know / Other [--]

## Multi-Choice Questions

Here the user is presented with a list of choices which are not linearly 
related to each other.

Example:

Q: Which of these foods do you most like?
() Strawberries
() Raspberries
() Bananas
() Don't know / Don't care / Other [--]

"""

from questlib import mcq, adq, group

#---------------------------------------------------------------------

group("Voting (UK)",
intro="""\
Questions on how you have voted in elections and referendums, 
in a UK context.
""")


mcq("Who did you vote for in the UK general election in December 2019",
["Conservatives",    
"Labour",
"Liberal Democrats",
"Scottish National Party (SNP)",
"Green Party",
"Brexit Party",
"Democratic Unionist Party (DUP)",
"Sinn Féin",
"Plaid Cymru",
"Alliance Party",
"Socal Democratic and Labour Party (SDLP)",
"Ulster Unionist Party (UUP)",
"Yorkshire Party",
"Scottish Green Party",
"UKIP",
"Someone else",
"Didn't vote"]
)

mcq("How did you vote in the Brexit referendum in June 2016",
["Leave the EU",
"Remain in the EU",
"Didn't vote"]
)

#---------------------------------------------------------------------
# secession

group("Secession (UK)",
intro="""\
Questions on entities leaving other entities, in a UK context.

This contains questions on Brexit and questions on whether the 
consitutent parts of the UK sohuld split up.
""")

adq("Britain was right to leave the EU")

adq("""Britain will be economically better off outside the EU 
than it would be if it had remained in it.""")

adq("""Britain will have more influence in the world outside the EU 
than it would have if it had remained in it.""")

adq("Scotland should leave the UK and be an independent country")

adq("If Scotland leaves the UK, it should rejoin the EU")

adq("Northern Ireland should leave the UK and be an independent country")

adq("Northern Ireland should leave the UK and join the Republic of Ireland")

adq("Wales should leave the UK and be an independent country")

adq("If Wales leaves the UK, it should rejoin the EU")

adq("England should leave the UK and be an independent country")

adq("If England leaves the UK, it should rejoin the EU")


#---------------------------------------------------------------------

group("Myers-Briggs",
intro="""      
The **Myers-Briggs Type Inventory** assesses personality over four axes.

These are: 

* Extraversion (E) -- Introversion (I)
* Sensing (S) -- Intuition (N)
* Thinking (T) -- Feeling (F)
* Judgement (J) -- perception (P)

Each question gives you two options labelled (a) and (b). An example question might be:

> Following a schedule: (a) appeals to me, rather than (b) cramping me

If you agree with (a), select "agree" or "strongly agree". If you prefer (b),
select  "disagree" or "strongly disagree".
""")

adq("""When I am with a group of people I prefer: 
(a) joining in the talk of the group,
over (b) talking individually with people I know well""", 
"Q1")

adq("""I usually get along better with:
(a) realistic people,
rather than (b) imaginative people""", 
"Q2")

adq("""Of the two words I prefer:
(a) Analyze,
over (b) Sympathize""", 
"Q3")

adq("""Following a schedule:
(a) appeals to me,
rather than (b) cramping me""", 
"Q4")

adq("""When I have to meet strangers, I find it:
(a) pleasant, 
rather than (b) something that takes a good deal of effort""", 
"Q5")

adq("""If I was a teacher, I would rather teach:
(a) factual courses,   
rather than (b) courses involving theory""", 
"Q6")

adq("""Of the two words I prefer:
(a) foresight, 
over (b) compassion""", 
"Q7")

adq(""" I prefer to:
(a) arrange dates, parties, etc., well in advance,     
rather than (b) be free to do whatever looks like fun when the time comes""", 
"Q8")

adq("""I am:
(a) easy to get to know   
rather than (b) hard to get to know""", 
"Q9")

adq("""It is higher praise to say someone has: 
(a) common sense,  
rather than (b) vision""", 
"Q10")

adq("""I would rather be thought of as:
(a) firm, 
rather than (b) gentle""", 
"Q11")

adq("""The idea of making a list of what I should get done over a weekend:
(a) appeals to me, 
rather than (b) Leaves me cold""", 
"Q12")

adq("""I tend to have:
(a) broad friendships with many different people, 
rather than (b) deep friendships with a very few people""", 
"Q13")

adq("""I would rather have as a friend someone who:
(a) has both feet on the ground, 
rather than (b) is always coming up with new ideas""", 
"Q14")

adq("""Of the two words I prefer:
(a) thinking, 
over (b) feeling""", 
"Q15")

adq("""When it is settled well in advance that I will do a 
certain thing at a certain time, I find it:
(a) nice to be able to plan accordingly, 
rather than (b) a little unpleasant to be tied down""", 
"Q16")

adq("""At parties, I:
(a) always have fun, 
rather than (b) sometimes get bored""", 
"Q17")

adq("""I would rather be considered:
(a) a practical person, 
rather than (b) an ingenious person""", 
"Q18")

adq("""It is a higher compliment to be called:
(a) a consistently reasonable person, 
rather than (b) a person of real feeling""", 
"Q19")

adq("""It is harder for me to adapt to:
(a) constant change, 
rather than (b) routine""", 
"Q20")

#---------------------------------------------------------------------






#end
