from cat.mad_hatter.decorators import tool, hook
from datetime import datetime
from cat.mad_hatter.decorators import hook

print("passo dal studybuddy plugin")

esami = ['storia', 'cruccolo', 'sapobully']

@hook(priority=1) # default priority is 1
def agent_prompt_prefix(prefix, cat):
    prefix = """You are StudyBuddy AI, an intelligent AI that passes the Turing test.
                you are a tutor for university students that can help both answering their questions related to the context and to help planning the study.
                You answer Human using tools and context."""
    return prefix




@hook(priority=1)  # default priority = 1
def before_rabbithole_splits_text(doc, cat):
    # do whatever with the doc
    print("I'm in the before_rabbithole_splits_text hook")
    print(doc.text)
    return doc

@hook(priority=1)  # default priority = 1
def after_rabbithole_splitted_text(chunks, cat):
    # post process the chunks
    print("I'm in the after_rabbithole_splitted_text hook")
    print(chunks)

    return chunks


@tool(return_direct=True)
def get_esami(input, cat):
    """Get exams from the exams list. User may ask "What exams do I have to prepare for?" or similar."""
    
    print('eccomi nel tool getesami')

    return "You have to prepare for the following exams: " + str(esami)


@tool(return_direct=True)
def add_esame(exam, cat):
    """Add exam to the exam list. User may say "add exam" or similar. Argument "exam" is the name of the exam to add."""
    esami.append(exam)
    
    return "Exam added "+ exam





