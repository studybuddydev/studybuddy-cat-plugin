from cat.mad_hatter.decorators import tool, hook
from datetime import datetime
from cat.mad_hatter.decorators import hook

print("passo dal studybuddy plugin")


@hook(priority=1) # default priority is 1
def agent_prompt_prefix(prefix, cat):
    prefix = """You are StudyBuddy AI, an intelligent AI that passes the Turing test.
                you are a tutor for university students that can help both answering their questions related to the context and to help planning the study.
                You answer Human using tools and context."""
    return prefix


esami = ['storia', 'gattologia', 'sapobully']

@tool(return_direct=False)
def get_esami(input, cat):
    """
        return the list of exams to prepare for.
  
        Example inputs:
        "which exams do I have to prepare for"
        "what exams do I have to prepare for"
        "what are the exams i have to do?"

  
    """
    print('eccomi nel tool getesami') 
    return "You have to prepare for the following exams: " + str(esami)


@tool(return_direct=True)
def add_esame(name, cat):
    """Add exam to the exam list. Replies when user say "add exam" or similar, add exam only if it is clear the user want to add an exam. Argument "name" is the name of the exam to add."""
    esami.append(name)
    
    return "Exam added "+ name




@tool(return_direct=True)









