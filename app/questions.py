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

from quest import mcq, adq, group

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

adq("""Following a schedule:
(a) appeals to me,
rather than (b) cramping me""")

adq("""When I am with a group of people I prefer: 
(a) joining in the talk of the group,
over (b) talking individually with people I know well""")

adq("""I usually get along better with:
(a) realistic people,
rather than (b) imaginative people""")


#---------------------------------------------------------------------






#end
