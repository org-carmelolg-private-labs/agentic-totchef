from lib.tool import KindergartenTools, HomeKitchenTools
from lib.utils import PromptUtils, OllamaUtils

#user_prompt = "What can I do if I call the spell 'Wingardium Leviosa'?"
#user_prompt = "What spell would I use to make objects levitate?"
user_prompt = "Dammi le ricette casalinghe a base di proteine?"

# get available functions
_functions = {}
_functions.update(KindergartenTools.available_functions())
_functions.update(HomeKitchenTools.available_functions())
functions = _functions

stream = OllamaUtils.chat(user_prompt=user_prompt, tools=functions)
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
