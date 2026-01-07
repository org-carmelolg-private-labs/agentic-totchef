from lib.core.service import LLMService

user_prompt = "Dammi le ricette casalinghe a base di verdure?"
#user_prompt = "Dammi il menu di martedì della seconda settimana del nido"


stream = LLMService.chat(prompt=user_prompt)
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
