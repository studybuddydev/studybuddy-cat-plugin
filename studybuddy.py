from cat.mad_hatter.decorators import tool, hook


print("passo dal studybuddy plugin")

@hook(priority=1) # default priority is 1
def agent_prompt_prefix(prefix, cat):
    prefix = """You are StudyBuddy AI, an intelligent AI that passes the Turing test.
                you are a tutor for university students that can help both answering their questions related to the context and to help planning the study.
                You answer Human using tools and context."""
    return prefix