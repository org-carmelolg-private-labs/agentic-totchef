from lib.adapters.outbound import LLMExecutor

print("Welcome to TotChef Chat! Type 'exit' or 'quit' to end the chat.")

# Start chat
while True:
    user_prompt = input('\nUser > ')
    if user_prompt.lower() in ['exit', 'quit']:
        break
    else:
        print('Assistant >', end=' ')
        stream = LLMExecutor.chat(prompt=user_prompt)
        # print the response from the chatbot in real-time
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
