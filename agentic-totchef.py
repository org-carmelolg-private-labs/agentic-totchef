from lib.adapters.outbound import LLMExecutor

user_prompt = "Dammi le ricette casalinghe a base di verdure?"
# user_prompt = "Dammi il menu di martedì della seconda settimana del nido"

first_response = LLMExecutor.chat(prompt=user_prompt, chatbot_mode=False).message.content

print(first_response)
print('************************')

second_response = LLMExecutor.ask(prompt=first_response,
                                  system_prompt="Ti è stato consegnata una lista di verdure. Restituisci solo quelle con il nome che inizia per C",
                                  chatbot_mode=False).message.content

print(second_response)

# for chunk in stream:
#    print(chunk['message']['content'], end='', flush=True)
